# Databricks notebook source
# MAGIC %md
# MAGIC 
<div style="text-align: center; line-height: 0; padding-top: 9px;">
  <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning">
</div>


# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # 1.LAB -  Get started with Databricks DI Platform
# MAGIC The goal of this lab task is to familiarize yourself with the Databricks Data Intelligence Platform's workspace and learn how to manage repositories efficiently.
# MAGIC
# MAGIC **Lab Ouline:**
# MAGIC
# MAGIC + Task 1: Create a ML specific Cluster
# MAGIC + Task 2: Perform Repos and Git Integration
# MAGIC + Task 3: Manage Data Storage and control Permissions with Unity Catalog using SQL command

# COMMAND ----------

# MAGIC %md
# MAGIC ##Task 1: Create a Cluster 
# MAGIC **Step 1: Launch a New Cluster with ML Runtime**
# MAGIC 1. Navigate to Compute in the left sidebar.
# MAGIC 1. Click the `Create Compute` button.
# MAGIC 1. Provide a suitable name for the cluster, such as "ML-Lab-Cluster"
# MAGIC 1. Choose the Machine Learning runtime version.
# MAGIC 1. Select a cluster mode based on your needs.
# MAGIC 1. Configure the cluster size according to your requirements.
# MAGIC 1. Click Create compute to create the cluster.
# MAGIC
# MAGIC **Step 2: Attach the ML Runtime-Enabled Cluster**
# MAGIC 1. Navigate back to this notebook, click on `🔵 Connect`
# MAGIC 1. Select the `ML-Lab-Cluster` cluster from the dropdown.
# MAGIC 1. Click Confirm to attach the notebook to the cluster.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC #### Requirements
# MAGIC
# MAGIC Please review the following requirements before starting the next task steps:
# MAGIC
# MAGIC * To run this notebook, you need to use one of the following Databricks runtime(s): **any**

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC #### Notebook Setup
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

# COMMAND ----------

print(f"Username:          {DA.username}")
print(f"Catalog Name:      {DA.catalog_name}")
print(f"Schema Name:       {DA.schema_name}")
print(f"Working Directory: {DA.paths.working_dir}")
print(f"Dataset Location:  {DA.paths.datasets}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Task 2: Repos and Git Integration
# MAGIC Integrate repositories and Git seamlessly within the Databricks Data Intelligence Platform for streamlined collaboration and version control for machine learning projects.
# MAGIC
# MAGIC
# MAGIC **Step 1: Add a New Git Repository**
# MAGIC
# MAGIC + Click on the `+ New` icon in the left navigation bar.
# MAGIC + Navigate to the `Repos` option.
# MAGIC + Provide the Git repository URL when prompted and click `Create`.
# MAGIC
# MAGIC **Step 2: Describe Git Integration Processes**
# MAGIC
# MAGIC **a. Update README.md:**
# MAGIC
# MAGIC + Inside the cloned repository folder, locate the `README.md` file.
# MAGIC + Open the `README.md` file in a text editor or Databricks notebook.
# MAGIC + Make the desired changes or updates to the content of the `README.md` file.
# MAGIC + Save the changes.
# MAGIC
# MAGIC **b. Pulling Changes:**
# MAGIC
# MAGIC + Inside the cloned repo folder, right-click on the folder name.
# MAGIC + Select `Git...` from the dropdown menu.
# MAGIC + Click on the `Pull` button at the top-right corner to update the repo with the latest changes.
# MAGIC
# MAGIC **c. Pushing Changes:**
# MAGIC
# MAGIC + Inside the cloned repo folder, click on the Git button.
# MAGIC + Select the branch in which you want to push the changes.
# MAGIC + Choose `Push` to send your local changes to the remote repository.
# MAGIC
# MAGIC **d. Committing Changes:**
# MAGIC
# MAGIC + Inside the cloned repository folder, click the Git button.
# MAGIC + Select the branch where you want to make your changes.
# MAGIC + Enter a commit message describing your changes.
# MAGIC + Choose `Commit` to save your changes along with the commit message.
# MAGIC
# MAGIC
# MAGIC ***After completing the above steps, return to this notebook to proceed to the next task.***

# COMMAND ----------

# MAGIC %md
# MAGIC ## Task 3: Manage Data Storage and control Permissions with Unity Catalog using SQL command
# MAGIC Utilize SQL commands in Unity Catalog to efficiently manage data storage and control permissions, ensuring secure and accessible data for ML tasks.
# MAGIC
# MAGIC **Step 1:** Run the following cmd to Create a Table in a Catalog

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

# MAGIC %md
# MAGIC **Step 2: Create a bar chart visualization following the provided steps:**
# MAGIC
# MAGIC + Run the follwing SQL query to get the necessary data for the bar chart.
# MAGIC + Click the (+) icon at the top of your table in the cell output.
# MAGIC + Choose **`Visualization`** from the dropdown.
# MAGIC + Select **`Bar`** as your visualization type.
# MAGIC + Pick the bar chart column types and save your visualization.

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM customer_demographics;

# COMMAND ----------

# MAGIC %md
# MAGIC **Step 3: Grant Permissions**
# MAGIC
# MAGIC + Change language of the cell to SQL.
# MAGIC + Write the SQL command to grant MODIFY permissions on the customer_demographics table to the account users group

# COMMAND ----------

# MAGIC %sql
# MAGIC --Grant permission to Modify on customer_demographics table to `account users`
# MAGIC <FILL_IN>

# COMMAND ----------

# MAGIC %md
# MAGIC **Step 4: Verify Permission**
# MAGIC
# MAGIC + Write the SQL command to verify that the permissions were granted successfully

# COMMAND ----------

# MAGIC %sql
# MAGIC --Check for permissions on customer_demographics table
# MAGIC <FILL_IN>

# COMMAND ----------

# MAGIC %md
# MAGIC **Step 5: Revoke Permissions**
# MAGIC
# MAGIC + Write SQL command to revoke permissions on the customer_demographics table

# COMMAND ----------

# MAGIC %sql
# MAGIC --Revoke modify permission from `account users` on customer_demographics table
# MAGIC <FILL_IN>

# COMMAND ----------

# MAGIC %md
# MAGIC ##Clean up Classroom
# MAGIC After completing the demo, clean up any resources created.
# MAGIC
# MAGIC Run the following cell to remove lessons-specific assets created during this lesson.

# COMMAND ----------

DA.cleanup()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Conclusion
# MAGIC In this lab, we covered essential tasks to get started with the Databricks Data Intelligence Platform. From creating clusters and managing repositories to data storage and permission management, we explored key features of the platform. By following these steps, users can efficiently utilize Databricks for their Machine Learning and Data Science tasks

# COMMAND ----------

# MAGIC %md
# MAGIC 
&copy; 2024 Databricks, Inc. All rights reserved.<br/>
Apache, Apache Spark, Spark and the Spark logo are trademarks of the 
<a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
<br/><a href="https://databricks.com/privacy-policy">Privacy Policy</a> | 
<a href="https://databricks.com/terms-of-use">Terms of Use</a> | 
<a href="https://help.databricks.com/">Support</a>