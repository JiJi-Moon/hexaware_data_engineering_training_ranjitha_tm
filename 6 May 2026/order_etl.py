# PART 10 — DLT ASSESSMENT (ORDERS PIPELINE)

import dlt
from pyspark.sql.functions import col, sum

# 88. Create Bronze table using inline data.

@dlt.table(
    name="dlt_bronze_orders_pipeline_v2",
    comment="Raw product/order data (Bronze Layer)"
)
def dlt_bronze_orders_pipeline_v2():

    products_data = [
        (101,"Rice Bag","Groceries","Hyderabad",1200,50),
        (102,"Wheat Flour","Groceries","Bengaluru",900,80),
        (103,"Sunflower Oil","Groceries","Mumbai",1800,40),
        (104,"Milk Pack","Dairy","Chennai",60,200),
        (105,"Cheese Block","Dairy","Delhi",450,70),
        (106,"Soap","Personal Care","Kolkata",120,300),
        (107,"Shampoo","Personal Care","Pune",320,150),
        (108,"Toothpaste","Personal Care","Ahmedabad",90,250),
        (109,"Notebook","Stationery","Hyderabad",75,500),
        (110,"Pen Pack","Stationery","Mumbai",110,400),
        (111,"LED TV","Electronics","Delhi",45000,15),
        (112,"Refrigerator","Electronics","Chennai",38000,10),
        (113,"Washing Machine","Electronics","Bengaluru",29000,12),
        (114,"Mobile Phone","Electronics","Hyderabad",25000,35),
        (115,"Laptop","Electronics","Pune",62000,18),
        (116,"Air Conditioner","Electronics","Mumbai",42000,9),
        (117,"Mixer Grinder","Home Appliances","Kolkata",3500,45),
        (118,"Water Purifier","Home Appliances","Delhi",12000,20),
        (119,"Ceiling Fan","Home Appliances","Ahmedabad",2800,60),
        (120,"Gas Stove","Home Appliances","Chennai",5500,25)
    ]

    columns = [
        "product_id",
        "product_name",
        "category",
        "city",
        "price",
        "quantity"
    ]

    return spark.createDataFrame(products_data, columns)


# 89. Create Silver cleaned table.
# 90. Add total revenue calculation.
# 91. Remove invalid records.

@dlt.table(
    name="dlt_silver_orders_pipeline_v2",
    comment="Cleaned orders with total revenue"
)
def dlt_silver_orders_pipeline_v2():

    df = dlt.read("dlt_bronze_orders_pipeline_v2")

    return (
        df
        .filter(col("price") > 0)
        .filter(col("quantity") > 0)
        .withColumn(
            "total_revenue",
            col("price") * col("quantity")
        )
    )


# 92 Gold by City

@dlt.table(
    name="dlt_gold_city_revenue_pipeline_v2",
    comment="Revenue aggregated by city"
)
def dlt_gold_city_revenue_pipeline_v2():

    df = dlt.read("dlt_silver_orders_pipeline_v2")

    return df.groupBy("city") \
             .agg(sum("total_revenue").alias("total_revenue"))


# 93 Gold by Category

@dlt.table(
    name="dlt_gold_category_revenue_pipeline_v2",
    comment="Revenue aggregated by category"
)
def dlt_gold_category_revenue_pipeline_v2():

    df = dlt.read("dlt_silver_orders_pipeline_v2")

    return df.groupBy("category") \
             .agg(sum("total_revenue").alias("total_revenue"))