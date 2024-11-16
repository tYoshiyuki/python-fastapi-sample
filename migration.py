from app.db import create_db_and_tables, seed

# テーブル作成
create_db_and_tables()

# 初期データ投入
seed()
