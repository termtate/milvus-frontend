from injector import Module, provider, Injector, inject, singleton
from ml.config import settings
from db.proxy import CollectionProxy
from db.session import Session
from db.crud.crud_patient import CRUDPatient


class CollectionModule(Module):
    @singleton
    @provider
    def provide_collection_session(self) -> Session:
        session = Session()
        session.connection.connect()
        session.init_collection()
        return session
    
    @singleton
    @provider
    def provide_crud_patient(self, session: Session) -> CRUDPatient:
        return CRUDPatient(session)