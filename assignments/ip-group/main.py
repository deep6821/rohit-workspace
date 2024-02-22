"""
Input CSV File
--------------
ChargingEvent,CPID,StartDate,EndDate,StartTime,EndTime,Energy,PluginDuration
15554472,AN07263,2017-10-01,2017-10-30,17:08:00,09:30:00,5.3,3.633333333333333
15554473,AN07264,2017-10-02,2017-10-30,17:08:00,09:45:00,5.3,3.633333333333333
15554474,AN07265,2017-10-03,2017-10-30,17:08:00,10:00:00,5.3,3.633333333333333
15554475,AN07266,2017-10-04,2017-10-30,17:08:00,10:15:00,5.3,3.633333333333333


PluginDuration column stores duration in hours

For each chargepoint, identified by it unique CPID, we would like 
to know the duration (in hours) of the longest plugin and duration(in hours) for average plugin.

 |-- ChargingEvent: integer (nullable = true)
 |-- CPID: string (nullable = true)
 |-- StartDate: string (nullable = true)
 |-- StartTime: string (nullable = true)
 |-- EndDate: string (nullable = true)
 |-- EndTime: string (nullable = true)
 |-- Energy: double (nullable = true)
 |-- PluginDuration: double (nullable = true)
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, col, concat, lit, max, round, to_timestamp


class ChargePointsETLJob:
    input_path = 'data/input/electric-chargepoints-2017.csv'
    output_path = 'data/output/chargepoints-2017-analysis'

    def __init__(self):
        self.spark_session = (SparkSession.builder
                                          .master("local[*]")
                                          .appName("ElectricChargePointsETLJob")
                                          .getOrCreate())

    def extract(self):
        df = self.spark_session.read.csv(ChargePointsETLJob.input_path, header=True, inferSchema=True)
        return df

    def transform(self, df):
        df = df.withColumn("EndDateTime", to_timestamp(concat(col("EndDate"), lit(" "), col("EndTime")), "yyyy-MM-dd HH:mm:ss"))
        df = df.withColumn("StartDateTime", to_timestamp(concat(col("StartDate"), lit(" "), col("StartTime")), "yyyy-MM-dd HH:mm:ss"))
        
        df = df.withColumn("PluginDurationHours", (col("EndDateTime").cast("long") - col("StartDateTime").cast("long")) / 3600)
        
        transformed_df = (df.groupBy("CPID").agg(
            max(col("PluginDurationHours")).alias("max_duration"), 
            avg(col("PluginDurationHours")).alias("avg_duration")
            )
        )

        transformed_df = transformed_df.withColumnRenamed("CPID", "chargepoint_id")
        transformed_df = transformed_df.withColumn("max_duration", round(col("max_duration"), 2))
        transformed_df = transformed_df.withColumn("avg_duration", round(col("avg_duration"), 2))

        transformed_df = transformed_df.select("chargepoint_id", "max_duration", "avg_duration")

        return transformed_df

    def load(self, df):
        print("\n DF", df.show(5))
        df.write.parquet(ChargePointsETLJob.output_path)

    def run(self):
        self.load(self.transform(self.extract()))
