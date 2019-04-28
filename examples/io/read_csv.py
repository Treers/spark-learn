# -*- coding: utf-8 -*-
import sys
sys.path.append('/tmp/pycharm_project_920/spark-learn/')
from splearn.io import csv_txt

data=load_data.read_csv('/tmp/learningPySpark/Chapter03/flight-data/departuredelays.csv',spark_home='/usr/local/spark')

data.data2frame(header='True',inferSchema='True',sep=',').show()
