# Databricks notebook source
# MAGIC %md
# MAGIC 
<div style="text-align: center; line-height: 0; padding-top: 9px;">
  <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning">
</div>


# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # Data Storage and Management
# MAGIC
# MAGIC In this demo, we will delve into the topic of data storage and management using the Delta Lake feature in Databricks. Delta Lake is a powerful storage layer that brings ACID transactions and data quality to big data workloads. We will cover creating, managing, and optimizing Delta tables to ensure efficient data storage and retrieval.
# MAGIC
# MAGIC **Learning Objectives:**
# MAGIC - Recognize that all tables created in Databricks are Delta tables by default.
# MAGIC - Create a new schema in an existing catalog.
# MAGIC - Create a new managed Delta table from an existing cloud file using SQL.
# MAGIC - Create a new managed Delta table from an existing Delta table using SQL.
# MAGIC - Drop a managed Delta table that is no longer needed.
# MAGIC - Understand that Delta Lake incorporates built-in optimizations to enhance performance.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Requirements
# MAGIC
# MAGIC Please review the following requirements before starting the lesson:
# MAGIC
# MAGIC * To run this notebook, you need to use one of the following Databricks runtime(s): **any**
# MAGIC * You need a Unity Catalog enabled workspace.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Classroom Setup
# MAGIC
# MAGIC Before starting the demo, run the provided classroom setup script. This script will define configuration variables necessary for the demo. Execute the following cell:

# COMMAND ----------

# MAGIC %run ../Includes/Classroom-Setup-01

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Other Conventions:**
# MAGIC
# MAGIC Throughout this demo, we will use the object `DA`, which provides important variables for the curriculum. Run the code block below to view these details:

# COMMAND ----------

print(f"Username:          {DA.username}")
print(f"Catalog Name:      {DA.catalog_name}")
print(f"Schema Name:       {DA.schema_name}")
print(f"Working Directory: {DA.paths.working_dir}")
print(f"Dataset Location:  {DA.paths.datasets}")

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Catalog and Schema
# MAGIC
# MAGIC Unity Catalog offers a 3-level namespace: organization, catalog, and schema. Here's how you can interact with it:

# COMMAND ----------

# MAGIC %md
# MAGIC **Create a Table in a Catalog:**

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE SCHEMA IF NOT EXISTS `${DA.catalog_name}`.`demo_table`;

# COMMAND ----------

# MAGIC %md
# MAGIC **List Schemas in the Catalog:**
# MAGIC
# MAGIC - Use the following code to list schemas in the catalog:

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW SCHEMAS FROM `${DA.catalog_name}`;

# COMMAND ----------

# MAGIC %md
# MAGIC **Delete a schema:**

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP SCHEMA IF EXISTS `${DA.catalog_name}`.`demo_table`;

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Ingest Data
# MAGIC
# MAGIC To demonstrate data ingestion, let's read two `csv` files. These files contains customer demographics and subscription details.
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM csv.`${DA.paths.datasets}/telco/customer-demographics.csv`

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

# MAGIC %md
# MAGIC
# MAGIC ## Silver Table
# MAGIC
# MAGIC * Create new table named **`customer_silver_merged`**
# MAGIC
# MAGIC * Join **`customer_details`** and **`customer_demographics`** tables
# MAGIC
# MAGIC * Save the resulting data in the **`customer_silver_merged`** table

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Create the customer_silver_merged table and save data by joining customer_details, customer_demographics table
# MAGIC
# MAGIC CREATE OR REPLACE TABLE customer_silver_merged AS
# MAGIC SELECT cd.customerID AS customerdetailsID,
# MAGIC     cdm.customerID AS customerdemographicsID,
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

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM customer_silver_merged;

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Manage Permissions with UC
# MAGIC
# MAGIC <!--explian permission management with UC. Mention that permissions can be managed from the Data Explorer UI or using SQL commands.-->
# MAGIC
# MAGIC Managing permission is essential for controlling who can access and perform actions on your data and resources. Unity catalog allows to manage permissions using the the Data Explorer UI or using SQL commands.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Granting Table Permissions to Users
# MAGIC
# MAGIC * Navigate to the data icon in the left sidebar actions
# MAGIC
# MAGIC * Open the catalog name in the list of data assets
# MAGIC
# MAGIC * Click on **( ⋮ )** kebab icon on the table name to which you want to give read permission
# MAGIC
# MAGIC * Select **Open in the Data Explorer** option
# MAGIC   
# MAGIC * Click **Permissions**. We can grant and revoke permissions on this table using this tab.  
# MAGIC   
# MAGIC * Click the **Grant** button.  
# MAGIC   
# MAGIC * Click on the dropdown inside principles.  
# MAGIC   
# MAGIC * Choose **`Account Users`** from the dropdown
# MAGIC
# MAGIC * Click **SELECT** in the privileges section and click on **Grant** button 
# MAGIC   
# MAGIC * You can grant **ALL PRIVILEGES**, **MODIFY**, or **SELECT** privileges. Tick the box next to **SELECT**. This allows this user read-only access to this table.  
# MAGIC   
# MAGIC * Click **Grant**. The new privilege is added to the list.

# COMMAND ----------

# MAGIC %sql
# MAGIC GRANT SELECT, MODIFY ON TABLE customer_silver_merged TO `account users`;

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW GRANTS ON TABLE customer_silver_merged;

# COMMAND ----------

# MAGIC %sql
# MAGIC REVOKE MODIFY ON TABLE customer_silver_merged FROM `account users`;

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Clean up Classroom
# MAGIC
# MAGIC After completing the demo, clean up any resources created.
# MAGIC
# MAGIC Run the following cell to remove lessons-specific assets created during this lesson.

# COMMAND ----------

DA.cleanup()

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Conclusion
# MAGIC
# MAGIC In this demo, we explored the concepts of data storage and management using Delta Lake in Databricks. We learned how to create and manage Delta tables, perform data transformation, optimize performance, and ensure a clean environment by dropping unnecessary tables. Delta Lake's built-in optimizations enhance performance and provide a robust solution for managing data storage and retrieval within Databricks.

# COMMAND ----------

# MAGIC %md
# MAGIC 
&copy; 2024 Databricks, Inc. All rights reserved.<br/>
Apache, Apache Spark, Spark and the Spark logo are trademarks of the 
<a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
<br/><a href="https://databricks.com/privacy-policy">Privacy Policy</a> | 
<a href="https://databricks.com/terms-of-use">Terms of Use</a> | 
<a href="https://help.databricks.com/">Support</a>