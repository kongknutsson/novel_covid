from mimetypes import init
from elasticsearch import Elasticsearch
from os import getenv
from dotenv import load_dotenv

load_dotenv()
ELASTIC_PASSWORD = getenv("ELASTIC_PASSWORD")
ELASTIC_USERNAME = getenv("ELASTIC_USERNAME")
ELASTIC_CERT = getenv("ELASTIC_CERT")

class ElasticHelper:

    def __init__(self) -> None:
        self.es = Elasticsearch(
            "https://localhost:9200",
            ca_certs= ELASTIC_CERT,
            basic_auth=("elastic", ELASTIC_PASSWORD),
            verify_certs=False
        )
    
    def bulk_insert(self):
        pass 
