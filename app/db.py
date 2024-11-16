""" DB関連モジュール """

from sqlalchemy import create_engine, delete
from sqlmodel import SQLModel, Session

from app import models

SQLITE_FILE_NAME = "fastapi-sample.db"
sqlite_url = f"sqlite:///{SQLITE_FILE_NAME}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)


def create_db_and_tables():
    """DB・テーブルを作成する"""
    SQLModel.metadata.create_all(engine)


def get_session():
    """DBセッションを取得する"""
    with Session(engine) as session:
        yield session


def seed():
    """シードデータを投入する"""
    with Session(engine) as session:
        session.exec(delete(models.Hero))
        session.commit()

        session.add(models.Hero(id=101, name="One", age=11, secret_name="one"))
        session.add(models.Hero(id=102, name="Two", age=22, secret_name="two"))
        session.add(models.Hero(id=103, name="Three", age=33, secret_name="three"))
        session.commit()
