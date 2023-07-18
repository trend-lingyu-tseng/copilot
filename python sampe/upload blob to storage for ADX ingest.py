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


connectsring="your connection string";
container=ContainerClient.from_container_url(connectsring);
blob_client =container.get_blob_client('folder/filename');

blob_metadata = {'kustoTable': 'yourtablename', 'kustoDataFormat':'yourdatatype(json/mutijson/csv/..)','kustoIngestionMappingReference':'yourmappingname','kustoDatabase':'yourdatabasename','rawSizeBytes':'filesize(b)'}
    with open("filename", "rb") as data:
         blob_client.upload_blob(data)
         blob_client.set_blob_metadata(metadata=blob_metadata)
