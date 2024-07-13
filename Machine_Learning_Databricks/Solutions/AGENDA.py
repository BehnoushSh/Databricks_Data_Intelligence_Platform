# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC
# MAGIC ## Get Started with Databricks for Machine Learning
# MAGIC
# MAGIC In this course, you will learn basic skills that will allow you to use the Databricks Data Intelligence Platform to perform a simple data science and machine learning workflow. You will be given a tour of the workspace, and you will be shown how to work with notebooks. You will train a baseline model with AutoML and transition the best model to production. Finally, the course will also introduce you to MLflow, feature store and workflows and demonstrate how to train and manage an end-to-end machine learning lifecycle. 
# MAGIC
# MAGIC
# MAGIC ## Course agenda
# MAGIC
# MAGIC | Time | Module &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; | Lessons &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; |
# MAGIC |:----:|-------|-------------|
# MAGIC | 70m    | **[Databricks DI Platform Fundamentals]($./M01 - Databricks DI Platform Fundamentals)**    | Databricks Fundamentals<br>[Demo: Exploring the Workspace]($./M01 - Databricks DI Platform Fundamentals/01 - Exploring the Workspace) </br> Working with Notebooks </br> [Demo: Working with Notebooks]($./M01 - Databricks DI Platform Fundamentals/02 - Working with Notebooks) </br> Data Storage and Management </br> [Demo: Data Storage and Management]($./M01 - Databricks DI Platform Fundamentals/03 - Data Storage and Management)<br>[Lab: Get started with Databricks DI Platform]($./M01 - Databricks DI Platform Fundamentals/1.LAB -  Get started with Databricks DI Platform)|
# MAGIC | 50m    | **[Databricks for Machine Learning]($./M02 - Databricks for Machine Learning)** | Introduction to Databricks for Machine Learning </br> [Demo: Experimentation with AutoML]($./M02 - Databricks for Machine Learning/01 - Experimentation with AutoML) </br> End-to-End ML on the DI Platform </br> [Demo: End-to-End ML on the DI Platform]($./02 - Databricks for Machine Learning/2.2 - End-to-End ML on the DI Platform) | 
# MAGIC | 30m    | **[Comprehensive Lab]($./M03.1 - Lab)** | [Lab: Getting Started with Databricks for ML]($./M03.1 - Lab/2.Lab - Getting Started with Databricks for ML) | 
# MAGIC | 30m    | **[Capstone Project]($./M03.2 - Capstone Project)** | [01-Project-Details]($./M03.2 - Capstone Project/01-Project-Details) </br> [02- Example Project Solution]($./M03.2 - Capstone Project/02- Example Project Solution) |

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Requirements
# MAGIC
# MAGIC Please review the following requirements before starting the lesson:
# MAGIC
# MAGIC * To run demo and lab notebooks, you need to use one of the following Databricks runtime(s): **14.3.x-cpu-ml-scala2.12, 14.3.x-gpu-ml-scala2.12**

# COMMAND ----------

# MAGIC %md
# MAGIC &copy; 2024 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>