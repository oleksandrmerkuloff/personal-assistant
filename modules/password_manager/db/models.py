import json
import uuid
from json.decoder import JSONDecodeError
from dataclasses import dataclass, asdict, field
from datetime import datetime
from typing import Optional


@dataclass
class PasswordRecord:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str = ''
    password: str = ''
    salt: str = ''
    url: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.now)

    def save(self, file_path) -> None:
        file_path = file_path + 'passwords.json'

        password_data = asdict(self)
        password_data['created_at'] = password_data['created_at'].isoformat()

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                if isinstance(data, dict):
                    records = list(data.values())
                else:
                    records = data
        except (FileNotFoundError, JSONDecodeError):
            records = []
        
        records.append(password_data)

        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(records, file, indent=2, ensure_ascii=False)
