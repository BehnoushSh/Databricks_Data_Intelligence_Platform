# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # Demo: Working with Notebooks
# MAGIC Notebooks are the primary means of developing and executing code interactively on Databricks. This lesson provides a basic introduction to working with Databricks notebooks.
# MAGIC
# MAGIC **Learning Objectives**
# MAGIC 1. Describe Databricks Notebooks as the most common interface for data engineers when working with Databricks.
# MAGIC 1. Recognize common use cases for data engineers when working with Notebooks.
# MAGIC 1. Create a new Notebook.
# MAGIC 1. Write code in Notebook cells.
# MAGIC 1. Run code in Notebook cells.
# MAGIC 1. Write markdown-based notes in a Notebook.
# MAGIC 1. Run code using multiple languages within the same Notebook. 
# MAGIC 1. Change the name of a Notebook.
# MAGIC 1. Explore basic visualization capabilities in Databricks Notebooks.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Attach to a Cluster
# MAGIC
# MAGIC In the previous lesson, you should have either deployed a cluster or identified a cluster that an admin has configured for you to use.
# MAGIC
# MAGIC At the top right corner of your screen, click the cluster selector ("Connect" button) and choose a cluster from the dropdown menu. When the notebook is connected to a cluster, this button shows the name of the cluster.
# MAGIC
# MAGIC **NOTE**: If your cluster is not running at the time you select it from the list, it will begin the startup process. Deploying a cluster can take several minutes. A solid green circle will appear to the left of the cluster name once resources have been deployed. 

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Notebooks Basics
# MAGIC
# MAGIC Notebooks provide cell-by-cell execution of code. Multiple languages can be mixed in a notebook. Users can add plots, images, and markdown text to enhance their code.
# MAGIC
# MAGIC Throughout this course, our notebooks are designed as learning instruments. Notebooks can be easily deployed as production code with Databricks, as well as providing a robust toolset for data exploration, reporting, and dashboarding.
# MAGIC
# MAGIC ### Running a Cell
# MAGIC * Run the cell below using one of the following options:
# MAGIC   * Place your cursor in the cell, and type **CTRL+ENTER** or **CTRL+RETURN**
# MAGIC   * Place your cursor in the cell, and type **SHIFT+ENTER** or **SHIFT+RETURN** to run the cell and move to the next one
# MAGIC   * Click on the right-pointing triangle image in the upper-right corner of the cell and using **Run Cell**, **Run All Above** or **Run All Below** as seen here<br/><img style="box-shadow: 5px 5px 5px 0px rgba(0,0,0,0.25); border: 1px solid rgba(0,0,0,0.25);" src="https://files.training.databricks.com/images/notebook-cell-run-cmd.png"/>  
# MAGIC     
# MAGIC ### Lesson Setup
# MAGIC Run the following cell. It will install a data file, called `customers.csv`, that we will use throughout this demo.

# COMMAND ----------

# MAGIC %run ../Includes/Classroom-Setup-05

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC **NOTE**: Cell-by-cell code execution means that cells can be executed multiple times or out of order. Unless explicitly instructed, you should always assume that the notebooks in this course are intended to be run one cell at a time from top to bottom. If you encounter an error, make sure you read the text before and after a cell to ensure that the error wasn't an intentional learning moment before you try to troubleshoot. Most errors can be resolved by either running earlier cells in a notebook that were missed or re-executing the entire notebook from the top.

# COMMAND ----------

# MAGIC %md
# MAGIC ### View customers.csv
# MAGIC Run the following cell to view the contents of `customers.csv`

# COMMAND ----------

display((spark.read
         .csv(f"{DA.paths.datasets}/customers.csv")
         ))

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ### Run a SQL Cell
# MAGIC
# MAGIC As shown immediately to the right of this notebook's name, the default language for the notebook is Python. If we want to run a SQL command in this notebook, we can start the cell with `%sql`. This is called a magic command. 
# MAGIC
# MAGIC Run the cell below. It contains a SQL command to view the contents of the same file as above.

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM csv.`dbfs:/mnt/dbacademy-datasets/get-started-with-data-engineering-on-databricks/v01/customers.csv`

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ### Markdown
# MAGIC
# MAGIC With the magic command **&percnt;md** we can render Markdown in a cell:
# MAGIC * Double click this cell to begin editing it
# MAGIC * Then hit **`Esc`** to stop editing
# MAGIC
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

# COMMAND ----------

# MAGIC %md
# MAGIC ### Create a New Notebook
# MAGIC There are many ways to create a new notebook. If you are already in a notebook, perform the following:
# MAGIC 1. Click the **File** menu and select **New notebook**  
# MAGIC The notebook opens in a new tab.
# MAGIC 1. Change the name of the new notebook to "My Notebook" by clicking the current name ("Untitled Notebook ...") in the upper-left corner 

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2023 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>