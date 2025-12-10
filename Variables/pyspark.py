from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum
spark = SparkSession.builder.appName("Day16-Sales").getOrCreate()
data = [
        ("2025-12-01", "P001", 2, 100.0),
        ("2025-12-01", "P002", 1, 200.0),
        ("2025-12-02", "P001", 3, 100.0),
        ("2025-12-02", "P003", 1, 150.0)]
columns = ["date", "product_id", "quantity", "price"]
df = spark.createDataFrame(data, columns)
# Calculate total revenue per day
sales_per_day = (df.withColumn("revenue", col("quantity") * col("price")).groupBy("date").agg(sum("revenue").alias("total_revenue")).orderBy("date"))
sales_per_day.show()