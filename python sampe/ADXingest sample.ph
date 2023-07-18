from datetime import timedelta
from azure.kusto.data import KustoClient, KustoConnectionStringBuilder, ClientRequestProperties
from azure.kusto.data.exceptions import KustoServiceError
from azure.kusto.data.helpers import dataframe_from_result_table
import datetime
import os, uuid
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from azure.identity import ClientSecretCredential
from azure.storage.blob import BlobPrefix

"""ADX ingest data from blob"""

def ingest(data_cluster,authority_id,client_id,client_secret,tablename,containername,storagename,dbname) :
    kcsb = KustoConnectionStringBuilder.with_aad_application_key_authentication(data_cluster, client_id, client_secret, authority_id)
    client = KustoClient(kcsb)
    pendosas= client_secret = dbutils.secrets.get(scope = "analyticsonekeyvault", key = "msppendo")
    etl=(datetime.datetime.today()- timedelta(days=1)).strftime("%Y-%m-%d")
    tags=datetime.datetime.today().strftime("%Y-%m-%d %H:%M")
    query = ".ingest into table ['{tablename}'] (h'https://{storagename}.blob.core.windows.net/containername/{tablename}/d={etl}/TMRM-msp-feature_events_excluded-{etl}.json?{pendosas}',h'https://bifexsql.blob.core.windows.net/worryfreependo/{tablename}/d={etl}/TMRM-msp-feature_events-{etl}.json?{pendosas}') with (format='multijson',ingestionMappingReference='{tablename}_mapping',ingestionMappingType='json',tags=\"['{tags}']\")".format(tablename=tablename , etl=etl,pendosas=pendosas,tags=tags,storagename=storagename)
    try:
        client.execute(dbname, query)
    print(query)
        except Exception as e:
    print("Cannot connect to ADX. Error message: {}".format(e))