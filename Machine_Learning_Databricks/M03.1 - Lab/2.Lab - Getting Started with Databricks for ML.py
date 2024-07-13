# Databricks notebook source
# MAGIC %md
# MAGIC 
<div style="text-align: center; line-height: 0; padding-top: 9px;">
  <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning">
</div>


# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # 2.Lab - Getting Started with Databricks for ML
# MAGIC
# MAGIC In this lab, we will construct a comprehensive ML model pipeline using Databricks. Initially, we will train and monitor our model using mlflow. Subsequently, we will register the model and advance it to the next stage. In the latter part of the lab, we will utilize Model Serving to deploy the registered model. Following deployment, we will interact with the model via a REST endpoint and examine its behavior through an integrated monitoring dashboard.
# MAGIC

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
# MAGIC ## Lab Setup
# MAGIC
# MAGIC To ensure a smooth experience, follow these initial steps:
# MAGIC
# MAGIC 1. Run the provided classroom setup script. This script will establish necessary configuration variables tailored to each user. Execute the following code cell:

# COMMAND ----------

# MAGIC %run ../Includes/Classroom-Setup-Lab

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Other Conventions:**
# MAGIC
# MAGIC Throughout this lab, we'll make use of the object `DA`, which provides critical variables. Execute the code block below to see various variables that will be used in this notebook:
# MAGIC

# COMMAND ----------

print(f"Username:          {DA.username}")
print(f"Catalog Name:      {DA.catalog_name}")
print(f"Schema Name:       {DA.schema_name}")
print(f"Working Directory: {DA.paths.working_dir}")
print(f"Dataset Location:  {DA.paths.datasets}")

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Data Ingestion
# MAGIC The first step in this lab is to ingest data from .csv files and save them as delta tables. Then, we will join customer data and create a new table.

# COMMAND ----------

# MAGIC %sql
# MAGIC USE CATALOG ${DA.catalog_name};

# COMMAND ----------

print("CSV file paths:")
print(f"{DA.paths.datasets}/telco/customer-demographics.csv")
print(f"{DA.paths.datasets}/telco/customer-details.csv")

# COMMAND ----------

# MAGIC %sql
# MAGIC --Create table customer_demographics and copy data into it from the CSV file
# MAGIC <FILL-IN>
# MAGIC
# MAGIC --Create table customer_details and copy data into it from the CSV file
# MAGIC <FILL-IN>

# COMMAND ----------

# MAGIC %sql
# MAGIC --Create a customer table with combined data
# MAGIC CREATE OR REPLACE TABLE customers AS
# MAGIC SELECT cd.customerID AS ID,
# MAGIC     cd.PhoneService, 
# MAGIC     cd.Contract,
# MAGIC     cd.PaymentMethod,
# MAGIC     cd.MonthlyCharges, 
# MAGIC     cd.Churn,
# MAGIC     cdm.gender,
# MAGIC     cdm.tenure,
# MAGIC     cdm.Dependents
# MAGIC FROM customer_details cd
# MAGIC LEFT JOIN customer_demographics cdm ON cd.customerID = cdm.customerID
# MAGIC WHERE isnotnull(cd.Churn);
# MAGIC
# MAGIC SELECT * FROM customers;

# COMMAND ----------

import pyspark.pandas as ps
import pandas as pd
from pyspark.sql.functions import col

sdf = spark.sql("SELECT * FROM customers")
sdf = sdf.drop("ID")

pdf = ps.DataFrame(sdf)

training_df = ps.get_dummies(
    pdf,
    columns=[
        "gender",
        "Dependents",
        "PaymentMethod",
        "Contract",
        "PhoneService"
    ],
    dtype="float64",
).to_pandas()

# COMMAND ----------

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

X = training_df.drop("Churn", axis=1)
y = training_df["Churn"]

# Convert categorical labels to numerical labels
y = y.map({'Yes': 1.0, 'No': 0.0})

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# COMMAND ----------

mlflow.<FILL_IN>(f"/Users/{DA.username}/LAB-Get-Started-with-Databricks-for-ML")

# COMMAND ----------

with <FILL_IN>(run_name = 'gs_db_ml_LAB_run') as run:
    # Initialize the Random Forest classifief
    rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)

    # Fit the model on the training data
    rf_classifier.fit(<FILL_IN>)

    # Make predictions on the test data
    y_pred = rf_classifier.predict(<FILL_IN>)

    mlflow.<FILL_IN>("test_f1", <FILL_IN>)
        
    mlflow.<FILL_IN>(
        <FILL_IN>,
        artifact_path = "model-artifacts", 
        input_example=X_train[:3],
        signature=infer_signature(X_train, y_train)
    )

    model_uri = f"runs:/<FILL_IN>/model-artifacts"

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

model_name = f"gs_db_ml_LAB_{DA.unique_name('-')}"

#Register the model in the model registry
registered_model = <FILL_IN>

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ### Manage Model Stages
# MAGIC
# MAGIC As the model is registered into Model Registry, we can manage its stage using the UI or the API. In this demo, we will use the API to transition registered model to `Staging` stage.

# COMMAND ----------

from mlflow.tracking.client import MlflowClient
client = MlflowClient()

#Transition the model to the "Production" stage
client.<FILL_IN>(
    name = <FILL_IN>,
    version = <FILL_IN>,
    stage = <FILL_IN>
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
# MAGIC In this lab, we explored the full potential of Databricks Data Intelligence Platform for machine learning tasks. From data ingestion to model deployment, we covered essential steps such as data preparation, model training, tracking, registration, and serving. By utilizing MLflow for model tracking and management, and Model Serving for deployment, we demonstrated how Databricks offers a seamless workflow for building and deploying ML models. Through this comprehensive lab, users can gain a solid understanding of Databricks capabilities for ML tasks and streamline their development process effectively.

# COMMAND ----------

# MAGIC %md
# MAGIC 
&copy; 2024 Databricks, Inc. All rights reserved.<br/>
Apache, Apache Spark, Spark and the Spark logo are trademarks of the 
<a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
<br/><a href="https://databricks.com/privacy-policy">Privacy Policy</a> | 
<a href="https://databricks.com/terms-of-use">Terms of Use</a> | 
<a href="https://help.databricks.com/">Support</a>