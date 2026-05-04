#  PART 7 — DLT PIPELINE
# Tasks:
# 1. Create Bronze table (inline data)
# 2. Create Silver table with transformations
# 3. Create Gold table with aggregations
# 4. Define proper dependencies
# 5. Run the pipeline

import dlt
from pyspark.sql.functions import col, sum

# 1. Bronze Table (Raw Data - Inline)

@dlt.table(
    name="bronze_patients",
    comment="Raw patient data (Bronze Layer)"
)
def bronze_patients():
    data = [
        (101,"Arjun Reddy","Hyderabad","Cardiology",5000,1),
        (102,"Sneha Kapoor","Delhi","Orthopedics",3000,2),
        (103,"Rahul Sharma","Mumbai","Dermatology",1500,1),
        (104,"Priya Nair","Bangalore","Cardiology",5000,2),
        (105,"Vikram Singh","Chennai","Neurology",7000,1),
        (106,"Ananya Das","Kolkata","Orthopedics",3000,3),
        (107,"Karan Patel","Ahmedabad","Cardiology",5000,1),
        (108,"Meera Iyer","Bangalore","Dermatology",1500,2)
    ]
    columns = [
        "visit_id",
        "patient_name",
        "city",
        "department",
        "consultation_fee",
        "tests_count"
    ]
    return spark.createDataFrame(data, columns)

# 2. Silver Table (Transformations)

@dlt.table(
    name="silver_patients",
    comment="Cleaned and transformed data with total_bill"
)
def silver_patients():
    df = dlt.read("bronze_patients")

    return df.withColumn(
        "total_bill",
       df.consultation_fee + df.tests_count 
    )

# 3. Gold Table (Aggregations)

@dlt.table(
    name="gold_patients",
    comment="Aggregated revenue by department"
)
def gold_patients():
    df = dlt.read("silver_patients")

    return df.groupBy("department") \
             .agg(sum("total_bill").alias("total_revenue"))
