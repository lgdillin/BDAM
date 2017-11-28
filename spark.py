from pyspark import SparkContext, SparkConf

# The first thing a Spark program must do is create a SparkContext object,
# which tells spark how to access a cluster
conf = SparkConf().setAppName(bdam).setMaster(master)
sc = SparkContext(conf=conf)
