from datetime import datetime
from dataclasses import dataclass


@dataclass
class User:
    login: str
    password: str
    age: int = 0
    created_at: datetime = datetime.now()

    def __str__(self) -> str:
        return self.login
    
    def save(self, storage_path: str) -> None:
        pass
