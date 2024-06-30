# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # Demo: Data Governance and Security
# MAGIC
# MAGIC **Learning Objectives**
# MAGIC 1. Grant another user the appropriate access to SELECT a table.
# MAGIC 1. Grant a group the appropriate access to SELECT a table.
# MAGIC 1. Revoke another user’s access to a table.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Getting Catalog Name
# MAGIC In the last lesson, we created two tables in the catalog that was created by our classroom setup. If you haven't run the notebook in the last lesson, please do so now.  
# MAGIC   
# MAGIC Copy the catalog name from the last lesson now. We will use it in the next cell.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Granting Permissions on Tables
# MAGIC Now that we have created a bronze table, which contains the raw data we ingested from the data file(s), and we have our silver table, which we can use to clean the data and make it ready for use, let's share the silver table with other users on our team in Databricks. We do this using the Data Explorer.  

# COMMAND ----------

# MAGIC %md
# MAGIC ### The Data Explorer
# MAGIC To view the Data Explorer, right-click on **Data** in the left sidebar menu, and open the link in a new tab.  
# MAGIC   
# MAGIC Drill open the catalog name in the list of data assets on the left side of the Data Explorer. The name of your catalog is listed in the output of the previous cell. If you do not see the name of your catalog in the Data Explorer, run the previous lesson's notebook in its entirety, and start this lesson over.  
# MAGIC   
# MAGIC Your catalog contains the schema we created in the previous lesson, `getting_started` and a `default` schema and `information_schema`. The `default` schema is simply an empty schema that is created when the catalog was created. We will not be discussing the `information_schema` in this course.  
# MAGIC   
# MAGIC Click the schema `getting_started`. We see the two tables we created, `customers_bronze` and `customers_silver_merged`. Note the other metadata and tabs as well.  

# COMMAND ----------

# MAGIC %md
# MAGIC ### Granting Table Permissions to Users
# MAGIC Click the table `customers_silver_merged`. We see the column information for this table. Note we can also view sammple data, details, permissions, history, lineage, and insights.  
# MAGIC   
# MAGIC Click **Permissions**. We can grant and revoke permissions on this table using this tab.  
# MAGIC   
# MAGIC Click the **Grant** button.  
# MAGIC   
# MAGIC Click inside the **Users and groups** dropdown to open the list. Note that you can grant permissions to individual users, groups, and service principles.  
# MAGIC   
# MAGIC Choose a user from the list and close the dropdown list using the `ESC` key on your keyboard.  
# MAGIC   
# MAGIC You can grant **ALL PRIVILEGES**, **MODIFY**, or **SELECT** privileges. Tick the box next to **SELECT**. This allows this user read-only access to this table.  
# MAGIC   
# MAGIC Click **Grant**. The new privilege is added to the list.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Granting Table Permissions to Groups
# MAGIC Databricks recommends you use groups to organize permissions and privileges. Using groups, you can subdivide your users based on their roles, and grant privileges to the group. In this way, you can remove a user from a group, and all privileges associated with that group are revoked. To grant privileges to a group:  
# MAGIC   
# MAGIC Click the **Grant** button.  
# MAGIC   
# MAGIC Click inside the **Users and groups** dropdown to open the list. Choose a group from the list. There may not be very many groups in your workspace, but there will always be either an **Account Users** or a **Users** group. Choose one of these groups and close the dropdown list using the `ESC` key on your keyboard.  
# MAGIC   
# MAGIC You can grant **ALL PRIVILEGES**, **MODIFY**, or **SELECT** privileges. Tick the box next to **SELECT**. This allows this group read-only access to this table.  
# MAGIC   
# MAGIC Click **Grant**. The new privilege is added to the list.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Revoking Table Permissions
# MAGIC Since we have granted read-only privileges to all users, we can revoke the individual privileges granted to our one user.  
# MAGIC   
# MAGIC Run your mouse over the name of the user to whom you granted privileges on this table and tick the box to the left of the username.  
# MAGIC   
# MAGIC Click the **Revoke** button.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Clean up Classroom
# MAGIC
# MAGIC We will continue to use our tables from the previous lesson, so we do not need to run a clean up script.

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2023 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>