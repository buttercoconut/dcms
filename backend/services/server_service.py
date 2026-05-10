# services/server_service.py
from sqlalchemy.orm import Session
from ..models.server import Server, ServerCreate, ServerRead

class ServerService:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Server).all()

    def create(self, server_in: ServerCreate):
        db_server = Server(**server_in.dict())
        self.db.add(db_server)
        self.db.commit()
        self.db.refresh(db_server)
        return db_server
