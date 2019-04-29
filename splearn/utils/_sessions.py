import os
import sys


class SparkSessionNow(object):
    '''
    note
    '''

    def __init__(self, spark_home):
        self.spark_home = spark_home

    def _remote_environ(self):
        if isinstance(self.spark_home, str):
            sys_path = self.spark_home + '/python'
            os.environ['SPARK_HOME'] = self.spark_home
            sys.path.append(sys_path)

    def spark_entry(self, appName, config, master):

        if self.spark_home is not None:
            self._remote_environ()

        from pyspark.sql import SparkSession
        spark = SparkSession.builder \
            .master(master) \
            .appName(appName) \
            .config(config[0], config[1], config[2]) \
            .getOrCreate()

        return spark
