import logging
from common.config import settings
from milvus.client import Collection, MilvusConnection
from pymilvus import CollectionSchema, utility
import pandas as pd
from db.models.patients import patients
from db.models.patient_2 import patients2
from db.proxy import CollectionProxy


logger = logging.getLogger(__name__)

def init_if_need(conn: MilvusConnection):
    if not utility.has_collection(patients.table_name) or not utility.has_collection(patients2.table_name):
        logger.info("init collections")
        check_vector_fields()
        init_db(conn)


def check_vector_fields():
    db_vector_fields = sorted(patients.vector_fields + patients2.vector_fields)
    settings_vector_fields = sorted(settings.COLUMNS_NAME_MAP[_] for _ in settings.ANN_SEARCH_FIELDS)
    assert db_vector_fields == settings_vector_fields,\
        "common/config.py$Settings内的ANN_SEARCH_FIELDS字段必须与db/model内表定义的向量字段一致，" \
            f"{db_vector_fields=}, {settings_vector_fields=}"

def init_db(conn: MilvusConnection) -> None:
    create_collection(conn)
    logging.info("created collection1, collection2")


def create_collection(conn: MilvusConnection) -> tuple[Collection, Collection]:
    return (conn.create_collection(
        collection_name=patients.table_name,
        schema=CollectionSchema(patients.fields),
        vector_fields=patients.vector_fields,
        index_params=patients.index_params
    ), conn.create_collection(
        collection_name=patients2.table_name,
        schema=CollectionSchema(patients2.fields),
        vector_fields=patients2.vector_fields,
        index_params=patients2.index_params
    ))