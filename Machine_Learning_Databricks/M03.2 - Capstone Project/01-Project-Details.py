# Databricks notebook source
# MAGIC %md
# MAGIC 
<div style="text-align: center; line-height: 0; padding-top: 9px;">
  <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning">
</div>


# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # Capstone Project - Enhancing Paperless Billing at Telcom Inc.
# MAGIC
# MAGIC **Project Overview:** Telcom Inc., an internet service provider, is embarking on a crucial project aimed at increasing the adoption of paperless billing among its customers. This initiative holds significant importance for the company, both in terms of environmental sustainability and cost reduction.
# MAGIC
# MAGIC **Platform:** Telcom Inc. has chosen Databricks as its Lakehouse platform. The data engineering team manages aggregated customer data in comma-separated plain text files. As a data scientist, your mission is to ingest this data into Databricks and develop a machine learning model capable of predicting whether a user is likely to opt for paperless billing or not. This predictive model will be a valuable tool for various stakeholders within the company, enabling them to take actions that encourage more customers to embrace paperless billing.
# MAGIC
# MAGIC **Databricks Features to Use:** 
# MAGIC * **Delta Lake**: Data storage
# MAGIC * **Unity Catalog**: Data governance
# MAGIC * **Feature Store**: Store features in tables
# MAGIC * **AutoML**: Building a baseline model with no-code 
# MAGIC * **MLFlow**: Tracking and managing ML models
# MAGIC * **Model Serving**: Server ML models via REST API
# MAGIC * **Workflows**: Orchestrate data ingestion and model training workflows   
# MAGIC
# MAGIC ## Dataset
# MAGIC
# MAGIC The dataset provided by the data engineering team comprises customer demographics and subscription details. Below, you'll find a setup script that downloads both files in CSV format and provides the file paths.
# MAGIC
# MAGIC ## Project Tasks
# MAGIC
# MAGIC This section outlines the tasks you need to follow for this project.
# MAGIC
# MAGIC #### Task 1: Ingest Data and Pre-processing
# MAGIC The initial step involves data ingestion and pre-processing. Ingest data from CSV files and save them to Delta tables. Subsequently, create a "silver" table by consolidating all customer data into a single table. Ensure data cleanliness by performing necessary transformations while saving data to the silver table.
# MAGIC
# MAGIC #### Task 2: Feature Engineering
# MAGIC Feature engineering is a crucial phase in machine learning. Here, you must decide which features to extract from the customer table. The next step involves saving these features to a Feature Store table. For an efficiency boost, consider automating the feature extraction process with Databricks Workflows. Configure a workflow task to run regularly and refresh the features with new data.
# MAGIC
# MAGIC **🚀 Stand-out**: Take it a step further by automating the feature extraction process with Databricks Workflows. Configure a workflow task to run daily, ensuring that features are continuously updated with fresh data.
# MAGIC
# MAGIC **🚀 Stand-out**: Feature Store now supports creating feature table from existing tables. You can try this method after ingesting and merging data. 
# MAGIC
# MAGIC #### Task 3: Baseline Model
# MAGIC In this stage, you'll create a baseline model using AutoML. This allows you to quickly gain insights into feature performance and evaluate how effectively these features predict a customer's billing preference (paperless or not). AutoML also empowers you to compare results from different libraries and machine learning algorithms, helping you choose the most suitable one.
# MAGIC
# MAGIC #### Task 4: Train and Track A Model
# MAGIC Here, your focus shifts to training and tracking a model with MLflow. Before that, make informed decisions regarding which features to include in the model and which machine learning framework to utilize. Experiment with various options to arrive at the best possible model.
# MAGIC
# MAGIC #### Task 5: Register the Model
# MAGIC Once you've trained the final model, it's time to register it in the Model Registry. Additionally, ensure that you transition the model to an appropriate stage, such as "Staging."
# MAGIC
# MAGIC #### 🚀 Stand-out: Automate with Workflows
# MAGIC Consider automating both the model training and model registration processes with Databricks Workflows. If you completed the optional step in Task 2, you can establish task dependencies for the automation process.
# MAGIC
# MAGIC #### Task 6: Serve the Model
# MAGIC
# MAGIC After registering the model, you need to make it accessible to the entire organization via a REST endpoint. Stakeholders can conveniently consume this endpoint without requiring intricate knowledge of the model's details. Employ Databricks model serving to deploy the model and implement auto-scaling to reduce costs during idle periods.
# MAGIC
# MAGIC #### 🚀 Stand-out: Model A/B Testing
# MAGIC
# MAGIC Building effective and performant machine learning models is an ongoing endeavor. As new data becomes available, you may need to update your model to improve its performance. In this step, create another model, preferably one with better evaluation metrics, and serve it. However, rather than immediately replacing the production model, begin with testing. Serve the new model through the same endpoint and distribute incoming traffic at an 80/20 ratio for testing purposes.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ## Project Setup
# MAGIC
# MAGIC Run the code below to download dataset that you will be using for this project.
# MAGIC
# MAGIC For this project, you are expected to use this notebook to build the solution. If you want to use another notebook, please make sure to import the setup script as shown in next cell.

# COMMAND ----------

# MAGIC %run ../Includes/Classroom-Setup-Project

# COMMAND ----------

# MAGIC %md
# MAGIC 
&copy; 2024 Databricks, Inc. All rights reserved.<br/>
Apache, Apache Spark, Spark and the Spark logo are trademarks of the 
<a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
<br/><a href="https://databricks.com/privacy-policy">Privacy Policy</a> | 
<a href="https://databricks.com/terms-of-use">Terms of Use</a> | 
<a href="https://help.databricks.com/">Support</a>