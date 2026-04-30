import dlt
from pyspark.sql.functions import col, sum, count, upper

# ---------------------------------------------------
# Question:
# Step 1 — Create a Bronze Table using inline raw data.
# The table should be named "bronze_patient_visits".
# Students must not modify the given data.
# ---------------------------------------------------
@dlt.table(
    name="bronze_patient_visits"
)
def bronze_patient_visits():
    data = [
        (1001,"Arjun Reddy","Hyderabad","Cardiology",5000,1),
        (1002,"Sneha Kapoor","Delhi","Orthopedics",3000,2),
        (1003,"Rahul Sharma","Mumbai","Dermatology",1500,1),
        (1004,"Priya Nair","Bangalore","Cardiology",5000,2),
        (1005,"Vikram Singh","Chennai","Neurology",7000,1),
        (1006,"Ananya Das","Kolkata","Orthopedics",3000,3),
        (1007,"Karan Patel","Ahmedabad","Cardiology",5000,1),
        (1008,"Meera Iyer","Bangalore","Dermatology",1500,2),
        (1009,"Farhan Ali","Hyderabad","Neurology",7000,1),
        (1010,"Divya Menon","Kochi","Cardiology",5000,1)
    ]

    columns = [
        "visit_id",
        "patient_name",
        "city",
        "department",
        "consultation_fee",
        "number_of_tests"
    ]

    return spark.createDataFrame(data, columns)


# ---------------------------------------------------
# Question:
# Step 2 — Create a Silver Table named "silver_patient_visits".
# Perform the following transformations:
# 1. Read data from "bronze_patient_visits".
# 2. Convert department names to uppercase.
# 3. Add a column: test_cost = number_of_tests * 2000.
# 4. Add a column: total_bill = consultation_fee + test_cost.
# 5. Remove records where consultation_fee <= 0.
# ---------------------------------------------------
@dlt.table(
    name="silver_patient_visits"
)
def silver_patient_visits():
    df = dlt.read("bronze_patient_visits")

    return df.select(
        col("visit_id"),
        col("patient_name"),
        col("city"),
        upper(col("department")).alias("department"),
        col("consultation_fee").cast("int"),
        col("number_of_tests").cast("int"),
        (col("number_of_tests") * 2000).alias("test_cost"),
        (col("consultation_fee") + (col("number_of_tests") * 2000)).alias("total_bill")
    ).filter(
        col("consultation_fee") > 0
    )


# ---------------------------------------------------
# Question:
# Step 3 — Create a Gold Table named "gold_hospital_summary".
# Perform the following analytics:
# 1. Group data by city and department.
# 2. Calculate:
#    - total_patients (count of records)
#    - total_tests (sum of number_of_tests)
#    - total_revenue (sum of total_bill)
# ---------------------------------------------------
@dlt.table(
    name="gold_hospital_summary"
)
def gold_hospital_summary():
    df = dlt.read("silver_patient_visits")

    return df.groupBy("city", "department").agg(
        count("*").alias("total_patients"),
        sum("number_of_tests").alias("total_tests"),
        sum("total_bill").alias("total_revenue")
    )