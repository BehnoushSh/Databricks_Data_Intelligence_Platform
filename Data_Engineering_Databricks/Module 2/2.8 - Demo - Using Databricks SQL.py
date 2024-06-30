# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # Demo: Databricks SQL
# MAGIC
# MAGIC
# MAGIC **Learning Objectives**
# MAGIC 1. Describe Databricks SQL as a data warehousing solution for analysts and engineers working with Databricks.
# MAGIC 1. Recognize common use cases for data engineers when working with Databricks SQL.
# MAGIC 1. Open the SQL Editor.
# MAGIC 1. Write and run a Query.
# MAGIC 1. Describe the visualization and dashboarding capabilities of Databricks SQL.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### Getting Catalog Name
# MAGIC In the lesson, 2.3 - Demo - Data Management, we created two tables in the catalog that was created by our classroom setup. If you haven't run the notebook in that lesson, please do so now.  
# MAGIC   
# MAGIC Copy the catalog name from that lesson now. We will use it next.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC ### Databricks SQL
# MAGIC
# MAGIC 1. Right-click on **SQL Editor** in the left sidebar and open the link in a new tab.
# MAGIC 1. Recall that we created a SQL Warehouse in a previous lesson. It's also possible that one has been created for you
# MAGIC 1. Select a SQL Warehouse from the dropdown list to the left of the **Save** button in the SQL Editor
# MAGIC 1. Drop open the catalog name (immediately to the right of the **Run** button) and select your catalog
# MAGIC 1. Drop open the schema name to the right of the catalog name and select **getting_started**
# MAGIC 1. Paste the following query into the SQL Editor  
# MAGIC `SELECT * FROM customers_silver_merged`
# MAGIC 1. Run the query you just pasted in the SQL Editor by clicking the **Run** button
# MAGIC

# COMMAND ----------

# MAGIC %run "../Includes/Classroom-Setup-01"

# COMMAND ----------

print(f"SELECT * FROM {DA.catalog_name}.getting_started.customers_silver_merged")

# COMMAND ----------

# MAGIC %md
# MAGIC ### Create a Visualization
# MAGIC 1. After the query finishes, click the **+** button to the right of the **Results** tab and select **Visualization**
# MAGIC 1. Give the visualization a name by clicking the current name, Map (Markers) 1, in the upper-left corner and typing a new name.
# MAGIC 1. Drop open the **Visualization type** dropdown, and note the number of different visualizations available to you. 
# MAGIC 1. Choose **Map (Markers)**. The lat and lon columns will automatically be selected.
# MAGIC 1. Note that all customers are located in the United States, except one. Click the marker for this customer.  
# MAGIC   
# MAGIC As shown in the popup, the customer's address is in the state of Colorado. Clearly, there is something wrong with the lat and/or lon in this customer's data. 
# MAGIC   
# MAGIC 1. Click **Save** in the lower-right corner.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Create a Dashboard
# MAGIC 1. We can create a quick dashboard from this visualization by clicking the small down arrow next to the visualization's name and selecting **Add to dashboard**.
# MAGIC 1. Click the text **Create new dashboard** and give the dashboard a name.
# MAGIC 1. Click **Save and add**.
# MAGIC 1. View the dashboard by clicking **Dashboards** in the left sidebar menu and clicking the name of the dashboard you just created.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Conclusion
# MAGIC In this lesson, we worked in Databricks SQL to create a visualization from our data. We found one problem with the data that we would have struggled to find any other way.  
# MAGIC   
# MAGIC The next lesson is a lab where you will test your knowledge, hands-on.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ### Clean up Classroom
# MAGIC
# MAGIC Run the following two cells to remove lessons-specific assets created during this lesson.

# COMMAND ----------

DA.cleanup()

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2023 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>