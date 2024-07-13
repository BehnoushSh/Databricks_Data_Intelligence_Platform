# Databricks notebook source
# MAGIC %md
# MAGIC 
<div style="text-align: center; line-height: 0; padding-top: 9px;">
  <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning">
</div>


# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # Experimentation with AutoML
# MAGIC
# MAGIC In this demo, we will explore the powerful capabilities of AutoML (Automated Machine Learning) within Databricks. AutoML allows you to automatically build, train, and select the best machine learning models for your data without manual intervention. We will create an AutoML experiment, evaluate the results, register the best model, and transition it to the "Staging" stage.
# MAGIC
# MAGIC **Learning Objectives:**
# MAGIC - Create an AutoML experiment using the Experiments UI.
# MAGIC - Understand the various configuration options available in AutoML experiments.
# MAGIC - Evaluate the results of an AutoML experiment to identify the best model run.
# MAGIC - Open the automatically generated notebook associated with the best model run.
# MAGIC - Register the best model run as a new model with a version.
# MAGIC - Explore the inputs and outputs of the model version.
# MAGIC - Transition the model to the "Staging" stage for deployment.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Requirements
# MAGIC
# MAGIC Please review the following requirements before starting the lesson:
# MAGIC
# MAGIC * To run this notebook, you need to use one of the following Databricks runtime(s): **any**
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Classroom Setup
# MAGIC
# MAGIC Before diving into the demo, execute the provided classroom setup script. This script will define configuration variables required for the demo. Run the following code cell:

# COMMAND ----------

# MAGIC %run ../Includes/Classroom-Setup-02

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Other Conventions:**
# MAGIC
# MAGIC Throughout this demo, we'll use the object `DA` which provides important variables. Execute the code block below to understand the context:

# COMMAND ----------

print(f"Username:          {DA.username}")
print(f"Catalog Name:      {DA.catalog_name}")
print(f"Schema Name:       {DA.schema_name}")
print(f"Working Directory: {DA.paths.working_dir}")
print(f"User DB Location:  {DA.paths.user_db}")

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Prepare Data
# MAGIC
# MAGIC For this demonstration, we will utilize a fictional dataset from a Telecom Company, which includes customer information. This dataset encompasses customer demographics, including gender, as well as internet subscription details such as subscription plans and payment methods.
# MAGIC
# MAGIC To get started, execute the code block below. 
# MAGIC
# MAGIC This will create the `customers` table and allow us to explore its features.
# MAGIC
# MAGIC Also, it creates a second table `customers_to_predict` which we will use to predict with final model. 
# MAGIC

# COMMAND ----------

DA.create_customers_table()
spark.table('customers').printSchema()

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Create AutoML Experiment
# MAGIC
# MAGIC Let's initiate an AutoML experiment to construct a baseline model for predicting customer churn. The target field for this prediction will be the `Churn` field.
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
# MAGIC 5. Select the `customers` table, which was created in the previous step, as the input training dataset.
# MAGIC
# MAGIC 6. Specify **`Churn`** as the prediction target.
# MAGIC
# MAGIC 7. Deselect the **CustomerID** field as it's not needed as a feature.
# MAGIC
# MAGIC 8. In the **Advanced Configuration** section, set the **Timeout** to **5 minutes**.
# MAGIC
# MAGIC 9. Enter a name for your experiment. Let's enter `Churn_Prediction_AutoML_Experiment` as experiment name.
# MAGIC
# MAGIC **Optional Advanced Configuration:**
# MAGIC
# MAGIC - You have the flexibility to choose the **evaluation metric** and your preferred **training framework**.
# MAGIC
# MAGIC - If your dataset includes a timeseries field, you can define it when splitting the dataset.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## View the Best Run
# MAGIC
# MAGIC Once the experiment is finished, it's time to examine the best run:
# MAGIC
# MAGIC 1. Access the completed experiment in the **Experiments** section.
# MAGIC
# MAGIC 2. Identify the best model run by evaluating the displayed **metrics**. Alternatively, you can click on **View notebook for the best model** to access the automatically generated notebook for the top-performing model.
# MAGIC
# MAGIC 3. Utilize the **Chart** tab to compare and contrast the various models generated during the experiment.
# MAGIC
# MAGIC You can find all details for the run  on the experiment page. There are different columns such as the framework used (e.g., Scikit-Learn, XGBoost), evaluation metrics (e.g., Accuracy, F1 Score), and links to the corresponding notebooks for each model. This allows you to make informed decisions about selecting the best model for your specific use case.
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC **Import Notebooks for Other Experiment Trials in AutoML**
# MAGIC
# MAGIC For classification and regression experiments, AutoML generated notebooks for data exploration and the best trial in your experiment are automatically imported to your workspace. For all trials besides the best trial, the notebooks **are NOT created** automatically. If you need to use these notebooks, you can manually import them into your workspace with the **`automl.import_notebook`** Python API.
# MAGIC
# MAGIC **🚨 Notice:** `destination_path` takes Workspace as root.

# COMMAND ----------

from databricks import automl
from datetime import datetime
# Set up AutoML experiment
# Manually set up the experiment configuration based on UI details
automl_run = automl.classify(
    dataset=spark.table("customers"), 
    target_col="Churn", 
    exclude_cols=["CustomerID"], 
    timeout_minutes=5)

# Create the Destination path for storing the best run notebook
destination_path = f"/Users/{DA.username}/imported_notebooks/demo-01-{datetime.now().strftime('%Y%m%d%H%M%S')}"

# Get the path and url for the generated notebook
result = automl.import_notebook(automl_run.trials[5].artifact_uri, destination_path)
print(f"The notebook is imported to: {result.path}")
print(f"The notebook URL           : {result.url}")

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Register the Model
# MAGIC
# MAGIC To make use of the best model for operational purposes, we'll register it following these steps:
# MAGIC
# MAGIC 1. Start by clicking on the best run to access detailed information about it. This information typically includes essential details such as the `run id`, `parameters`, `metrics`, and `artifacts` used during the run.
# MAGIC
# MAGIC 2. Once you're on the model's details page, navigate to the **Model** section.
# MAGIC
# MAGIC 3. Look for the **Register Model** option and click on it. This action signifies your intention to formally register this model for use in production scenarios.
# MAGIC
# MAGIC 4. A dialog or form will appear, prompting you to provide a name for the model and specify a version. Let's enter **`Churn_Prediction_Base_Model`** as model name.
# MAGIC
# MAGIC 5. Finally, click the **Register** button to complete the registration process.
# MAGIC
# MAGIC If you are registering a new version of an existing model, select the relevant existing model from the list and click **Register**. This process allows you to maintain version history and updates for your models, ensuring seamless model management and deployment.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Manage Model Stage
# MAGIC
# MAGIC Now, let's move the registered model to the "Staging" stage:
# MAGIC
# MAGIC 1. Go to the **Models** section on the left panel.
# MAGIC
# MAGIC 2. Select the model we registered earlier (`Churn_Prediction_Base_Model`).
# MAGIC
# MAGIC 3. Click on the version you want to stage.
# MAGIC
# MAGIC 4. In the top right corner, click the **Stage** dropdown.
# MAGIC
# MAGIC 5. Choose **Transition to Staging**.
# MAGIC
# MAGIC 6. Optionally, add a comment.
# MAGIC
# MAGIC 7. Confirm the transition.
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Use Model For *Batch* Inference
# MAGIC
# MAGIC 1. Go to the **Models** section on the left panel.
# MAGIC
# MAGIC 1. Select the model we registered earlier (`Churn_Prediction_Base_Model`).
# MAGIC
# MAGIC 1. Click **Use Model for inference**.
# MAGIC
# MAGIC 1. Select **Batch Inference** tab.
# MAGIC
# MAGIC 1. Select model version.
# MAGIC
# MAGIC 1. Select input table that will be used for inference. In this case, there is a table, `customers_to_predict`, created for us to use for prediction. 
# MAGIC
# MAGIC 1. Select a destination for output notebook. 
# MAGIC
# MAGIC 1. Click **Use Model for batch inference**.
# MAGIC
# MAGIC This will generate a notebook that you can edit and run for using the model for inference. 
# MAGIC
# MAGIC
# MAGIC **📌  Important**: As for this model, the target column is string (*Yes/No*), we need to change `result_type` to `string` in **Load model and run inference** section. The final code should be `predict = mlflow.pyfunc.spark_udf(spark, model_uri, result_type="string")`

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Classroom Clean-up
# MAGIC
# MAGIC After completing the demo, clean up any resources created.
# MAGIC
# MAGIC - Delete saved models from model registry.
# MAGIC
# MAGIC - Delete AutoML experiment from Experiments page.
# MAGIC
# MAGIC Run the following cell to remove lessons-specific assets created during this lesson.

# COMMAND ----------

DA.cleanup()

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Conclusion
# MAGIC
# MAGIC In this demo, we explored the powerful capabilities of AutoML in Databricks. We learned how to create an AutoML experiment, evaluate the results, register the best model, transition it to the "Staging" stage, and prepare it for deployment. AutoML streamlines the process of building and selecting the best machine learning models, saving valuable time and effort in the model development process.

# COMMAND ----------

# MAGIC %md
# MAGIC 
&copy; 2024 Databricks, Inc. All rights reserved.<br/>
Apache, Apache Spark, Spark and the Spark logo are trademarks of the 
<a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
<br/><a href="https://databricks.com/privacy-policy">Privacy Policy</a> | 
<a href="https://databricks.com/terms-of-use">Terms of Use</a> | 
<a href="https://help.databricks.com/">Support</a>