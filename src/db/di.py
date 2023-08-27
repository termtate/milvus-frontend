from injector import Module, provider, Injector, inject, singleton
from ml.config import settings
from db.proxy import CollectionProxy
from db.session import Session


class CollectionModule(Module):
    @singleton
    @provider
    def provide_collection_session(self) -> Session:
        return Session()