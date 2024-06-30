# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # Demo: The Lakehouse Platform
# MAGIC
# MAGIC **Learning Objectives**
# MAGIC 1. Describe the navigational interface to the Databricks Lakehouse Platform, including the organization of services and capabilities on the left-side navigation bar and the availability of settings in the top-right corner.
# MAGIC 1. Navigate throughout the Workspace.
# MAGIC 1. Describe the Workspace as the solution for organizing assets within Databricks.
# MAGIC 1. Perform the actions available in the Workspace.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## The Landing Page
# MAGIC In the upper-left corner, right click on the Databricks logo and open the link in a new tab. This will allow you to keep this notebook open while navigating the Databricks workspace.
# MAGIC What you see is the Databricks landing page. On the page, you three sections: Get Started, Recents, and Popular. 
# MAGIC ### Get Started
# MAGIC In the Get Started section, there are quick links that will help you with some common tasks like importing data, creating a new notebook, and opening the SQL Editor.
# MAGIC ### Recents
# MAGIC This section provides a list of the most recently used items. It can include notebooks, queries, dashboards, and other items.
# MAGIC ### Popular
# MAGIC There are some items you will use more often than others. This section tracks the items that are accessed more often. This will help you quickly find your most commonly used items.

# COMMAND ----------

# MAGIC %md
# MAGIC ## The Sidebar Menu
# MAGIC On the left side of your workspace, you will find the sidebar menu. There are five sections in this menu, and three of the sections can be collapsed if you do not use them often. 
# MAGIC 1. Click the "Machine Learning" heading in the sidebar menu, and it will collapse. 
# MAGIC 1. Click again, and it will expand.
# MAGIC You can also collapse and expand the entire sidebar menu. At the bottom of the menu, you will find a menu item that provides this feature
# MAGIC 1. Click the last menu item in the sidebar menu to either expand or collapse the sidebar menu. Note: you will need to move your mouse off the sidebar menu to see it collapse.
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ## The Workspace Page
# MAGIC Click "Workspace" in the sidebar menu. The workspace is the way you organize your assets in Databricks. There are four sections: Home, Workspace, Repos, and Trash.
# MAGIC ### Home
# MAGIC The "Home" section is a shortcut to your user folder. This folder can also be found by clicking Workspace -> Users -> _your-username_. You can add sub-folders by clicking Add -> Folder, or you can create new assets like Queries, Alerts, Notebooks, MLFlow experiments, and others.
# MAGIC 1. Create a new notebook in your home folder
# MAGIC 1. Change the name of the notebook in the upper-left corner of the notebook. "Name it Getting Started."
# MAGIC 1. Go back to your home folder by clicking Workspace -> Home. The notebook appears in your Home folder.
# MAGIC Let's share the notebook with others.
# MAGIC 1. At the far right of the notebook name, click the kebab menu and select "Share (Permissions)." Note that the notebook is shared with you, and the Admins group, by default.
# MAGIC 1. Click in the input box, and select "All Users." On the right, you can select the privileges you are granting to this group. They can view, run, edit, or manage the notebook, depending on which option you choose. Note: whichever option you choose, the group will be granted all privileges below that option (i.e., if they can edit, they can also run and view).
# MAGIC 1. For the privilege type, select "Can View."
# MAGIC 1. Click "Add."
# MAGIC 1. Click the "X" to close the sharing dialog box.
# MAGIC Let's delete the notebook.
# MAGIC 1. Again, click the kebab menu to the far right of the notebook name. Note: there are many options in this menu (Open in new tab, Clone, Rename, etc). We are not going to discuss these in this course.
# MAGIC 1. Select "Move to Trash."
# MAGIC 1. Confirm that you wish to move the notebook to the trash by selecting "Confirm and move to Trash."
# MAGIC The notebook is moved to the trash. If you wish to undo this action or permantly delete the item, click "Trash" on the left side of the page.
# MAGIC 1. Click the kebab menu to the far right of the notebook name. There are two options: "Permanently delete" and "Restore."
# MAGIC 1. Select "Permanently delete" to delete the notebook.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Workspace
# MAGIC The Workspace section allows you to organize your assets outside of your home folder and outside of any repositories (discussed next). You can use this section to organize subfolders that are shared with specific users/groups, organize specific projects, or organize based on departments within your organization. 

# COMMAND ----------

# MAGIC %md 
# MAGIC ### Repos
# MAGIC Databricks Repos allow us to connect our notebooks to repositories, such as Github, to enable CI/CD workflows or to simply backup our work. A personal access token (PAT) is required when setting up a connection. Once the PAT is configured, it is very simple to add new repos. We are going to discuss this in the next lesson.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Trash
# MAGIC As mentioned above, assets that are moved to the trash appear in this section. Any item moved to the trash will be permentantly deleted after 30 days, unless you delete it earlier.

# COMMAND ----------

# MAGIC %md
# MAGIC ### "Kebab" and "Add" Menus
# MAGIC Before leaving this lesson, please note that the "kebab" and "Add" menus provide different functionality depending on the section you are in and the type of file involved. For example, the kebab menu for repos will have a "Git" option where you can commit, pull, and otherwise work with Git. Feel free to add new files and experiment with the kebab and Add menus to see how things change.

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2023 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>