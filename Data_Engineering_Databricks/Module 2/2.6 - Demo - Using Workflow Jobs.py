# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # Demo: Databricks Workflows
# MAGIC In this lesson, we are going to create a simple workflow job that will run a notebook on a specific schedule.
# MAGIC
# MAGIC **Learning Objectives**
# MAGIC 1. Describe Workflows as a capability to productionize data workflows.
# MAGIC 1. Describe Jobs as a simple solution to schedule and automate one or more tasks.
# MAGIC 1. Recognize the types of assets that are able to be automated with Jobs.
# MAGIC 1. Automate the running of a single notebook using Jobs.
# MAGIC 1. Review the results of a completed single-notebook Job.
# MAGIC 1. Describe Delta Live Tables as a solution for building and running robust data pipelines.

# COMMAND ----------

# MAGIC %run ../Includes/Classroom-Setup-10

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ### Generate Job Configuration
# MAGIC
# MAGIC Configuring this job will require parameters unique to a given user.
# MAGIC
# MAGIC Run the cell below to print out values you'll use to configure your job in subsequent steps.

# COMMAND ----------

DA.print_job_config_v1()

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ### Configure Job with a Single Notebook Task
# MAGIC
# MAGIC When using the Jobs UI to orchestrate a workload with multiple tasks, you'll always begin by creating a job with a single task.
# MAGIC
# MAGIC Steps:
# MAGIC 1. Right-click the **Workflows** button on the sidebar, and open the link in a new tab. This way, you can refer to these instructions, as needed.
# MAGIC 1. Click the **Jobs** tab, and click the **Create Job** button.
# MAGIC 1. Configure the job and task as specified below. You'll need the values provided in the cell output above for this step.
# MAGIC
# MAGIC | Setting | Instructions |
# MAGIC |--|--|
# MAGIC | Task name | Enter **Example Job** |
# MAGIC | Type | Choose **Notebook**. Note in the dropdown list the many different types of jobs that can be scheduled |
# MAGIC | Source | Choose **Workspace** |
# MAGIC | Path | Use the navigator to specify the **My Notebook Path** provided above |
# MAGIC | Cluster | From the dropdown menu, under **Existing All Purpose Clusters**, select your cluster |
# MAGIC | Job name | In the top-left of the screen, enter the **Job Name** provided above to add a name for the job (not the task) |
# MAGIC
# MAGIC <br>
# MAGIC
# MAGIC 1. Click the **Create** button.
# MAGIC 1. Click the blue **Run now** button in the top right to start the job.
# MAGIC
# MAGIC <img src="https://files.training.databricks.com/images/icon_note_24.png"> **Note**: When selecting your all-purpose cluster, you may get a warning about how this will be billed as all-purpose compute. Production jobs should always be scheduled against new job clusters appropriately sized for the workload, as this is billed at a much lower rate.

# COMMAND ----------

# MAGIC %md
# MAGIC If you do not wish to manually configure the job, you can run the code in the next cell to configure it automatically.

# COMMAND ----------

# Optional: Run this if you did not manually create the job as outlined above
DA.create_job_v1()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Check the Configuration
# MAGIC Run the next cell to verify that things are setup correctly.

# COMMAND ----------

DA.validate_job_v1_config()

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC ### Explore Scheduling Options
# MAGIC Steps:
# MAGIC 1. On the right hand side of the Jobs UI, locate the **Schedules & Triggers** section.
# MAGIC 1. Select the **Add trigger** button to explore scheduling options.
# MAGIC 1. Changing the **Trigger type** from **None (Manual)** to **Scheduled** will bring up a cron scheduling UI.
# MAGIC    - This UI provides extensive options for setting up chronological scheduling of your Jobs. Settings configured with the UI can also be output in cron syntax, which can be edited if custom configuration not available with the UI is needed.
# MAGIC 1. Select **Cancel** to return to Job details.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC ### Review Run
# MAGIC
# MAGIC To review the job run:
# MAGIC 1. On the Job details page, select the **Runs** tab in the top-left of the screen (you should currently be on the **Tasks** tab)
# MAGIC 1. Find your job.
# MAGIC 1. Open the output details by clicking on the timestamp field under the **Start time** column
# MAGIC     - If **the job is still running**, you will see the active state of the notebook with a **Status** of **`Pending`** or **`Running`** in the right side panel. 
# MAGIC     - If **the job has completed**, you will see the full execution of the notebook with a **Status** of **`Succeeded`** or **`Failed`** in the right side panel
# MAGIC
# MAGIC The job we cretead runs the notebook in the lesson, **Data Management**. It will use `COPY INTO` to ingest new files and `MERGE INTO` to add the data in those files to our `customers_silver_merged` table. If we wanted to, we could add code in that notebook that would clean the data in the `customers_silver_merged` table.

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2023 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>