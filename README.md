# spark-learn
spark-learn is a library for data mining engineering built on top of Python Spark.
# LICENSE
MIT. See [License File](https://github.com/Treers/spark-scorecard/blob/master/LICENSE).
# Environmental Configuration
1.[Installation and Use of Spark](http://dblab.xmu.edu.cn/blog/1689-2/)

2.[How to call remote Python and add the PySpark module as an external library using local Pycharm](https://blog.csdn.net/u011596455/article/details/78979378)


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

<img src="https://github.com/Treers/spark-learn/blob/master/etc/1.jpg" width="70%" height="60%" div align=center>





