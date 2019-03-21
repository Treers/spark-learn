import sys
from setuptools import setup,find_packages

setup(
    name='dmtools',
    version='0.1.0',
    #url='',
    license='MIT',
    author='Youcai Fang',
    author_email='ahutfangyoucai@163.com',
    description=__doc__,
    keywords="spark-scorecard",
    packages=find_packages(),
    #scripts=[],
    #include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=['numpy', 'pandas','pyspark','scikit-learn',"ipywidgets >= 7.0.0"]
)
