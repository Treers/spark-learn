# -*- coding: utf-8 -*-

from ..utils._sessions import SessionInit
from ..utils._discriminators import is_path


class ReadFile(SessionInit):
    """Interface used to load a DataFrame from external .csv or .txt files

    :param file_path: The path of a file. Whether it is a local file or an HDFS file, the
        path should be in the same format as: /localhost/path/to/xxx.csv.
    :param hdfs: If True, the file will be read from HDFS, otherwise it will be read from
        the local file system.

    >>>
    """

    def __init__(self, file_path, hdfs=False):
        if is_path(file_path):
            if not hdfs:
                self.file_path = 'file://' + file_path
            else:
                self.file_path = file_path
        else:
            raise NotADirectoryError("The path may look like '/usr/local/xxx.csv'")

        super(ReadFile, self).__init__()

    def csv2frame(self, schema=None, sep=None, encoding=None, quote=None, escape=None,
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


