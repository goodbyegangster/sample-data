# AdventureWorks サンプル データベース

## 動作確認環境

- Windows 11 Pro
  - SQL Server Express 2022
- WSL2
  - Ubuntu 22.04
- Python 3.13
  - [ライブラリ](./pyproject.toml)

## SQLServer Express の設定

- SQL Server Express インストールモジュール
  - [Microsoft SQL Server 2022 Express](https://www.microsoft.com/ja-jp/download/details.aspx?id=104781)
- AdventureWorks サンプル データベースのリストア手順
  - [AdventureWorks サンプル データベース](https://learn.microsoft.com/ja-jp/sql/samples/adventureworks-install-configure?view=sql-server-ver16&tabs=ssms)
    - AdventureWorks 2022 OLTP 系
- `SQL Server 認証モードと Windows 認証モード` に設定変更
  - [サーバーの認証モードの変更](https://learn.microsoft.com/ja-jp/sql/database-engine/configure-windows/change-server-authentication-mode?view=sql-server-ver16&tabs=ssms)
- 利用ポートを静的ポートに変更
  - [SQL Server が特定の TCP ポートでリッスンするように構成する](https://learn.microsoft.com/ja-jp/sql/database-engine/configure-windows/configure-a-server-to-listen-on-a-specific-tcp-port?view=sql-server-ver16)

## WSL 側の設定

- SQL Server 向けの ODBC ドライバーのインストールモジュール
  - [Install the Microsoft ODBC driver for SQL Server (Linux)](https://learn.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver16&tabs=ubuntu18-install%2Calpine17-install%2Cdebian8-install%2Credhat7-13-install%2Crhel7-offline)
- `sqlcmd` および `bcp` コマンドをインストール
  - [Linux に SQL Server コマンドライン ツール sqlcmd および bcp をインストールする](https://learn.microsoft.com/ja-jp/sql/linux/sql-server-linux-setup-tools?view=sql-server-ver16&tabs=redhat-install)

## Python プログラム

### config.toml を作成

`config.toml.sample` より `config.toml` を作成する。

### 実行コマンド

```sh
source .venv/bin/activate
python -m main.main
```
