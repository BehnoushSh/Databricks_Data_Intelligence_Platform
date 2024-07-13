# Databricks notebook source
# MAGIC %md
# MAGIC 
<div style="text-align: center; line-height: 0; padding-top: 9px;">
  <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning">
</div>


# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # End-to-End ML on the DI Platform
# MAGIC
# MAGIC In this demo, we'll explore the process of performing end-to-end machine learning on the Databricks DI platform. We'll cover creating a feature store table, training and tracking a machine learning model, registering the model in the model registry, transitioning the model to the "production" stage, and automating these steps using workflows.
# MAGIC
# MAGIC **Learning Objectives:**
# MAGIC - Create a feature store table using an existing Delta Lake table for model training purposes.
# MAGIC - Automatically generate a notebook to batch compute model predictions on a holdout set.
# MAGIC - Recognize the types of assets that can be automated with Jobs.
# MAGIC - Automate the execution of a single notebook using Jobs.
# MAGIC - Review the outcomes of a completed single-notebook Job.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Requirements
# MAGIC
# MAGIC Please review the following requirements before starting the lesson:
# MAGIC
# MAGIC * To run this notebook, you need to use one of the following Databricks runtime(s): **any**

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Classroom Setup
# MAGIC
# MAGIC To ensure a smooth experience, follow these initial steps:
# MAGIC
# MAGIC 1. Run the provided classroom setup script. This script will establish necessary configuration variables tailored to each user. Execute the following code cell:

# COMMAND ----------

# MAGIC %run ../Includes/Classroom-Setup-02

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Other Conventions:**
# MAGIC
# MAGIC Throughout this demo, we'll make use of the object `DA`, which provides critical variables. Execute the code block below to understand its purpose:
# MAGIC

# COMMAND ----------

print(f"Username:          {DA.username}")
print(f"Catalog Name:      {DA.catalog_name}")
print(f"Schema Name:       {DA.schema_name}")
print(f"Working Directory: {DA.paths.working_dir}")
print(f"User DB Location:  {DA.paths.user_db}")

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Feature Engineering with Feature Store

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ### Ingest Data and Pre-processing
# MAGIC
# MAGIC Before proceeding, let's prepare our data:
# MAGIC
# MAGIC 1. Import a CSV file into a Databricks table.
# MAGIC 2. This will serve as the foundation for our feature store table.

# COMMAND ----------

import pyspark.pandas as ps
import pandas as pd
from pyspark.sql.functions import col
import re

# read data sets and join them by customer id
sdf_customer_demographics = spark.read.csv(
    f"{DA.paths.datasets}/telco/customer-demographics.csv",
    header=True,
    inferSchema=True,
)
sdf_customer_details = spark.read.csv(
    f"{DA.paths.datasets}/telco/customer-details.csv", header=True, inferSchema=True
).withColumnRenamed("customerID", "id")

sdf_customers = sdf_customer_demographics.join(
    sdf_customer_details, col("customerID") == col("id")
)

# convert spark data frame to pyspark dataframe
df_customers = ps.DataFrame(sdf_customers)

# exclude columns that we don't want to use
df_customers = df_customers.drop(
    columns=[
        "Dependents",
        "id",
        "MultipleLines",
        "OnlineSecurity",
        "OnlineBackup",
        "DeviceProtection",
        "TechSupport",
        "PaperlessBilling",
        "TotalCharges",
    ]
)

# one-hot-encode categorical features
df_customers_ohe = ps.get_dummies(
    df_customers,
    columns=[
        "gender",
        "SeniorCitizen",
        "Partner",
        "PhoneService",
        "InternetService",
        "StreamingTV",
        "StreamingMovies",
        "Contract",
        "PaymentMethod",
    ],
    dtype="float64",
)
# Convert integer columns to float64 - this best practice for mlflow
df_customers_ohe['tenure'] = df_customers_ohe['tenure'].astype('float64')


# clean-up column names
df_customers_ohe.columns = [
    re.sub(r"[^a-zA-Z0-9_]", "_", col).lower() for col in df_customers_ohe.columns
]

# let's review the final data set
df_customers_ohe.info()

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ### Create a Feature Table
# MAGIC
# MAGIC Now, let's create a feature store table from the previously created table.
# MAGIC
# MAGIC Next, use the `feature_table` operation to register the DataFrame as a Feature Store table.
# MAGIC
# MAGIC To do this, provide the following:
# MAGIC
# MAGIC 1. The `name` of the database and table where we want to store the feature table
# MAGIC 1. The `keys` for the table
# MAGIC 1. The `schema` of the table
# MAGIC 1. A `description` of the contents of the feature table
# MAGIC
# MAGIC
# MAGIC **📌 Important:**  The prediction column, `Churn` in this case, should NOT BE included as a feature in the registered feature table. 
# MAGIC
# MAGIC
# MAGIC **📌 Important:** Feature Store - Unity Catalog integration is in public preview. If this feature is not enabled for your workspace, you need to create the feature table in hive_metastore.

# COMMAND ----------

from databricks.feature_store import FeatureStoreClient
fs = FeatureStoreClient()

#drop table if exists
try:
    fs.drop_table('customer_features')
except:
    pass

# exclude prediction column and save the features to the feature table
df_customers_ohe = df_customers_ohe.drop(columns=["churn"])

fs.create_table(
  name = "customer_features",
  primary_keys = ["customerid"],
  schema = df_customers_ohe.spark.schema(),
  description="This customer-level table contains one-hot encoded and numeric features."
)

fs.write_table(df=df_customers_ohe.to_spark(), name="customer_features", mode="overwrite")

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Review Feature Table:**
# MAGIC
# MAGIC After creating the customers feature table, review it in **Features** section. Similar to other tables, you will be able to view table details, sample data, and lineage information.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Load Features
# MAGIC
# MAGIC Let's load the features we saved in the previous step and use these features to train a model.
# MAGIC
# MAGIC At the end we are getting the same data set as we started! However, it is important to understand that we loaded features from the feature store. In a real-life scenario, we process features first and then retrieve them when needed.

# COMMAND ----------

from databricks.feature_store import FeatureLookup

fs = FeatureStoreClient()

# a dataframe to use for retreving features
sdf_lookup = sdf_customer_details.select(['id','Churn'])

feature_lookups = [
    FeatureLookup(
      table_name = 'customer_features',
      lookup_key = 'id'
    )
]

training_set = fs.create_training_set(
    df = sdf_lookup,
    feature_lookups = feature_lookups,
    label = 'Churn',
    exclude_columns = ['id']
)

training_df = training_set.load_df().toPandas()

display(training_df)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Model Tracking and Management with MLflow
# MAGIC
# MAGIC In this section, we will use MLflow to track and manage models. First, we will load features

# COMMAND ----------

# MAGIC %md
# MAGIC ### Train and Track Model
# MAGIC
# MAGIC Next, we'll train a machine learning model using scikit-learn.

# COMMAND ----------

import mlflow
import mlflow.sklearn
from mlflow.models.signature import infer_signature

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score

# set the path for mlflow experiment
mlflow.set_experiment(f"/Users/{DA.username}/M02-End-to-end-ML-Lakehouse")

X = training_df.drop("Churn", axis=1)
y = training_df["Churn"]

# Convert categorical labels to numerical labels
y = y.map({'Yes': 1.0, 'No': 0.0})

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

with mlflow.start_run(run_name = 'end_to_end_ml_on_databricks_run') as run:
    # Initialize the Random Forest classifief
    rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)

    # Fit the model on the training data
    rf_classifier.fit(X_train, y_train)

    # Make predictions on the test data
    y_pred = rf_classifier.predict(X_test)

    mlflow.log_metric("test_f1", f1_score(y_test, y_pred))
        
    mlflow.sklearn.log_model(
        rf_classifier,
        artifact_path = "model-artifacts", 
        input_example=X_train[:3],
        signature=infer_signature(X_train, y_train)
    )

    model_uri = f"runs:/{run.info.run_id}/model-artifacts"

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ### Register the Model
# MAGIC
# MAGIC Now, let's register the trained model in the model registry:
# MAGIC
# MAGIC 1. Use the logged model from the previous step.
# MAGIC 2. Provide a name and description for the model.
# MAGIC 3. Register the model.

# COMMAND ----------

model_name = f"end_to_end_ml_on_db_model_{DA.unique_name('-')}"

# Register the model in the model registry
registered_model = mlflow.register_model(model_uri=model_uri, name=model_name)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ### Manage Model Stages
# MAGIC
# MAGIC As the model is registered into Model Registry, we can manage its stage using the UI or the API. In this demo, we will use the API to transition registered model to `Staging` stage.

# COMMAND ----------

from mlflow.tracking.client import MlflowClient

client = MlflowClient()

# Transition the model to the "Production" stage
client.transition_model_version_stage(
    name = registered_model.name,
    version = registered_model.version,
    stage = "Staging"
)

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Serve Model with Model Serving
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

# COMMAND ----------

# MAGIC %md
# MAGIC ### Query Serving Endpoint
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

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Automate with Workflows
# MAGIC
# MAGIC Now, let's create a workflow job to run a notebook automatically:
# MAGIC
# MAGIC 1. Navigate to the **Jobs** section in Databricks.
# MAGIC 2. Create a new workflow job.
# MAGIC 3. Configure the job to run a specific notebook on a regular schedule.
# MAGIC 4. Define the necessary parameters for the notebook.

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
# MAGIC ## Conclusion
# MAGIC
# MAGIC In this comprehensive demo, we covered the entire process of performing machine learning on the Databricks DI platform. From data preparation and creating a feature table to training, tracking, and deploying a model, we demonstrated how Databricks provides an integrated environment for managing and deploying machine learning models efficiently.

# COMMAND ----------

# MAGIC %md
# MAGIC 
&copy; 2024 Databricks, Inc. All rights reserved.<br/>
Apache, Apache Spark, Spark and the Spark logo are trademarks of the 
<a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
<br/><a href="https://databricks.com/privacy-policy">Privacy Policy</a> | 
<a href="https://databricks.com/terms-of-use">Terms of Use</a> | 
<a href="https://help.databricks.com/">Support</a>