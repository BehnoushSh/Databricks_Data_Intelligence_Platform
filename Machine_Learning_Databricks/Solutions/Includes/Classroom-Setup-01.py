# Databricks notebook source
# MAGIC %run ./_common

# COMMAND ----------

# create a sample table to be used for the lesson
def create_customers_table(self):
    spark.sql(f"USE CATALOG {DA.catalog_name};")

    spark.sql(f"""
        CREATE OR REPLACE TEMPORARY VIEW `temp-retail-customers`
        USING csv
        OPTIONS (
        path "{DA.paths.datasets}/retail/customers.csv",
        header "true",
        inferSchema "true"
        )
    """)

    spark.sql(f"""
        CREATE OR REPLACE TABLE `retail-customers` AS
        SELECT * FROM `temp-retail-customers`;
    """)

    print("Customers table created successfully!")
DBAcademyHelper.monkey_patch(create_customers_table)

# COMMAND ----------

DA = DBAcademyHelper(course_config, lesson_config)  # Create the DA object
DA.reset_lesson()                                   # Reset the lesson to a clean state
DA.init()                                           # Performs basic intialization including creating schemas and catalogs
DA.conclude_setup()                                 # Finalizes the state and prints the config for the student