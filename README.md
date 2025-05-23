# Hello World Python Project

## 概要

このプロジェクトは、パッケージ管理に`uv`、リンティングとフォーマットに`ruff`、テストに`pytest`を使用した基本的なPythonのセットアップを示しています。メインスクリプトは "hello world"メッセージを出力します。このプロジェクトは、最新のPython開発ワークフローのテンプレートとして機能します。

## 前提条件

-   **Python**: Python 3.12+ を推奨します (このプロジェクトは Python 3.12 でセットアップされました)。
-   **`uv`**: Rustで書かれた高速なPythonパッケージインストーラーおよびリゾルバーです。もし持っていなければ、pip経由でインストールできます: `pip install uv`。

## セットアップ手順

1.  **リポジトリをクローンする** (まだの場合):
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **仮想環境の作成/有効化と依存関係のインストール**:

    このプロジェクトは `uv` を使用するように設定されています。 virtual environment は理想的には `uv` によって作成および管理されるべきです。

    ```bash
    # Python 3.12 を使用して .venv という名前の virtual environment を作成します (まだ存在しない場合)
    # `uv init` を使用して開始した場合、これは実行されているか、.python-version ファイルが作成されている可能性があります。
    # 特定のPythonバージョンでセットアップされていることを明示的に作成または確認するには:
    uv venv .venv --python 3.12 

    # virtual environment を有効化します
    # macOS/Linux の場合:
    source .venv/bin/activate
    # Windows (Git Bash または WSL) の場合:
    # source .venv/Scripts/activate
    # Windows (コマンドプロンプト) の場合:
    # .venv\Scripts\activate.bat
    # Windows (PowerShell) の場合:
    # .venv\Scripts\Activate.ps1
    ```

    virtual environment が有効化されたら、`uv` を使用して dependencies (開発ツールである `pytest` や `ruff` を含む) をインストールします:

    ```bash
    # pyproject.toml で定義された dependencies をインストールします ('dev' extras を含む)
    uv pip install .[dev]
    ```
    このコマンドは、`pyproject.toml` ファイルの `[project.dependencies]` および `[project.optional-dependencies.dev]` の下にリストされているすべての dependencies をインストールします。

## コードの実行方法

virtual environment が有効化されていることを確認してください。

メインアプリケーションを実行するには:
```bash
python main.py
```
または、virtual environment の Python インタープリタを明示的に使用するには:
```bash
.venv/bin/python main.py
```
これにより `main.py` が実行され、コンソールに "hello world" と出力されます。

## テストの実行方法

virtual environment が有効化され、development dependencies (例えば `pytest`) がインストールされていることを確認してください。

テストスイートを実行するには:
```bash
pytest
```
または、virtual environment の Python インタープリタを明示的に使用して `pytest` をモジュールとして実行するには:
```bash
.venv/bin/python -m pytest
```
これにより、`tests` ディレクトリに定義されているすべてのテストが検出され、実行されます。

## リンター/フォーマッターの実行方法

virtual environment が有効化され、development dependencies (例えば `ruff`) がインストールされていることを確認してください。

**リンティングの問題を確認する:**
```bash
ruff check .
```
または、明示的に:
```bash
.venv/bin/python -m ruff check .
```

**ファイルを自動的にフォーマットする:**
```bash
ruff format .
```
または、明示的に:
```bash
.venv/bin/python -m ruff format .
```
これにより、`pyproject.toml`（`[tool.ruff]` の下）で定義されたルールに従ってコードがフォーマットされます。

---

このREADMEは、プロジェクトを起動し、統合された開発ツールを利用するための基本的な手順を提供します。
