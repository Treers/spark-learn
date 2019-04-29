# -*- coding: utf-8 -*-

from ..utils._sessions import SparkSessionNow
from ..utils._discriminators import is_path
from .. import config


class ReadCsv(object):
    """
    Interface used to load a DataFrame from external .csv or .txt files

    Parameters
    ----------
    file_path : str, path object
        Whether it is a local file or an HDFS file, the path should be in
        the same format as: /localhost/path/to/xxx.csv.



    """
    def __init__(self, file_path, hdfs=False):

        if is_path(file_path):
            if not hdfs:
                self.file_path = 'file://' + file_path
            else:
                self.file_path = file_path
        else:
            raise NotADirectoryError("The path may look like '/usr/local/xxx.csv'")

        self.spark = SparkSessionNow(spark_home=config.get('spark_home', default=None)) \
            .spark_entry(config.get('app_name'),
                         config.get('spark_config', default=['', '', None]),
                         config.get('master'))

    def to_frame(self, schema=None, sep=None, encoding=None, quote=None, escape=None,
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