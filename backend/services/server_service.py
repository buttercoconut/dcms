from .models import ServerStatus
from datetime import datetime
import random
from typing import List

def get_server_status() -> List[ServerStatus]:
    # Dummy implementation: return random status for 3 servers
    servers = [
        {"hostname": "server1", "ip_address": "192.168.1.10"},
        {"hostname": "server2", "ip_address": "192.168.1.11"},
        {"hostname": "server3", "ip_address": "192.168.1.12"},
    ]
    statuses: List[ServerStatus] = []
    for s in servers:
        status = random.choice(["online", "offline", "maintenance"])
        statuses.append(
            ServerStatus(
                hostname=s["hostname"],
                ip_address=s["ip_address"],
                status=status,
                last_checked=datetime.utcnow(),
            )
        )
    return statuses
