# Databricks notebook source
# MAGIC %md
# MAGIC 
<div style="text-align: center; line-height: 0; padding-top: 9px;">
  <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning">
</div>


# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # Working with Notebooks
# MAGIC
# MAGIC In this demo, we will delve into the functionalities of working with notebooks on the Databricks platform. Notebooks serve as a powerful environment for interactive coding, data exploration, and documentation. You'll learn how to create, attach, and execute code using different languages, as well as utilize markdown for notes and basic visualization capabilities.
# MAGIC
# MAGIC **Learning Objectives:**
# MAGIC - Launch a new cluster with ML runtime.
# MAGIC - Understand the high-level configuration options for a cluster created for ML.
# MAGIC - Create a notebook and attach a compute resource to it.
# MAGIC - Write and execute code using multiple languages.
# MAGIC - Utilize markdown-based notes in a notebook.
# MAGIC - Explore basic visualization capabilities in Databricks notebooks.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Requirements
# MAGIC
# MAGIC Please review the following requirements before starting the lesson:
# MAGIC
# MAGIC * To run this notebook, you need to use one of the following Databricks runtime(s): **any**

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
# MAGIC **Other Conventions:**
# MAGIC
# MAGIC Throughout this demo, we'll refer to the object `DA`. This object, provided by Databricks Academy, contains variables such as your username, catalog name, schema name, working directory, and dataset locations. Run the code block below to view these details:

# COMMAND ----------

print(f"Username:          {DA.username}")
print(f"Catalog Name:      {DA.catalog_name}")
print(f"Schema Name:       {DA.schema_name}")
print(f"Working Directory: {DA.paths.working_dir}")
print(f"Dataset Location:  {DA.paths.datasets}")

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Create a Cluster
# MAGIC
# MAGIC Before working with notebooks, let's ensure we have a suitable compute environment. We will create a cluster with the necessary runtime configuration. Follow these steps:
# MAGIC
# MAGIC 1. Click on **Compute** in the left navigation bar.
# MAGIC
# MAGIC 2. Click the blue **Create Compute** button.
# MAGIC
# MAGIC 3. Provide a suitable name for the cluster, such as "ML-Demo-Cluster".
# MAGIC
# MAGIC 4. Choose the **Machine Learning** runtime version.
# MAGIC
# MAGIC 5. Select a cluster mode based on your needs.
# MAGIC
# MAGIC 6. Configure the cluster size as per your requirements.
# MAGIC
# MAGIC 7. Click **Create compute** to create the cluster.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Working with Notebooks
# MAGIC
# MAGIC Let's now explore the power of Databricks notebooks:
# MAGIC
# MAGIC * Attach a Notebook to a Cluster:
# MAGIC    - Click on **Workspace** in the left navigation bar.
# MAGIC    - Select the desired folder or create a new one.
# MAGIC    - Right-click and choose **Create > Notebook**.
# MAGIC    - Name your notebook and select the previously created cluster from the dropdown.
# MAGIC    - Click **Confirm**.
# MAGIC
# MAGIC * Creating a Cell
# MAGIC    - Navigate to the bottom of existing cell
# MAGIC    - Click on the **(+)** icon to add new cell    
# MAGIC
# MAGIC * Running a Cell:
# MAGIC    - Cells in a notebook can be executed using the **Run** button at the top-right corner of the cell or by pressing **Shift + Enter**.
# MAGIC    - Try running a cell with simple Python code to see the output.
# MAGIC
# MAGIC * Run all cells:
# MAGIC    - Click on the **Run all** button to run all cell at one's in notebook
# MAGIC
# MAGIC * Create Python, SQL cells:
# MAGIC    - Navigate to the language switcher cell at the top-right of cell
# MAGIC    - Select the desired language for your cell
# MAGIC    - Alternatively, type **%py** or **%sql** at the top of the cell
# MAGIC
# MAGIC ### Left sidebar actions
# MAGIC    - Click on the **Table of contents** icon between the left sidebar and the topmost cell to access notebook table content
# MAGIC    - Click on the folder icon to access **folder** structure of the workspace
# MAGIC    - Navigate to the **data** icon to get a list of metastore's
# MAGIC    - Navigate to **data assistant** (public preview) for getting code suggestions, diagnosing errors, etc.
# MAGIC
# MAGIC ### Right sidebar actions 
# MAGIC    - Click on the message icon to add **Comments** on existing code
# MAGIC    - Use the **MLflow experiments** icon to create a workspace experiment.
# MAGIC    - Access code versioning history through the **Revision history** icon.
# MAGIC    - Get a list of variables used in a notebook by navigating to **Variable explorer** icon
# MAGIC    - Discover Python libraries used in the notebook by navigating to the **Python libraries** icon.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ### Working with Python
# MAGIC
# MAGIC To run Python code, select default language as **"Python"** at the top of the notebook. To work with Python in non-Python notebooks, just add **`%py`** to the first line of the cell and write the code. 
# MAGIC
# MAGIC Let's check out next example.

# COMMAND ----------

print("This is a Python cell!!")

# COMMAND ----------

# you can install external libraries with pip
%pip install parsedatetime

# COMMAND ----------

#read data with Spark and display the result
df = spark.read.option("header", "true").csv(f"{DA.paths.datasets}/retail/customers.csv")
display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Working with SQL
# MAGIC
# MAGIC To run SQl code, select default language as **"SQL"** at the top of the notebook. To work with SQL in non-sql notebooks, just add **`%sql`** to the first line of the cell and write the code.
# MAGIC
# MAGIC Let's check out next example.

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT date_format(getdate(), 'd MMM') AS Today;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM csv.`${DA.paths.datasets}/retail/customers.csv`

# COMMAND ----------

# MAGIC %md
# MAGIC ### Working with Markdown
# MAGIC
# MAGIC Working with Markdown Cells:
# MAGIC - Markdown cells allow you to add formatted text and documentation to your notebook.
# MAGIC - Create a new cell, change its type to Markdown, and enter some text using Markdown syntax.
# MAGIC - Alternatively, type **%md** at the top of cell
# MAGIC
# MAGIC Editing a Mardown cell:
# MAGIC - Double click this cell to begin editing it
# MAGIC - Then hit **`Esc`** to stop editing
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC # Title One
# MAGIC ## Title Two
# MAGIC ### Title Three
# MAGIC
# MAGIC This is a test of the emergency broadcast system. This is only a test.
# MAGIC
# MAGIC This is text with a **bold** word in it.
# MAGIC
# MAGIC This is text with an *italicized* word in it.
# MAGIC
# MAGIC This is an ordered list
# MAGIC 1. one
# MAGIC 1. two
# MAGIC 1. three
# MAGIC
# MAGIC This is an unordered list
# MAGIC * apples
# MAGIC * peaches
# MAGIC * bananas
# MAGIC
# MAGIC Links/Embedded HTML: <a href="https://en.wikipedia.org/wiki/Markdown" target="_blank">Markdown - Wikipedia</a>
# MAGIC
# MAGIC Images:
# MAGIC ![Spark Engines](https://files.training.databricks.com/images/Apache-Spark-Logo_TM_200px.png)
# MAGIC
# MAGIC And of course, tables:
# MAGIC
# MAGIC | name   | value |
# MAGIC |--------|-------|
# MAGIC | Yi     | 1     |
# MAGIC | Ali    | 2     |
# MAGIC | Selina | 3     |
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Visualization with Notebooks
# MAGIC
# MAGIC Notebooks support creating interactive charts to visualize data. 
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **Create a Sample Customers Table:** The code below will create a sample customers table that we will use for this demo.

# COMMAND ----------

DA.create_customers_table()

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ### Create a Table Visualization:
# MAGIC
# MAGIC Run the cell below to view the result as a table. You can download the result or add the table to a dashboard.

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM `retail-customers`;

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ### Bar Chart Visualization:
# MAGIC
# MAGIC In addition to table view in cell output, we can create visualization from the output data. In this example, we will create a bar chart following these steps;
# MAGIC
# MAGIC - Run the cell.
# MAGIC - Click the **(+)** icon at top your table in the cell output.
# MAGIC - Choose **'Visualization'** from the dropdown.
# MAGIC - Select **'Bar'** as your visualization type.
# MAGIC - Pick the bar chart column type.
# MAGIC - Save your visualization.

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT 
# MAGIC   loyalty_segment, 
# MAGIC   count(*) AS total_customers  
# MAGIC FROM `retail-customers`
# MAGIC GROUP BY loyalty_segment
# MAGIC ORDER BY loyalty_segment

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Data Profiler Feature:
# MAGIC
# MAGIC For more advanced data exploration, use the Data Profiler feature.
# MAGIC To access it, click on a **(+)** icon in cell output, select **Data Profile**, and explore the generated insights.

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM `retail-customers`
# MAGIC WHERE city = 'VIENNA'

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
# MAGIC In this demo, we explored the essential aspects of working with notebooks on Databricks. You've learned how to create notebooks, attach them to clusters, write and execute code, leverage markdown cells for documentation, and perform basic data visualization. Notebooks are a versatile tool for data analysis, coding, and collaboration within the Databricks environment.

# COMMAND ----------

# MAGIC %md
# MAGIC 
&copy; 2024 Databricks, Inc. All rights reserved.<br/>
Apache, Apache Spark, Spark and the Spark logo are trademarks of the 
<a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
<br/><a href="https://databricks.com/privacy-policy">Privacy Policy</a> | 
<a href="https://databricks.com/terms-of-use">Terms of Use</a> | 
<a href="https://help.databricks.com/">Support</a>