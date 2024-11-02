# python-fastapi-sample
Windows環境で構築する Python + FastAPI + pytest のサンプル

## Feature
- Python 3.12
- FastAPI
- pytest
- SQLite
- Windows
- Visual Studio Code
- Azure DevOps

## Settings
- venv、及び SQLite を初期設定します。
    - SQLite は、プロジェクトルート > `fastapi-sample.db` になります。
    - venv は、プロジェクト > `.venv` になります。

```ps1
PS > .\init.ps1
```

## Debug
- Visual Studio Code > 実行とデバッグ より実行します。
    - `http://127.0.0.1:8000/docs` にアクセスすると Swagger UI が表示されます。

## Test
- pytest による単体テストの実行、カバレッジの取得を行います。
    - テスト結果は、プロジェクトルート > `test_result` に出力します。

```ps1
PS > .\test.ps1
```

- ↓ カバレッジレポートのイメージ

![Test1](image/test001.jpg)

![Test2](image/test002.jpg)

- Visual Studio Code > テスト より実行することも出来ます。

![Test3](image/test003.jpg)

## PipeLine (Azure DevOps)
- `azure-pipelines.yml` を Azure DevOps で PipeLine に登録します。

- ↓ Azure DevOps のテスト結果、カバレッジレポートのイメージ

![PipeLine1](image/pipeline001.jpg)

![PipeLine2](image/pipeline002.jpg)
