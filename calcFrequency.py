from pyspark import SparkContext, SparkConf 

conf = SparkConf().setAppName(appName).setMaster(master)
sc = SparkContext(conf=conf)

distFile = sc.textFile("sherlock.txt")
