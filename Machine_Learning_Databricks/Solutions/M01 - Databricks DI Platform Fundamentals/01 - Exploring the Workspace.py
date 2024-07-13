# Databricks notebook source
# MAGIC %md
# MAGIC 
<div style="text-align: center; line-height: 0; padding-top: 9px;">
  <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning">
</div>


# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # Exploring the Workspace
# MAGIC
# MAGIC In this demo, we will navigate through the Databricks DI Platform Workspace, understanding its layout and features. The Workspace acts as a central hub for organizing and accessing various assets, such as notebooks and files. By the end of this demo, you'll be familiar with navigating the Workspace efficiently and using its functionalities.
# MAGIC
# MAGIC **Learning Objectives:**
# MAGIC - Understand the Databricks Workspace interface.
# MAGIC - Learn how to navigate through different sections of the Workspace.
# MAGIC - Explore the organization of assets within the Workspace.
# MAGIC - Perform common actions available in the Workspace.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Requirements
# MAGIC
# MAGIC In this demo, we will be using Repos. If you want to follow the steps, you need to setup git integration for your account in **"User Settings"** page. Follow this <a href="https://docs.databricks.com/en/repos/repos-setup.html#set-up-databricks-repos" target="_blank">documentation page</a> to set git credentials from **User settings**.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Overview of the UI
# MAGIC
# MAGIC When you first land on the Databricks DI Platform, you'll be greeted by a landing page. The left-side navigation bar provides easy access to various services and capabilities, such as the Workspace, Data, Clusters, and more. In the top-right corner, you'll find settings, notifications, and other account-related options.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Workspace
# MAGIC
# MAGIC The Workspace is where you'll manage your assets and perform various tasks. Here's how to navigate and perform common actions within the Workspace:
# MAGIC
# MAGIC * **Create a Folder**:
# MAGIC    - Click on the **Workspace** button in the left navigation bar.
# MAGIC    - Select the folder where you want to create a new folder.
# MAGIC    - Right-click and choose **Create > Folder**.
# MAGIC    - Provide a name for the folder and click **Create**
# MAGIC    - Alternatively, click on **Add** button at the top-right corner
# MAGIC    - Select **folder** option name it and click on **Create** button 
# MAGIC
# MAGIC * **Import a File**:
# MAGIC    - Navigate to the desired folder.
# MAGIC    - Right-click and choose **Import**.
# MAGIC    - Select the file you want to import and click **Import**.
# MAGIC    - Alternatively, navigate to desired folder and click on **( ⋮ )** kebab icon at top-right corner
# MAGIC    - Select the import option from the dropdown
# MAGIC    - Select the file you want to import and click **Import**
# MAGIC
# MAGIC * **Export a File**:
# MAGIC    - Right-click on a file in the Workspace.
# MAGIC    - Choose **Export** and select the desired export format.
# MAGIC    - Alternatively, navigate to folder in which file is present
# MAGIC    - Click on the click on **( ⋮ )** kebab icon and select export
# MAGIC    - Select the desired file type
# MAGIC
# MAGIC * **Navigating Folders**:
# MAGIC    - Double-click on a folder to enter it.
# MAGIC    - Use the breadcrumb trail at the top to navigate back.
# MAGIC    - Alternatively, click on the workspace on left sidebar to move at top of folder structure
# MAGIC
# MAGIC * **Create a notebook**:
# MAGIC    - Navigate to the desired folder
# MAGIC    - Right-click and hover over create
# MAGIC    - Select the notebook option from the dropdown
# MAGIC    - Alternatively, click on the **Add** button inside the desired folder
# MAGIC    - Select **notebook** option to create new notebook
# MAGIC
# MAGIC * **Rename Folder**:
# MAGIC    - Navigate over your folder name
# MAGIC    - Right-click on a folder and select **Rename**
# MAGIC    - Enter the new name and select **Ok**
# MAGIC    - Alternatively, navigate to desired folder 
# MAGIC    - Click on kebab icon **( ⋮ )** on folder name want to rename
# MAGIC    - Rename the folder and click on **ok** button
# MAGIC  
# MAGIC * **Share Folder**:
# MAGIC    - Hover over the folder you want to share
# MAGIC    - Click on the kebab icon **( ⋮ )** at right corner
# MAGIC    - Click on the Share(permissions) option from the dropdown
# MAGIC    - Select the username from the search bar you want to share
# MAGIC    - Provide edit, view, manage, run permissions you want to give to user
# MAGIC    - Click on **Add** button

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Working with Repos
# MAGIC
# MAGIC The Databricks Workspace allows you to connect your projects with Git repositories. This enables you to collaborate on code, track changes, and easily sync your work between Databricks and Git. 
# MAGIC
# MAGIC Here's how to work with repos:
# MAGIC
# MAGIC **📌 Note:** Before working with Repos user should have git credentials for resources and operations at the Databricks workspace level. Follow this <a href="https://docs.databricks.com/en/repos/repos-setup.html#set-up-databricks-repos" target="_blank">documentation</a> to set git credentials from **User settings**.
# MAGIC
# MAGIC * **Add a Repo**:
# MAGIC    - Click on the **Workspace** button in the left navigation bar.
# MAGIC    - Click on Repos and navigate to your username
# MAGIC    - Right-click and choose **Create > Repo**.
# MAGIC    - Provide the Git repository <a href="https://github.com/databricks-academy/get-started-with-data-engineering-on-databricks-repo-example" target="_blank">URL</a> and click **Create**.
# MAGIC    - Alternatively, navigate to the **Repos** click on the Add button at top-right corner
# MAGIC    - Select **Repo** provide the Git repository <a href="https://github.com/databricks-academy/get-started-with-data-engineering-on-databricks-repo-example" target="_blank">URL</a> and click on **Create Repo**
# MAGIC
# MAGIC * **Pull Changes**:
# MAGIC    - Inside a cloned repo folder, right-click on the folder name
# MAGIC    - Select **Git** option from the dropdown
# MAGIC    - Click on the **Pull** button at the top-right corner to update the repo with the latest changes.
# MAGIC    
# MAGIC * **Push Changes**:
# MAGIC    - Inside a cloned repo folder, click on the **Git** button.
# MAGIC    - Select the **branch** in which you want to push the changes
# MAGIC    - Choose **Push** to send your local changes to the remote repository.
# MAGIC
# MAGIC * **Commit Changes**:
# MAGIC    - Inside the cloned repository folder, click the Git button.
# MAGIC    - Select the **branch** where you want to make your changes
# MAGIC    - Enter the commit message
# MAGIC    - Choose **Commit** to save your changes along with the commit message.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Finding Assets
# MAGIC
# MAGIC In the Workspace, you can quickly find assets using the search bar at the top. Type keywords related to the asset you're looking for, and the search will provide suggestions as you type:
# MAGIC
# MAGIC * **Finding assets through searchbox**:
# MAGIC    - Click on the search bar at the top-left
# MAGIC    - Enter the desired keyword.
# MAGIC    - Select the matching filename from the dropdown and press Enter.
# MAGIC    - For advanced search options, select "Open advanced search" while the search box is active. Advanced search allows you to filter results by asset type such as notebooks, dashboards, etc. 
# MAGIC
# MAGIC * **Find recent files/folders**:
# MAGIC    - Navigate to the sidebar
# MAGIC    - Click on **Recents**
# MAGIC    - Select the file you want to access

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Conclusion
# MAGIC
# MAGIC In this demo, we explored the Databricks DI Platform Workspace and its features. You've learned how to navigate the interface, manage folders, import and export files, and work with Git repositories. The Workspace provides a central location for organizing and accessing your assets, making your work more organized and efficient.

# COMMAND ----------

# MAGIC %md
# MAGIC 
&copy; 2024 Databricks, Inc. All rights reserved.<br/>
Apache, Apache Spark, Spark and the Spark logo are trademarks of the 
<a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
<br/><a href="https://databricks.com/privacy-policy">Privacy Policy</a> | 
<a href="https://databricks.com/terms-of-use">Terms of Use</a> | 
<a href="https://help.databricks.com/">Support</a>