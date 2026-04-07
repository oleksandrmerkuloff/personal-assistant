import json
import uuid
from json.decoder import JSONDecodeError
from dataclasses import dataclass, asdict, field
from datetime import datetime
from typing import Optional, Any


@dataclass
class PasswordRecord:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str = ""
    password: str = ""
    salt: str = ""
    url: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.now)

    def get_records(
        self,
        file_path: str,
        name: Optional[str] = None,
        demonstrate: Optional[bool] = False,
    ) -> list[Any]:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                if isinstance(data, dict):
                    records = list(data.values())
                else:
                    records = data
            if name:
                records = [record for record in records if record["name"] == name]
        except (FileNotFoundError, JSONDecodeError):
            records = []
        if demonstrate:
            for record in records:
                for key, value in record.items():
                    print(f"{key}: {value}")
        return records

    def save(self, file_path) -> None:
        """Save new password record to the JSON file"""
        file_path = file_path + "passwords.json"

        password_data = asdict(self)
        password_data["created_at"] = password_data["created_at"].isoformat()

        records = self.get_records(file_path)

        records.append(password_data)

        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(records, file, indent=2, ensure_ascii=False)
