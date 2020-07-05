from config.settings import settings
from typing import Optional


def provide_local_data() -> Optional[dict]:
    local_data = settings.read_local_data()
    if local_data:
        return local_data
    else:
        return None


def persist_local_data(data):
    settings.persist_local_data(data=data)
