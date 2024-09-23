from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from testpdf.config.ConfigStore import *
from testpdf.functions import *

def pdf_source(spark: SparkSession) -> DataFrame:
    return spark.read\
        .format("binaryFile")\
        .schema(
          StructType([
            StructField("path", StringType(), True), StructField("modificationTime", TimestampType(), True), StructField("length", LongType(), True), StructField("content", BinaryType(), True)
        ])
        )\
        .load("dbfs:/FileStore/bobwelshmer/sample_data/Data_Prep_in_the_Cloud___Why_organizations_are_moving_off_Alteryx.pdf")
