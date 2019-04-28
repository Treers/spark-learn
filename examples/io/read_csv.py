# -*- coding: utf-8 -*-
import sys
sys.path.append('/tmp/pycharm_project_920/spark-learn/')
from splearn.io import load_data

data=load_data.LoadFromLocal('/tmp/learningPySpark/Chapter03/flight-data/departuredelays.csv',spark_home='/usr/local/spark')

data.data2frame(header='True',inferSchema='True',sep=',').show()