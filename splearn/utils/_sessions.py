import os
import sys
from .. import configuration


class SessionInit(object):
    '''
    note
    '''

    def __init__(self):

        self.spark = self.spark_entry(configuration.get('app_name'),
                                      configuration.get('spark_config', default=['', '', None]),
                                      configuration.get('master'))

    @staticmethod
    def _remote_environ(spark_home):
        if isinstance(spark_home, str):
            sys_path = spark_home + '/python'
            os.environ['SPARK_HOME'] = spark_home
            sys.path.append(sys_path)

    def spark_entry(self, app_name, spark_config, master):

        spark_home = configuration.get('spark_home', default=None)

        if spark_home is not None:
            self._remote_environ(spark_home)

        from pyspark.sql import SparkSession
        spark = SparkSession.builder \
            .master(master) \
            .appName(app_name) \
            .config(spark_config[0], spark_config[1], spark_config[2]) \
            .getOrCreate()

        return spark

