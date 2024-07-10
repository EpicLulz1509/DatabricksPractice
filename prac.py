data = [[1, "A"], [2, "B"], [3, "C"]]
sdf = spark.createDataFrame(data, schema="id LONG, name STRING")
display(sdf)
