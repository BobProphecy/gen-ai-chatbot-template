from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from testpdf.config.ConfigStore import *
from testpdf.functions import *
from prophecy.utils import *
from testpdf.graph import *

def pipeline(spark: SparkSession) -> None:
    df_pdf_source = pdf_source(spark)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("testPDF")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/testPDF")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/testPDF", config = Config)(pipeline)

if __name__ == "__main__":
    main()
