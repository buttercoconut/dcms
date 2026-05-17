from pydantic import BaseModel

class Server(BaseModel):
    id: int
    hostname: str
    status: str
    cpu_usage: float
    memory_usage: float
