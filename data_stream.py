from pyspark.sql import SparkSession
from models import Data
from db import db
import json
from datetime import datetime

spark = SparkSession.builder \
    .appName("KafkaToMemorySingleMachine") \
    .master("local[*]") \
    .getOrCreate()

df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "fault_diagnosis_topic") \
    .option("startingOffsets", "earliest") \
    .load()

# 全局列表用于存储浮点数
global_floats = []


def process_batch(batch_df, batch_id):
    # 从 batch_df 中解析数据并写入数据库
    records = batch_df.selectExpr("CAST(value AS STRING) as json_str").collect()
    for record in records:
        json_data = json.loads(record.json_str)
        new_data = Data(
            machine_id=json_data['machine_id'],
            sensor_id=json_data['sensor_id'],
            value=float(json_data['value']),
            time=datetime.strptime(json_data['time'], '%Y-%m-%dT%H:%M:%S'),
            unit=json_data.get('unit', None)  # 假设单位不是必须的
        )
        db.session.add(new_data)
    db.session.commit()


query = df.writeStream \
    .foreachBatch(process_batch) \
    .start()

query.awaitTermination()
