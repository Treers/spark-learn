import os
import sys
from . import config

class SparkSessionNow(object):
    '''
    spark = SparkSessionNow(is_remote=True) \
    		.spark_entry(appName='myapp',spark_home='/usr/local/spark')
    '''
    def __init__(self, is_remote=False):
        self.is_remote = is_remote

    def _remote_environ(self, spark_home):
        if isinstance("spark_home", str):
            sys_path = spark_home + '/python'
            os.environ['SPARK_HOME'] = spark_home
            sys.path.append(sys_path)

    def spark_entry(self, appName, config={'key':"spark.some.config.option",'value':"some-value"}, 
    				spark_home=None, master='local'):

        if self.is_remote:
            self._remote_environ(spark_home)

        from pyspark.sql import SparkSession
        spark = SparkSession.builder \
            .master(master) \
            .appName(appName) \
            .config(config['key'], config['value']) \
            .getOrCreate()

        return spark







