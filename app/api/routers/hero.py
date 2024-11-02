""" Hero エンドポイントのモジュール """
from typing import Annotated
from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from app.db import get_session
from app.models import Hero

router = APIRouter()

SessionDep = Annotated[Session, Depends(get_session)]


@router.get("/hero", tags=["hero"])
async def hero(session: SessionDep):
    """ Heroを取得する """
    return session.exec(select(Hero)).all()
