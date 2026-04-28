from pyspark.sql import SparkSession
from pyspark.sql.functions import col, upper

# Initialize Spark Session
spark = SparkSession.builder.appName("InsuranceTransformation").getOrCreate()

# 1. Read raw JSON from GCS (Landing Zone)
# In an interview, say: "I read from the Bronze layer in GCS"
df = spark.read.json("gs://your-landing-bucket/raw_claims/*.json")

# 2. Simple Transformation: Flattening or Cleaning
# Example: Making policy types uppercase and filtering high-value claims
cleaned_df = df.withColumn("policy_type", upper(col("policy_type"))) \
               .filter(col("claim_amount") > 0)

# 3. Write clean data back to GCS or BigQuery
cleaned_df.write.mode("overwrite").parquet("gs://your-refined-bucket/cleaned_claims/")

spark.stop()