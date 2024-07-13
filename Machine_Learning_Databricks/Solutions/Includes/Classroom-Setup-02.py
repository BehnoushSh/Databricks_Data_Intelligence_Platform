# Databricks notebook source
# MAGIC %run ./_common

# COMMAND ----------

# create a sample table to be used for the lesson
def create_customers_table(self):
    from pyspark.sql.functions import col

    df_customer_demographics = (spark.read.csv(f"{DA.paths.datasets}/telco/customer-demographics.csv", header=True, inferSchema=True)
                                .withColumnRenamed('gender',"Gender")
                                .withColumnRenamed('customerID','CustomerID'))

    df_customer_details = (spark.read.csv(f"{DA.paths.datasets}/telco/customer-details.csv", header=True, inferSchema=True)
                           .withColumnRenamed('CustomerID', 'id'))

    df_customers = (df_customer_demographics.join(df_customer_details, col('customerID') == col('id'))
                    .select('CustomerID', 'Gender','SeniorCitizen','PhoneService', 'MultipleLines','PaymentMethod','MonthlyCharges', 'Churn'))

    experiment_data, predict_data = df_customers.randomSplit([0.99, 0.01], seed=42)
    
    #save to catalog
    spark.sql(f"USE CATALOG {DA.catalog_name}")
    experiment_data.write.mode('overwrite').saveAsTable('customers')
    predict_data.write.mode('overwrite').saveAsTable('customers_to_predict')
    
DBAcademyHelper.monkey_patch(create_customers_table)

# COMMAND ----------

DA = DBAcademyHelper(course_config, lesson_config)  # Create the DA object
DA.reset_lesson()                                   # Reset the lesson to a clean state
DA.init()                                           # Performs basic intialization including creating schemas and catalogs
DA.conclude_setup()                                 # Finalizes the state and prints the config for the student