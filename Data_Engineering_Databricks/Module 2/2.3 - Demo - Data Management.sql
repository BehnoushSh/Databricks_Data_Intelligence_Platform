-- Databricks notebook source
-- MAGIC %md-sandbox
-- MAGIC
-- MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
-- MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
-- MAGIC </div>

-- COMMAND ----------

-- MAGIC %md
-- MAGIC
-- MAGIC # Demo: Data Management
-- MAGIC Delta Lake tables provide ACID compliant updates to tables backed by data files in cloud object storage.
-- MAGIC
-- MAGIC In this notebook, we'll explore SQL syntax to process updates with Delta Lake. While many operations are standard SQL, slight variations exist to accommodate Spark and Delta Lake execution.
-- MAGIC
-- MAGIC **Learning Objectives**
-- MAGIC 1. Create a new schema in an existing catalog.
-- MAGIC 1. Create a new managed Delta table from an existing cloud file using SQL.
-- MAGIC 1. Create a new managed Delta table from an existing Delta table using SQL.
-- MAGIC 1. Drop a managed Delta table that is no longer needed.
-- MAGIC

-- COMMAND ----------

-- MAGIC %md
-- MAGIC
-- MAGIC ## Classroom Setup
-- MAGIC Run the following cell to setup our lesson.

-- COMMAND ----------

-- MAGIC %run ../Includes/Classroom-Setup-05

-- COMMAND ----------

-- MAGIC %md
-- MAGIC
-- MAGIC ### Overview of This Lesson
-- MAGIC We are going to take the data file that was copied into our workspace by the Classroom Setup script and create a table from it. Normally, this would be done by connecting to external cloud storage (i.e., Azure, AWS, GCP), but we would need to configure credentials for this, and credential creation is beyond the scop of this course.  
-- MAGIC   
-- MAGIC Once we have our table, we will copy the data into a second table and clean the data in this second table. In this way, we will always have our original, untouched data we can refer back to as needed.  
-- MAGIC   
-- MAGIC Finally, you will see how to drop a table.

-- COMMAND ----------

-- MAGIC %md
-- MAGIC
-- MAGIC ### Create a New Schema
-- MAGIC The classroom script created a new catalog that we can use during this lesson. All statements we run will use this catalog (unless it gets changed).  
-- MAGIC   
-- MAGIC Run the following cell to create a new schema within this catalog. Note that the command first drops the schema if it already exists. This is just so the command can be run multiple times without causing an error during the lesson.

-- COMMAND ----------

CREATE SCHEMA IF NOT EXISTS getting_started;
USE SCHEMA getting_started;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## Managed Tables
-- MAGIC
-- MAGIC We will create a **managed** table. A managed table copies the data from our data file into the default location of this workspace's metastore. This location, along with the metastore itself, is configured already, and we will not discuss this in this course. What's important for us to know is that data is copied from our data file, as opposed to the data file itself being the underlying data source for our table. Managed tables are the default table type, which can be overridden if we specify `LOCATION` in the `CREATE` statement.
-- MAGIC
-- MAGIC We will create the table in the schema (database) we created above.
-- MAGIC

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## Overview of customers.csv
-- MAGIC
-- MAGIC `customers.csv` has the following schema:
-- MAGIC
-- MAGIC | field | type | 
-- MAGIC |---|---|
-- MAGIC | customer_id | int |
-- MAGIC | tax_id | double | 
-- MAGIC | tax_code | string 
-- MAGIC | customer_name |string |
-- MAGIC | state | string |
-- MAGIC | city | string |
-- MAGIC | postcode | string
-- MAGIC | street | string
-- MAGIC | number | string
-- MAGIC | unit | string | 
-- MAGIC | region | string | 
-- MAGIC | district | string |
-- MAGIC | lon | double | 
-- MAGIC | lat | double |
-- MAGIC | ship_to_address | string | 
-- MAGIC | valid_from | int | 
-- MAGIC | valid_to | double | 
-- MAGIC | units_purchased | double | 
-- MAGIC | loyalty_segment | int | 
-- MAGIC
-- MAGIC We will use `COPY INTO` to copy the data from all `csv` files in our data directory. `COPY INTO` is idempotent, meaning it will only copy the data from a file once. We can also set the options to infer the schema and use the header as our column names. 

-- COMMAND ----------

CREATE TABLE IF NOT EXISTS customers_bronze;
COPY INTO customers_bronze
  FROM 'dbfs:/mnt/dbacademy-datasets/get-started-with-data-engineering-on-databricks/v01/'
  FILEFORMAT = CSV
  FORMAT_OPTIONS ('inferSchema' = 'true', 'header' = 'true')
  COPY_OPTIONS ('mergeSchema' = 'true')

-- COMMAND ----------

-- MAGIC %md
-- MAGIC Note: If you run the command above again, it will have 0 affected rows because `COPY INTO` will only copy the data from a file once.  
-- MAGIC   
-- MAGIC Let's view the data in our new table.

-- COMMAND ----------

SELECT * FROM customers_bronze;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## Clone our Bronze Table
-- MAGIC Let's create a deep clone of our `customers_bronze` table. A deep clone will create an independent copy of our table that we can use to clean the data.

-- COMMAND ----------

CREATE TABLE IF NOT EXISTS customers_silver
   DEEP CLONE customers_bronze;

SELECT * FROM customers_silver;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### A Problem
-- MAGIC There's a problem with creating our deep clone. We want to be able to reuse this notebook. By creating the deep clone, we replace all the data in the `customers_silver` table. We don't want to do that. We just want to add new customers (i.e., those with a new `customer_id`). Let's use `MERGE INTO` to accomplish this.  
-- MAGIC   
-- MAGIC `MERGE INTO` allows us to insert based on a specific condition.

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### Dropping Tables
-- MAGIC Let's drop the `customers_silver` table.

-- COMMAND ----------

DROP TABLE customers_silver;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### `MERGE INTO`
-- MAGIC Now, let's create a new table and use `MERGE INTO` to bring new data into our table. The table will only be created if it does not already exist.

-- COMMAND ----------

CREATE TABLE IF NOT EXISTS customers_silver_merged 
  (customer_id int,
  tax_id double,
  tax_code string,
  customer_name string,
  state string,
  city string,
  postcode string,
  street string,
  number string,
  unit string,
  region string,
  district string,
  lon double,
  lat double,
  ship_to_address string,
  valid_from int,
  valid_to double,
  units_purchased double,
  loyalty_segment int);
MERGE INTO customers_silver_merged
  USING customers_bronze
  ON customers_bronze.customer_id = customers_silver_merged.customer_id
  WHEN NOT MATCHED THEN INSERT *;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC
-- MAGIC ### Conclusion
-- MAGIC We now have a notebook that ingests new data from a directory without re-ingesting data that has already been processed, and we have created a table that contains the same data that we can use to clean and process for further consumption.  

-- COMMAND ----------

-- MAGIC %md
-- MAGIC
-- MAGIC ## No Clean up Classroom Script
-- MAGIC
-- MAGIC We are going to use the tables we created in this lesson in the next lesson, so we will not be running a cleanup script.

-- COMMAND ----------

-- MAGIC %md-sandbox
-- MAGIC &copy; 2023 Databricks, Inc. All rights reserved.<br/>
-- MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
-- MAGIC <br/>
-- MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>