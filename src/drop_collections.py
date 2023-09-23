from pymilvus import utility
from db.session import Session
from logging import getLogger

logger = getLogger(__name__)

session = Session()

with session.connection:
    logger.warning("start droping collections")
    for collection in utility.list_collections():
        utility.drop_collection(collection)
        logger.warning(f"dropped collection {collection}")
    logger.warning("all collections dropped")