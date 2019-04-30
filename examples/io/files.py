# -*- coding: utf-8 -*-
import sys
sys.path.append('/tmp/pycharm_project_102/spark-learn/')
from splearn.io.files import ReadFile
from splearn import configuration

configuration.Set(app_name='app', master='local')
configuration.Set(spark_home='/usr/local/spark')

read = ReadFile('/tmp/learningPySpark/Chapter03/flight-data/departuredelays.csv')
read.csv2frame(header='True', inferSchema='True', sep=',').show()

read2 = ReadFile('/user/hadoop/departuredelays.csv', hdfs=True)
read2.csv2frame(header='True', inferSchema='True', sep=',').show()

read3 = ReadFile('/usr/local/spark/examples/src/main/resources/people.json')
read3.json2frame().show()
