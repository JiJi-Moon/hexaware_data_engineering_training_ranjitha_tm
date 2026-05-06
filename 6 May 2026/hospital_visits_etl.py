# PART 10 — DLT ASSESSMENT
import dlt
from pyspark.sql.functions import col, sum

# 88. Create Bronze table using inline patient visit data.

@dlt.table(
    name="dlt_bronze_patient_visits_v1",
    comment="Raw patient visit data (Bronze Layer)"
)
def dlt_bronze_patient_visits_v1():
    data = [
        (1, "Hyderabad", "Cardiology", 1200, 2),
        (2, "Bengaluru", "Dermatology", 800, 1),
        (3, "Mumbai", "Orthopedics", 1500, 3),
        (4, "Delhi", "Pediatrics", 900, 1),
        (5, "Chennai", "Cardiology", 1300, 2),
        (6, "Hyderabad", "Neurology", 2000, 4),
        (7, "Kolkata", "Dermatology", 850, 1),
        (8, "Bengaluru", "Orthopedics", 1400, 2)
    ]

    columns = [
        "visit_id",
        "city",
        "specialization",
        "consultation_fee",
        "tests_count"
    ]

    return spark.createDataFrame(data, columns)


# 89. Create Silver table with cleaned fields.
# 90. Add total bill calculation in Silver.
# 91. Remove invalid records in Silver.

@dlt.table(
    name="dlt_silver_patient_visits_v1",
    comment="Cleaned data with total bill calculation"
)
def dlt_silver_patient_visits_v1():
    df = dlt.read("dlt_bronze_patient_visits_v1")

    return (
        df
        .filter(col("consultation_fee") > 0)
        .filter(col("tests_count") > 0)
        .withColumn(
            "total_bill",
            col("consultation_fee") * col("tests_count")
        )
    )


# 92. Create Gold table grouped by city.

@dlt.table(
    name="dlt_gold_city_revenue_v1",
    comment="Total revenue grouped by city"
)
def dlt_gold_city_revenue_v1():
    df = dlt.read("dlt_silver_patient_visits_v1")

    return df.groupBy("city") \
             .agg(sum("total_bill").alias("total_revenue"))


# 93. Create Gold table grouped by specialization.

@dlt.table(
    name="dlt_gold_specialization_revenue_v1",
    comment="Total revenue grouped by specialization"
)
def dlt_gold_specialization_revenue_v1():
    df = dlt.read("dlt_silver_patient_visits_v1")

    return df.groupBy("specialization") \
             .agg(sum("total_bill").alias("total_revenue"))