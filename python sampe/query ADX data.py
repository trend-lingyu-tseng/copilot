#this is sample for query adx data
from pyspark.sql import SparkSession
pyKusto = SparkSession.builder.appName("kustoPySpark").getOrCreate()
def ADXquery(cluster,db,query,appid,appkey):
  kustoOptions = {"kustoCluster":"private-dataview.westus2", "kustoDatabase" : "VisionOne_Report", "kustoAadAppId":appid ,
 "kustoAadAppSecret":dbutils.secrets.get(scope = "adx-connect", key = appkey), "kustoAadAuthorityID":"trendid"}
  KQLstring=query
  df  = pyKusto.read. \
            format("com.microsoft.kusto.spark.datasource"). \
            option("kustoCluster", kustoOptions["kustoCluster"]). \
            option("kustoDatabase", kustoOptions["kustoDatabase"]). \
            option("kustoQuery", KQLstring). \
            option("kustoAadAppId", kustoOptions["kustoAadAppId"]). \
            option("kustoAadAppSecret", kustoOptions["kustoAadAppSecret"]). \
            option("kustoAadAuthorityID", kustoOptions["kustoAadAuthorityID"]). \
            load()
