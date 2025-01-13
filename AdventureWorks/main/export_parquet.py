import warnings

import pandas
import pyodbc


class ExportParquet:
    def __init__(self, server: str, database: str, port: int, user: str, password: str):
        self.connection_string = "".join(
            [
                "DRIVER={ODBC Driver 18 for SQL Server};",
                f"SERVER={server},{str(port)};",
                f"DATABASE={database};",
                f"UID={user};",
                f"PWD={password};",
                "TrustServerCertificate=yes;",
            ]
        )

    def export(self, query: str, output: str):
        with pyodbc.connect(self.connection_string) as conn:
            # NOTE: SQLServer のデータ型で、Pandas で代替できないものに対して、同時の変換関数を用意する
            # https://github.com/mkleehammer/pyodbc/wiki/Using-an-Output-Converter-function
            # https://github.com/mkleehammer/pyodbc/wiki/Connection#add_output_converter
            conn.add_output_converter(-151, self.convert)

            # NOTE: 上述の変換関数を利用したい場合、pyodbc から直接コネクションを作成する必要がある
            # 本来であれば、pandas 利用時には SQLAlchemy 経由で接続しないとならないため、以下の Warning が出力される
            # UserWarning: pandas only supports SQLAlchemy connectable (engine/connection) or database string URI or sqlite3 DBAPI2 connection. Other DBAPI2 objects are not tested. Please consider using SQLAlchemy.
            warnings.filterwarnings("ignore")

            # NOTE: 本来であれば、下記のような SQLAlchemy 経由でコネクションを作成する必要がある
            # from sqlalchemy import create_engine
            # from sqlalchemy.engine import URL
            # url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
            # conn = create_engine(url=url, ignore_no_transaction_on_rollback=True)

            df = pandas.read_sql(query, conn)  # type: ignore

        # NOTE: デフォルト設定で Parquet ファイルを作成すると、BigQueryロード時に正しくデータ型を拾ってくれない箇所があるため、coerce_timestamps の設定を入れる
        # https://stackoverflow.com/questions/64038537/how-to-control-timestamp-schema-in-pandas-to-parquet
        df.to_parquet(path=output, engine="pyarrow", coerce_timestamps="ms")

    @staticmethod
    def convert(value: bytes) -> str:
        return value.hex()
