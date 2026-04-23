from typing import Optional, Sequence, Any

from sqlalchemy import func
from sqlalchemy import select, update
from sqlalchemy.exc import NoResultFound

from .settings import Session
from .models import PasswordModel


def create_password(password_data: dict[str, Any]) -> None:
    with Session() as session, session.begin():
        new_record = PasswordModel(**password_data)
        session.add(new_record)


def get_password(password_id: str) -> PasswordModel | None:
    with Session() as session:
        return session.get(PasswordModel, password_id)


def get_passwords_list(
    ordering_by: str = "name", name: Optional[str] = None
) -> Sequence[PasswordModel]:
    with Session() as session:
        order_column = getattr(PasswordModel, ordering_by, PasswordModel.name)
        if not name:
            return session.scalars(select(PasswordModel).order_by(order_column)).all()
        return session.scalars(
            select(PasswordModel)
            .where(func.lower(PasswordModel.name).contains(name.lower()))
            .order_by(order_column)
        ).all()


def update_password(to_update: dict[str, Any]) -> None:
    with Session() as session, session.begin():
        data = to_update.copy()
        record_id = data.pop("id")

        session.execute(
            update(PasswordModel)
            .where(PasswordModel.id == record_id)
            .values(**data)
        )


def delete_password(password_id: str) -> None:
    with Session() as session, session.begin():
        record = session.get(PasswordModel, password_id)
        if not record:
            raise NoResultFound("Password not found")
        session.delete(record)
