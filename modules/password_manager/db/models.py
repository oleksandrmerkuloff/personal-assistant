import json
import uuid
from json.decoder import JSONDecodeError
from dataclasses import dataclass, asdict, field
from datetime import datetime as dt
from typing import Optional, Any


@dataclass
class PasswordModel:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str = ""
    encrypted_password: str = ""
    url: Optional[str] = None
    created_at: dt = field(default_factory=dt.now)

    @classmethod
    def get_records(
        cls,
        file_path: str,
        name: Optional[str] = None,
        id: Optional[str] = None
    ) -> list[Any]:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                if isinstance(data, dict):
                    records = list(data.values())
                else:
                    records = data 
            if name and name.lower() != 'all':
                records = [record for record in records if name.lower() in record['name'].lower()]
        except (FileNotFoundError, JSONDecodeError):
            records = []
        return records
    
    @classmethod
    def get_password_index(cls, file_path: str, id: str) -> Optional[int]:
        records = cls.get_records(file_path=file_path)
        for index, record in enumerate(records):
            if record['id'] == id:
                return index
        return None

    @classmethod
    def delete(cls, file_path: str, id: str) -> bool:
        record_index = cls.get_password_index(file_path, id)
        records = cls.get_records(file_path=file_path)
        if record_index is None:
            return False
        try:
            del records[record_index]
            cls.write_to_file(file_path, records)
        except (FileNotFoundError, IndexError):
            return False
        return True

    @staticmethod
    def write_to_file(file_path: str, records: list[dict[str, Any]]) -> None:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(records, file, indent=2, ensure_ascii=False)

    def save(self, file_path) -> None:
        """Save new password record to the JSON file""" 

        password_data = asdict(self)
        password_data["created_at"] = dt.strftime(password_data["created_at"], '%H:%M %d/%m/%y')

        records = PasswordModel.get_records(file_path=file_path)

        records.append(password_data)

        self.write_to_file(file_path, records)
    
