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
      



Inputs:
- S is the training set,  
- L is a classification learning algorithm,  
- C is a cost matrix,  
- m is the number of resamples to generate,  
- n is the number of examples in each resample,  
- p is True iff L produces class probabilities,  
- q is True iff all resamples are to be used for each example

Procedure MetaCost (S, L, C, m, n, p, q)

For i = 1 to m
- Let S<sub>i</sub> be a resample of S with n examples.
- Let M<sub>i</sub> = Model produced by applying L to S<sub>i</sub>.

For each example x in S
- For each class j  
  - Let P(j|x) = \frac{1}{$\sum_{i}$} 
  
  \Sigma
  
 http://chart.googleapis.com/chart?cht=tx&chl=\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a})





