from injector import Module, provider, singleton
from db.session import Session
from db.crud.crud_patient import CRUDPatient


class CollectionModule(Module):
    @singleton
    @provider
    def provide_collection_session(self) -> Session:
        session = Session()
        session.connection.connect()
        session.init_collection()
        session.collection.load()
        return session
    