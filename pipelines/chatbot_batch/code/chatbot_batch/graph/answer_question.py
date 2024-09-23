from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from chatbot_batch.config.ConfigStore import *
from chatbot_batch.udfs.UDFs import *

def answer_question(spark: SparkSession, Aggregate_1: DataFrame) -> DataFrame:
    from spark_ai.llms.openai import OpenAiLLM
    from pyspark.dbutils import DBUtils
    OpenAiLLM(api_key = DBUtils(spark).secrets.get(scope = "open_ai", key = "token")).register_udfs(spark = spark)

    return Aggregate_1\
        .withColumn("_context", col("context"))\
        .withColumn("_query", col("input"))\
        .withColumn(
          "_template",
          lit(
            """Answer the question based on the context below.
Context:
```
{context}
```
Question: 
```
{query}
```
Answer:
"""
          )
        )\
        .withColumn("openai_answer", expr("openai_answer_question(_context, _query, _template)"))\
        .drop("_context", "_query")
