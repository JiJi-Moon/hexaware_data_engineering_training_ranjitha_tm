# ----------------------------------------------------------
# 🔥 FINAL CAPSTONE
#
# Build a system:
# Raw Data → Clean Data → Analytics → Governed Data
#
# Requirements:
# ✔ Use Delta tables
# ✔ Use incremental logic
# ✔ Build DLT pipeline
# ✔ Create a simple Unity Catalog structure
# ----------------------------------------------------------

import dlt
from pyspark.sql.functions import col, sum

# ----------------------------------------------------------
# 🔷 BRONZE LAYER (RAW DATA)
# ----------------------------------------------------------
@dlt.table(
    name="final_bronze_patients",
    comment="Raw patient data (ingestion layer)"
)
def final_bronze_patients():
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


# ----------------------------------------------------------
# 🔷 SILVER LAYER (CLEAN + TRANSFORM)
# ----------------------------------------------------------
@dlt.table(
    name="final_silver_patients",
    comment="Cleaned data with derived total_bill"
)
def final_silver_patients():
    df = dlt.read("final_bronze_patients")

    return df.withColumn(
        "total_bill",
        col("consultation_fee") * col("tests_count")
    )


# ----------------------------------------------------------
# 🔷 GOLD LAYER (ANALYTICS)
# ----------------------------------------------------------
@dlt.table(
    name="final_gold_revenue_by_department",
    comment="Aggregated revenue per department"
)
def final_gold_revenue_by_department():
    df = dlt.read("final_silver_patients")

    return df.groupBy("department") \
             .agg(sum("total_bill").alias("total_revenue"))


# ----------------------------------------------------------
# 🔷 INCREMENTAL LOGIC (STREAMING / UPSERT SIMULATION)
# ----------------------------------------------------------
@dlt.table(
    name="final_incremental_updates",
    comment="Simulated incoming daily updates"
)
def final_incremental_updates():
    data = [
        (101,"Arjun Reddy","Hyderabad","Cardiology",6000,2),
        (109,"New Patient","Chennai","Neurology",7000,1)
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


@dlt.table(
    name="final_silver_patients_incremental",
    comment="Incrementally updated patient data"
)
def final_silver_patients_incremental():
    base = dlt.read("final_silver_patients")
    updates = dlt.read("final_incremental_updates")

    updates = updates.withColumn(
        "total_bill",
        col("consultation_fee") * col("tests_count")
    )

    # Simulated merge logic using union + dedup
    combined = base.unionByName(updates)

    return combined.dropDuplicates(["visit_id"])


# ----------------------------------------------------------
# 🔷 GOVERNED DATA (FINAL TABLE)
# ----------------------------------------------------------
@dlt.table(
    name="final_governed_patients",
    comment="Final curated and governed dataset"
)
def final_governed_patients():
    return dlt.read("final_silver_patients_incremental")