# -*- coding: utf-8 -*-
import sys
sys.path.append('/tmp/pycharm_project_102/spark-learn/')
from splearn.io import csv
from splearn import config

config.Set(app_name='app', master='local')
config.Set(spark_home='/usr/local/spark')

data=csv.ReadCsv('/tmp/learningPySpark/Chapter03/flight-data/departuredelays.csv')
data.to_frame(header='True', inferSchema='True', sep=',').show()

data2=csv.ReadCsv('/user/hadoop/departuredelays.csv')
data2.to_frame(header='True', inferSchema='True', sep=',').show()

