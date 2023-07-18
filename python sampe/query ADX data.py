"""query azure data explorer data by cluster,db,query,appid,appkey """ 

def ADXquery(cluster,db,query,appid,appkey):
  kustoOptions = {"kustoCluster":cluster, "kustoDatabase" :db, "kustoAadAppId":appid ,
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
