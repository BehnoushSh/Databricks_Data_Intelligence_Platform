# Databricks notebook source
# MAGIC %md
# MAGIC 
<div style="text-align: center; line-height: 0; padding-top: 9px;">
  <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning">
</div>


# COMMAND ----------

# MAGIC %md
# MAGIC # Example Solution for Capstone Project

# COMMAND ----------

# MAGIC %run ../Includes/Classroom-Setup-Project

# COMMAND ----------

print(f"Username:          {DA.username}")
print(f"Catalog Name:      {DA.catalog_name}")
print(f"Schema Name:       {DA.schema_name}")
print(f"Working Directory: {DA.paths.working_dir}")
print(f"Dataset Location:  {DA.paths.datasets}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Task 1: Ingest Data and Pre-processing
# MAGIC
# MAGIC * Create table named **`customer_demographics`** and **`customer_details`**
# MAGIC
# MAGIC * Create new silver table named **`customer_silver_merged`**
# MAGIC
# MAGIC * Join **`customer_details`** and **`customer_demographics`** tables
# MAGIC
# MAGIC * Save the resulting data in the **`customer_silver_merged`** table

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Create table customer_demographics and copy data into it
# MAGIC CREATE TABLE IF NOT EXISTS customer_demographics;
# MAGIC COPY INTO customer_demographics
# MAGIC   FROM "${DA.paths.datasets}/telco/customer-demographics.csv"
# MAGIC   FILEFORMAT = CSV
# MAGIC   FORMAT_OPTIONS ('inferSchema' = 'true', 'header' = 'true')
# MAGIC   COPY_OPTIONS ('mergeSchema' = 'true')

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM customer_demographics;

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Create table customer_details and copy data into it
# MAGIC CREATE TABLE IF NOT EXISTS customer_details;
# MAGIC COPY INTO customer_details
# MAGIC   FROM "${DA.paths.datasets}/telco/customer-details.csv"
# MAGIC   FILEFORMAT = CSV
# MAGIC   FORMAT_OPTIONS ('inferSchema'= 'true', 'header'= 'true')
# MAGIC   COPY_OPTIONS ('mergeSchema' = 'true')

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM customer_details;

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Create the customer_silver_merged table and save data by joining customer_details, customer_demographics table
# MAGIC
# MAGIC CREATE OR REPLACE TABLE customer_silver_merged AS
# MAGIC SELECT 
# MAGIC     CASE 
# MAGIC         WHEN cd.customerID IS NOT NULL THEN cd.customerID
# MAGIC         ELSE cdm.customerID
# MAGIC     END AS customerIdNew,
# MAGIC     cd.PhoneService, 
# MAGIC     cd.MultipleLines,
# MAGIC     cd.InternetService,
# MAGIC     cd.OnlineSecurity,
# MAGIC     cd.OnlineBackup,
# MAGIC     cd.DeviceProtection,
# MAGIC     cd.TechSupport, 
# MAGIC     cd.StreamingTV, 
# MAGIC     cd.StreamingMovies,
# MAGIC     cd.Contract,
# MAGIC     cd.PaperlessBilling,
# MAGIC     cd.PaymentMethod,
# MAGIC     cd.MonthlyCharges, 
# MAGIC     cd.TotalCharges,
# MAGIC     cd.Churn,
# MAGIC     cdm.*
# MAGIC FROM customer_details cd
# MAGIC LEFT JOIN customer_demographics cdm ON cd.customerID = cdm.customerID;
# MAGIC
# MAGIC SELECT * FROM customer_silver_merged;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Task 2: Feature Engineering
# MAGIC
# MAGIC * Loading the Customer Data
# MAGIC
# MAGIC * Selecting Columns to Keep
# MAGIC
# MAGIC     Adhering to best practices for feature selection, we consider factors such as domain knowledge, correlation analysis, and feature importance assessment to choose the most relevant columns for modeling.
# MAGIC
# MAGIC * One-Hot Encoding Categorical Features
# MAGIC
# MAGIC * Converting Integer Columns to Float64
# MAGIC
# MAGIC * Clean-Up Column Names
# MAGIC
# MAGIC * Creating and Writing to a Feature Store Table
# MAGIC
# MAGIC * Load the features we saved in the previous step and use these features to train a model.
# MAGIC

# COMMAND ----------

import pyspark.pandas as ps
import re

# Load the 'customer_silver_merged' table
df_customers_silver = spark.sql("SELECT * FROM customer_silver_merged")

# Define the columns to keep
# Selected relevant feature columns for analysis, including key factors like customer demographics (gender, SeniorCitizen, Partner),
# service details (PhoneService, InternetService, Contract, PaymentMethod), and tenure-related information (MonthlyCharges, tenure).
columns_to_keep = [
    "PhoneService",
    "InternetService",
    "Contract",
    "PaymentMethod",
    "MonthlyCharges",
    "customerID",
    "gender",
    "SeniorCitizen",
    "Partner",
    "tenure",
    # Add other columns you want to keep here
]

# Overwrite the DataFrame by selecting the desired columns
df_customers_silver = df_customers_silver.select(*columns_to_keep)

# Convert the DataFrame to a PySpark DataFrame
df_customers_silver = ps.DataFrame(df_customers_silver)

# One-hot-encode categorical features
df_customers_ohe = ps.get_dummies(
    df_customers_silver,
    columns=[
        "gender",
        "SeniorCitizen",
        "Partner",
        "PhoneService",
        "InternetService",
        "Contract",
        "PaymentMethod",
    ],
    dtype="float64",
)

# Convert integer columns to float64 - this is a best practice for ML
df_customers_ohe['tenure'] = df_customers_ohe['tenure'].astype('float64')

# Clean-up column names
df_customers_ohe.columns = [
    re.sub(r"[^a-zA-Z0-9_]", "_", col).lower() for col in df_customers_ohe.columns
]

# Display information about the final DataFrame
df_customers_ohe.info()

# COMMAND ----------

from databricks.feature_store import FeatureStoreClient
from databricks.feature_store import FeatureLookup
fs = FeatureStoreClient()

#drop table if exists
try:
    fs.drop_table('customer_features')
except:
    pass

fs.create_table(
  name = "customer_features",
  primary_keys = ["customerid"],
  schema = df_customers_ohe.spark.schema(),
  description="This customer-level table contains one-hot encoded and numeric features."
)

fs.write_table(df=df_customers_ohe.to_spark(), name="customer_features", mode="overwrite")

# Execute a SQL query to select all rows and columns from the 'customer_features' table
result = spark.sql("SELECT * FROM `customer_features`")

# Display the result using the 'display' function
display(result)

# COMMAND ----------

# Load the 'customer_silver_merged' table
sdf_customers_details = spark.sql("SELECT * FROM `customer_details`")

# Create a DataFrame to use for retrieving features
sdf_lookup = sdf_customers_details.select(['customerID', 'PaperlessBilling'])

feature_lookups = [
    FeatureLookup(
        table_name='customer_features',
        lookup_key='customerID'
    )
]

customer_data_set = fs.create_training_set(
    df=sdf_lookup,
    feature_lookups=feature_lookups,
    label='PaperlessBilling',
    exclude_columns=['customerID']
)

training_df = customer_data_set.load_df().toPandas()

display(training_df)

# COMMAND ----------

# MAGIC %md
# MAGIC ## [Stand-out]: Create Feature Store Table from an Existing Table
# MAGIC
# MAGIC Feature engineering with Unity Catalog supports creating a feature table from any Delta table. **Please note that this feature is in Public Preview**. You can learn more about [feature store and Unity Catalog on Databricks Documentation](https://docs.databricks.com/en/machine-learning/feature-store/uc/feature-tables-uc.html). 
# MAGIC
# MAGIC In order to create a feature table from an existing Delta table, first, we need to set a primary key colum and set as `NOT NULL` and add a primary key constraint. 
# MAGIC
# MAGIC After creating and configuring the feature table, you can view it in Features UI from left sidebar. 
# MAGIC

# COMMAND ----------

# create a copy of the merged table to use as a feature store 
create_table_sql = f"""
  CREATE OR REPLACE TABLE `customer_features_in_uc`
  AS SELECT * FROM `customer_silver_merged`
"""

# Execute the SQL command to create the feature table
spark.sql(create_table_sql)

# set primary key column to not null
spark.sql("ALTER TABLE `customer_features_in_uc` ALTER COLUMN customerIdNew SET NOT NULL")
spark.sql("ALTER TABLE `customer_features_in_uc` ADD CONSTRAINT customer_features_in_uc_pk PRIMARY KEY(customerIdNew)")

# COMMAND ----------

# MAGIC %sql
# MAGIC -- table details should show constraints details at the end of the output
# MAGIC DESCRIBE TABLE EXTENDED `customer_features_in_uc`;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Task 3: Baseline Model
# MAGIC
# MAGIC Let's initiate an AutoML experiment to construct a baseline model for predicting a customer's billing preference (paperless or not). The target field for this prediction will be the `paperlessbilling` field.
# MAGIC
# MAGIC Follow these step-by-step instructions to create an AutoML experiment:
# MAGIC
# MAGIC 1. Navigate to the **Experiments** section in Databricks.
# MAGIC
# MAGIC 2. Click on **Create AutoML Experiment** located in the top-right corner.
# MAGIC
# MAGIC 3. Choose a cluster to execute the experiment.
# MAGIC
# MAGIC 4. For the ML problem type, opt for **Classification**.
# MAGIC
# MAGIC 5. Select the `customer_silver_merged` table, which was created in the previous step, as the input training dataset.
# MAGIC
# MAGIC 6. Specify **`paperlessbilling`** as the prediction target.
# MAGIC
# MAGIC 7. Deselect the **customerdetailsID** field as it's not needed as a feature.
# MAGIC
# MAGIC 8. In the **Advanced Configuration** section, set the **Timeout** to **5 minutes**.
# MAGIC
# MAGIC 9. Enter a name for your experiment. Let's enter `PaperlessBilling_Prediction_AutoML_Experiment` as experiment name.
# MAGIC
# MAGIC **Optional Advanced Configuration:**
# MAGIC
# MAGIC - You have the flexibility to choose the **evaluation metric** and your preferred **training framework**.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Task 4: Train and Track A Model
# MAGIC
# MAGIC ##### Data Preparation:
# MAGIC * Splitting the data into training and testing sets.
# MAGIC * Mapping categorical labels ("Yes" and "No") to numerical values (0 and 1).
# MAGIC
# MAGIC ##### Hyperparameter Logging:
# MAGIC
# MAGIC * Logging hyperparameters, including n_estimators and random_state, for experiment tracking.
# MAGIC
# MAGIC ##### Model Initialization:
# MAGIC * Initializing a RandomForestClassifier with specified hyperparameters.
# MAGIC
# MAGIC ##### Model Training:
# MAGIC * Fitting the model to the training data.
# MAGIC
# MAGIC ##### Evaluation and Metric Logging:
# MAGIC * Calculating and logging the F1 score as a performance metric.
# MAGIC
# MAGIC ##### Feature Importance Logging:
# MAGIC * Calculating and logging feature importance scores for each feature.
# MAGIC
# MAGIC ##### Model Logging:
# MAGIC * Logging the trained model as an artifact for reproducibility.
# MAGIC
# MAGIC ##### Optional Model Loading:
# MAGIC * Demonstrating loading the trained model for making predictions.

# COMMAND ----------

import mlflow
import mlflow.sklearn
from mlflow.models.signature import infer_signature
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score

# set mlflow experiment path
mlflow.set_experiment(f"/Users/{DA.username}/Capstone-Example-Project")

# Assuming you already have 'training_df' as your prepared DataFrame

# Split the data into training and testing sets
X = training_df.drop("PaperlessBilling", axis=1)
y = training_df["PaperlessBilling"]
y = y.map({'Yes': 1.0, 'No': 0.0})
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Start an MLflow run
with mlflow.start_run(run_name='capstone_project_solution_run') as run:
    # Log custom hyperparameters 
    n_estimators = 101
    mlflow.log_param("n_estimators", n_estimators)
    random_state = 72
    mlflow.log_param("random_state", random_state)

    # Utilizing RandomForest for improved model performance due to complex, non-linear relationships in the data, which LogisticRegression may not capture effectively.
    # Initialize the Random Forest classifier with hyperparameters
    rf_classifier = RandomForestClassifier(n_estimators=n_estimators, random_state=random_state)

    # Fit the model on the training data
    rf_classifier.fit(X_train, y_train)

    # Make predictions on the test data
    y_pred = rf_classifier.predict(X_test)

    # Calculate and log F1 score
    test_f1 = f1_score(y_test, y_pred)
    mlflow.log_metric("test_f1", test_f1)

    # Log feature importance
    feature_importance = rf_classifier.feature_importances_
    for i, feature_name in enumerate(X_train.columns):
        mlflow.log_param(f"feature_importance_{i}", feature_importance[i])

    # Log the trained model as an artifact
    mlflow.sklearn.log_model(
        rf_classifier,
        artifact_path="model-artifacts",
        input_example=X_train[:3],
        signature=infer_signature(X_train, y_train)
    )

    model_uri = f"runs:/{run.info.run_id}/model-artifacts"

    # Load the trained model for demonstration (optional)
    loaded_model = mlflow.sklearn.load_model(model_uri)

    # Example of using the loaded model for predictions
    example_input = X_test.iloc[0:10]  # Use the first row of the test data as an example
    loaded_model_prediction = loaded_model.predict(example_input)
    print(f"Loaded model prediction: {loaded_model_prediction}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Task 5: Register the Model
# MAGIC
# MAGIC Now, let's register the trained model in the model registry:
# MAGIC
# MAGIC - Use the logged model from the previous step.
# MAGIC
# MAGIC - Provide a name and description for the model.
# MAGIC
# MAGIC - Register the model.

# COMMAND ----------

model_name = f"capstone_project_solution_run_{DA.unique_name('-')}"

# Register the model in the model registry
registered_model = mlflow.register_model(model_uri=model_uri, name=model_name)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## [Stand-out]: Automate With Workflows
# MAGIC
# MAGIC Now, let's create a workflow job to run this notebook automatically. In a real project, we would have splitted the code here into moduler components and run each module as a task in the Workflows. For the sake of simplicity, we have all the code in this single notebook. 
# MAGIC
# MAGIC With Workflows, we can automatically run this notebook to ingest data, train and register the model. 
# MAGIC
# MAGIC To create a Work
# MAGIC
# MAGIC - Navigate to the **Workflows** from the left sidebar.
# MAGIC
# MAGIC - Create a new workflow job by clicking **Create Job** button.
# MAGIC
# MAGIC - Configure the job to run this notebook on a regular schedule.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Task 6: Serve the Model
# MAGIC
# MAGIC We can create Model Serving endpoints with the Databricks Machine Learning API or the Databricks Machine Learning UI. An endpoint can serve any registered Python MLflow model in the **Model Registry**.
# MAGIC
# MAGIC In order to keep it simple, in this demo, we are going to use the Model Serving UI for creating, managing and using the Model Serving endpoints. We can create model serving endpoints with the **"Serving"** page UI or directly from registered **"Models"** page. 
# MAGIC
# MAGIC Let's create a model serving endpoint in Models page.
# MAGIC
# MAGIC - Go to **Models**, select the model you want to serve.
# MAGIC
# MAGIC - Click the **Use model for inference** button on the top right.
# MAGIC
# MAGIC - Select the **Real-time** tab.
# MAGIC
# MAGIC - Select the **model version** and provide an **endpoint name**. Let's enter *"Model_Serving_Demo_Endpoint"* as endpoint name.
# MAGIC
# MAGIC - Select the compute size for your endpoint, and specify if your endpoint should **scale to zero** when not in use.
# MAGIC
# MAGIC - Click **Create endpoint**. 
# MAGIC
# MAGIC
# MAGIC **View Model Serving Endpoint:**
# MAGIC
# MAGIC - Go to **"Serving"** page.
# MAGIC
# MAGIC - Select the endpoint we just created.
# MAGIC
# MAGIC - The Serving endpoints page appears with Serving endpoint state shown as Not Ready. After a few minutes, Serving endpoint state changes to Ready.
# MAGIC
# MAGIC **Query Serving Endpoint:**
# MAGIC
# MAGIC Let's use the deployed model for real-time inference. Here’s a step-by-step guide for querying an endpoint in Databricks Model Serving:
# MAGIC
# MAGIC - Go to the **Serving** endpoints page and select the endpoint you want to query.
# MAGIC
# MAGIC - Click **Query endpoint** button the top right corner.
# MAGIC
# MAGIC - There are 3 methods for querying an endpoint; browser, CURL, HTTP request. For now, let's use the easiest method; querying right in the browser window. In this method, we need to provide the input parameters in JSON format. As our model is created with AutoML, an example is already registered with model. Click **Show example** button to populate the request field with and example query. Change the input values as you wish.
# MAGIC
# MAGIC - Click **Send request**.
# MAGIC
# MAGIC - **Response** field on the right panel will show the result of the inference.
# MAGIC
# MAGIC **Automate with Workflows:**
# MAGIC
# MAGIC Now, let's create a workflow job to run a notebook automatically:
# MAGIC
# MAGIC - Navigate to the **Jobs** section in Databricks.
# MAGIC
# MAGIC - Create a new workflow job.
# MAGIC
# MAGIC - Configure the job to run a specific notebook on a regular schedule.
# MAGIC
# MAGIC - Define the necessary parameters for the notebook.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## [Stand-out]: Model A/B Testing
# MAGIC
# MAGIC In this task, we will create another model and test it using the same existing model serving endpoint to ensure it's working correctly.
# MAGIC
# MAGIC - **Create a New Model:** Develop and train a new machine learning model that you want to test. This model should be registered in your Databricks Model Registry as a new version.
# MAGIC
# MAGIC - **Register the New Model Version:** In the Databricks Model Registry, register the newly created model as a new version. Make sure it's versioned and labeled appropriately.
# MAGIC
# MAGIC - **Update the Existing Model Serving Endpoint:**
# MAGIC
# MAGIC    - Go to the **Serving** page or **Models** page, where you originally created the model serving endpoint in Task 6.
# MAGIC    - Select the existing model serving endpoint that you want to update.
# MAGIC    - Look for an option to modify the endpoint or change the model version it is serving.
# MAGIC    - Update the endpoint to serve the new model version (the one created in this task).
# MAGIC
# MAGIC - **Test the Updated Endpoint:** After updating the model serving endpoint, test it to ensure it's working correctly with the new model version.
# MAGIC
# MAGIC    - Go to the **Serving** page and select the updated endpoint.
# MAGIC    - Use the same method mentioned in Task 6 to query the endpoint, but this time, specify input data for testing the new model version.
# MAGIC    - Click **Send request** and check the **Response** field to verify that the endpoint is correctly serving predictions using the new model.
# MAGIC
# MAGIC - **Evaluate Results:** Evaluate the results from the updated endpoint to ensure that the new model version is providing accurate predictions and behaving as expected.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Classroom Clean-up
# MAGIC
# MAGIC After completing the demo, it's important to clean up any resources that were created.
# MAGIC
# MAGIC Run the following cell to remove lessons-specific assets created during this lesson.

# COMMAND ----------

DA.cleanup()

# COMMAND ----------

# MAGIC %md
# MAGIC 
&copy; 2024 Databricks, Inc. All rights reserved.<br/>
Apache, Apache Spark, Spark and the Spark logo are trademarks of the 
<a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
<br/><a href="https://databricks.com/privacy-policy">Privacy Policy</a> | 
<a href="https://databricks.com/terms-of-use">Terms of Use</a> | 
<a href="https://help.databricks.com/">Support</a>