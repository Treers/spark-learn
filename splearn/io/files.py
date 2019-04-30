# -*- coding: utf-8 -*-

from ..utils._sessions import SessionInit
from ..utils._discriminators import is_paths


class ReadFile(SessionInit):
    """Interface used to load a DataFrame from external files

    :param file_path: The path of a file. Whether it is a local file or an HDFS file, the
        path should be in the same format as: /localhost/path/to/xxx.csv.
    :param hdfs: If True, the file will be read from HDFS, otherwise it will be read from
        the local file system.

    >>>
    """

    def __init__(self, *file_path, hdfs=False):
        if is_paths(file_path):
            if not hdfs:
                self.file_path = ['file://'+path for path in file_path]
            else:
                self.file_path = list(file_path)
        else:
            raise NotADirectoryError("The path may look like '/usr/local/xxx.csv'")

        super(ReadFile, self).__init__()

    def csv2frame(self, schema=None, sep=None, encoding=None, quote=None, escape=None,
                  comment=None, header=None, inferSchema=None, ignoreLeadingWhiteSpace=None,
                  ignoreTrailingWhiteSpace=None, nullValue=None, nanValue=None, positiveInf=None,
                  negativeInf=None, dateFormat=None, timestampFormat=None, maxColumns=None,
                  maxCharsPerColumn=None, maxMalformedLogPerPartition=None, mode=None):

        df = self.spark.read.csv(self.file_path[0], schema, sep, encoding, quote, escape,
                                 comment, header, inferSchema, ignoreLeadingWhiteSpace,
                                 ignoreTrailingWhiteSpace, nullValue, nanValue, positiveInf,
                                 negativeInf, dateFormat, timestampFormat, maxColumns,
                                 maxCharsPerColumn, maxMalformedLogPerPartition, mode)
        return df

    txt2frame = csv2frame

    def json2frame(self, schema=None, primitivesAsString=None, prefersDecimal=None,
                   allowComments=None, allowUnquotedFieldNames=None, allowSingleQuotes=None,
                   allowNumericLeadingZero=None, allowBackslashEscapingAnyCharacter=None,
                   mode=None, columnNameOfCorruptRecord=None, dateFormat=None, timestampFormat=None):

        df = self.spark.read.json(self.file_path[0], schema, primitivesAsString, prefersDecimal, allowComments,
                                  allowUnquotedFieldNames, allowSingleQuotes, allowNumericLeadingZero,
                                  allowBackslashEscapingAnyCharacter, mode, columnNameOfCorruptRecord,
                                  dateFormat, timestampFormat)
        return df

    def parquet2frame(self):
        df = self.spark.read.parquet(*self.file_path)
        return df
