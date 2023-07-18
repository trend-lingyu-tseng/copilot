# this is bif sample code for update blob to Azure storage for ADX ingest
import io;
import datetime;
import time;
import json;
import six;
import os, uuid;
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__
import pytz;
import asyncio;
from azure.storage.blob.aio import BlobClient;

def upload_to_blob_for_adxingest(connectionstring,filename,tablename,fileformat,yourdatatype,yourmapping,databasename,filesize):
    connectsring="your connection string";
    container=ContainerClient.from_container_url(connectsring);
    blob_client =container.get_blob_client('folder/filename');
    
    blob_metadata = {'kustoTable': tablename, 'kustoDataFormat':fileformat,'kustoIngestionMappingReference':'yourmapping','kustoDatabase':'databasename,'rawSizeBytes':filesize}
        with open("filename", "rb") as data:
             blob_client.upload_blob(data)
             blob_client.set_blob_metadata(metadata=blob_metadata)
