# -*- coding: utf-8 -*-

from ..common.spark_session import SparkSessionNow
from ..common.identification import is_path


class LoadFromLocal(object):
    def __init__(self, file_path, spark_home=None, config={'key': 'default', 'value': 'default'},
                 appName='LoadCSVFromLocal', master='local', is_remote=True):

        if is_path(file_path):
            self.file_path = 'file://' + file_path
        else:
            raise NotADirectoryError("The path may look like '/usr/local/xxx.csv'")

        if is_remote and spark_home is None:
            raise ValueError("'spark_home' cannot be set to None because 'is_remote' equals True")

        self.spark = SparkSessionNow(is_remote=is_remote) \
            .spark_entry(appName, config, spark_home, master)

    def data2frame(self, schema=None, sep=None, encoding=None, quote=None, escape=None,
                   comment=None, header=None, inferSchema=None, ignoreLeadingWhiteSpace=None,
                   ignoreTrailingWhiteSpace=None, nullValue=None, nanValue=None, positiveInf=None,
                   negativeInf=None, dateFormat=None, timestampFormat=None, maxColumns=None,
                   maxCharsPerColumn=None, maxMalformedLogPerPartition=None, mode=None):
        df = self.spark.read.csv(self.file_path, schema, sep, encoding, quote, escape,
                                 comment, header, inferSchema, ignoreLeadingWhiteSpace,
                                 ignoreTrailingWhiteSpace, nullValue, nanValue, positiveInf,
                                 negativeInf, dateFormat, timestampFormat, maxColumns,
                                 maxCharsPerColumn, maxMalformedLogPerPartition, mode)
        return df


class LoadFromHDFS(object):
    def __init__(self, file_path, spark_home=None, config={'key': 'default', 'value': 'default'},
                 appName='LoadCSVFromLocal', master='local', is_remote=True):
        if is_path(file_path):
            self.file_path = 'file://' + file_path

    def __repr__(self):
        return "You should provide the hdfs://host:port"
