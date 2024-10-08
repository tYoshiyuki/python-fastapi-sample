from app.models import Base
from app.db import engine

# テーブル作成
Base.metadata.create_all(bind=engine)