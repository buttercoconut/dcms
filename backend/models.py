from pydantic import BaseModel
from datetime import datetime

class ServerStatus(BaseModel):
    hostname: str
    ip_address: str
    status: str
    last_checked: datetime
