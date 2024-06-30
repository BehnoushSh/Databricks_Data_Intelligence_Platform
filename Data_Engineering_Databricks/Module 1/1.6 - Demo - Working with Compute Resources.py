# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # Demo: Compute Resources
# MAGIC In order to work with data in Databricks, we need to use compute resources (i.e., clusters and warehouses). In this demo, we will launch a new cluster and a new warehouse.
# MAGIC
# MAGIC **Learning Objectives**
# MAGIC 1. Launch a new cluster.
# MAGIC 1. Launch a new warehouse.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ## Create a Cluster
# MAGIC
# MAGIC Depending on the workspace in which you're currently working, you may or may not have cluster creation privileges. 
# MAGIC
# MAGIC Instructions in this section assume that you **do** have cluster creation privileges, and that you need to deploy a new cluster to execute the lessons in this course.
# MAGIC
# MAGIC **NOTE**: Check with your instructor or a platform admin to confirm whether or not you should create a new cluster or connect to a cluster that has already been deployed. Cluster policies may impact your options for cluster configuration. 
# MAGIC
# MAGIC Steps:
# MAGIC 1. In the left sidebar, right-click on **Compute** and open the link in a new tab. This will allow you to refer back to these instructions, as needed
# MAGIC 1. Click the blue **Create Compute** button
# MAGIC 1. For the **Cluster name**, use your name so that you can find it easily
# MAGIC 1. Set the cluster to Single Node, to control costs for this testing cluster.
# MAGIC 1. Set the Access Mode to Single User (this mode is required for Unity Catalog)
# MAGIC 1. Use the recommended **Databricks runtime version** for this course
# MAGIC 1. Leave boxes checked for the default settings under the **Autoscaling Options**
# MAGIC 1. Note the configuration options available for clusters
# MAGIC 1. Click the blue **Create Compute** button
# MAGIC
# MAGIC **NOTE:** Clusters can take several minutes to deploy and startup. Once you have finished deploying a cluster, feel free to continue to explore the compute creation UI.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ### <img src="https://files.training.databricks.com/images/icon_warn_24.png"> Single User Cluster Required for This Course
# MAGIC **IMPORTANT:** This course requires you to run notebooks on a single user cluster. 
# MAGIC
# MAGIC Follow the instructions above to create a cluster that has **Access mode** set to **`Single User`**.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Create a SQL Warehouse
# MAGIC
# MAGIC Now that we have created a cluster, let's create a SQL Warehouse, so we can run queries in Databricks SQL.  
# MAGIC   
# MAGIC Steps:
# MAGIC 1. Click on the tab, **SQL Warehouses**, on the Compute page
# MAGIC 1. Click **Create SQL warehouse**
# MAGIC 1. For the **Name**, use your name so that you can find it easily
# MAGIC 1. Set the **Cluster size** to 2X-Small
# MAGIC 1. Verify the **Auto-stop** is set to 10 minutes
# MAGIC 1. Verify the **Scaling** is set to 1 for the **Min.** and 1 for the **Max.**
# MAGIC 1. Verify that **Type** is set to Serverless
# MAGIC 1. Note the **Advanced options**
# MAGIC 1. Click **Create**

# COMMAND ----------

# MAGIC %md
# MAGIC ### Conclusion
# MAGIC Now that we have created our compute resources, we can begin running notebooks and queries.

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2023 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>