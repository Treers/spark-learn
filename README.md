# spark-learn
spark-learn is a library for data mining engineering built on top of Python Spark.
# LICENSE
MIT. See [License File](https://github.com/Treers/spark-scorecard/blob/master/LICENSE).
# Environmental Configuration
- [Apache Spark - Installation](http://dblab.xmu.edu.cn/blog/1689-2/)

- [How to add the remote PySpark module as an external library using local Pycharm](https://github.com/Treers/spark-learn/blob/master/etc/Pycharm_config.md)

      # An example under the configured environment
      
      import os
      import sys
      os.environ['SPARK_HOME'] = '/usr/local/spark'
      sys.path.append("/usr/local/spark/python")
     
      try:
          from pyspark import SparkContext
          from pyspark import SparkConf
     
          print ("Successfully imported Spark Modules")
     
      except ImportError as e:
          print ("Can not import Spark Modules", e)
          sys.exit(1)
          
          
      # After running the script, the output is as follows：
     
      ssh://hadoop@106.12.30.59:22/usr/bin/python3 -u /tmp/pycharm_project_192/test.py
      Successfully imported Spark Modules
     
      Process finished with exit code 0
      
