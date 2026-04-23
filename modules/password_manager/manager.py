from uuid import UUID
from typing import Optional, Sequence

from sqlalchemy import select
from sqlalchemy.exc import NoResultFound

from .settings import Session
from .models import PasswordModel


def create_password():
    with Session() as session, session.begin():
        pass


def get_password(password_id: UUID) -> PasswordModel | None:
    with Session() as session:
        return session.get(PasswordModel, password_id)


def get_passwords_list(
    ordering_by: str = "name", name: Optional[str] = None
) -> Sequence[PasswordModel]:
    with Session() as session:
        if not name:
            return session.scalars(select(PasswordModel).order_by(ordering_by)).all()
        return session.scalars(
            select(PasswordModel)
            .where(PasswordModel.name.icontains(name))
            .order_by(ordering_by)
        ).all()


def update_password():
    pass


def delete_password(password_id: UUID) -> None:
    with Session() as session, session.begin():
        record = get_password(password_id)
        if not record:
            raise NoResultFound("Password not found")
        session.delete(record)
