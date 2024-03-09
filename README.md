# sample-data

## タイタニック乗船客リスト

[タイタニック乗船客リスト](./titanic-passengers/)

## AWS Cloud Front サンプル・ログ

> s3://athena-examples-ap-northeast-1/cloudfront

- テキスト
- 時系列
- 半構造化

```sh
$ aws s3 ls --recursive --human-readable s3://athena-examples-ap-northeast-1/cloudfront
2017-05-08 12:57:46  198.3 KiB cloudfront/plaintext/log1
2017-05-08 12:57:46  198.7 KiB cloudfront/plaintext/log2
2017-05-08 12:57:46   98.9 KiB cloudfront/plaintext/log3
2017-05-08 12:57:46   99.4 KiB cloudfront/plaintext/log4
2017-05-08 12:57:46  198.9 KiB cloudfront/plaintext/log5
2017-05-08 12:57:46  198.7 KiB cloudfront/plaintext/log6
```

```sh
$ aws s3 cp s3://athena-examples-ap-northeast-1/cloudfront/plaintext/log1 - | cat | head -n 3
2014-07-05      20:00:00        LHR3    4260    10.0.0.15       GET     eabcd12345678.cloudfront.net    /test-image-1.jpeg      200     -       Mozilla/5.0%20(MacOS;%20U;%20Windows%20NT%205.1;%20en-US;%20rv:1.9.0.9)%20Gecko/2009040821%20IE/3.0.9
2014-07-05      20:00:00        MIA3    10      10.0.0.15       GET     eabcd12345678.cloudfront.net    /test-image-1.jpeg      304     -       Mozilla/5.0%20(Linux;%20U;%20Windows%20NT%205.1;%20en-US;%20rv:1.9.0.9)%20Gecko/2009040821%20Chrome/3.0.9
2014-07-05      20:00:00        MIA3    4252    10.0.0.15       GET     eabcd12345678.cloudfront.net    /test-image-3.jpeg      200     -       Mozilla/5.0%20(Android;%20U;%20Windows%20NT%205.1;%20en-US;%20rv:1.9.0.9)%20Gecko/2009040821%20Opera/3.0.9
```

## Shopping Queries Dataset: A Large-Scale ESCI Benchmark for Improving Product Search

[Shopping Queries Dataset: A Large-Scale ESCI Benchmark for Improving Product Search](https://github.com/amazon-science/esci-data)

> We introduce the “Shopping Queries Data Set”, a large dataset of difficult search queries, released with the aim of fostering research in the area of semantic matching of queries and products. For each query, the dataset provides a list of up to 40 potentially relevant results, together with ESCI relevance judgements (Exact, Substitute, Complement, Irrelevant) indicating the relevance of the product to the query. Each query-product pair is accompanied by additional information. The dataset is multilingual, as it contains queries in English, Japanese, and Spanish.

> クエリと商品のセマンティックマッチング分野の研究を促進する目的で公開された、困難な検索クエリの大規模なデータセットである「ショッピングクエリデータセット」を紹介する。各クエリに対して、このデータセットは最大 40 の関連しそうな結果のリストと、クエリと商品の関連性を示す ESCI 関連性判定（Exact、Substitute、Complement、Irelevant）を提供する。各クエリと商品のペアには追加情報が添えられている。データセットは多言語であり、英語、日本語、スペイン語のクエリを含む。

- [dataset](https://github.com/amazon-science/esci-data/tree/main/shopping_queries_dataset)
  - shopping_queries_dataset_examples.parquet
    - Parquet
  - shopping_queries_dataset_products.parquet
    - Parquet
    - 1GB
  - shopping_queries_dataset_sources.csv
    - CSV

カラムの情報は [Usage](https://github.com/amazon-science/esci-data?tab=readme-ov-file#usage) を確認すること

## New York City Taxi and Limousine Commission (TLC) Trip Record Data

> s3://nyc-tlc/trip data/

[The AWS Open Data Sponsorship Program: New York City Taxi and Limousine Commission (TLC) Trip Record Data](https://aws.amazon.com/marketplace/pp/prodview-okyonroqg5b2u#resources)

- parquet
- 時系列

> 黄色と緑色のタクシーの乗車記録には、乗車および降車の日付/時刻、乗車および降車の場所、移動距離、項目別の運賃、料金タイプ、支払いタイプ、運転手が報告した乗客数を記録するフィールドが含まれます

> レンタル車両 (「FHV」) の走行記録には、配車ベースのライセンス番号、ピックアップの日付、時刻、タクシー ゾーンの場所 ID をキャプチャするフィールドが含まれます

```sh
$ aws s3 ls --human-readable 's3://nyc-tlc/trip data/' | grep 2023-01.parquet
2023-03-21 07:23:31   10.8 MiB fhv_tripdata_2023-01.parquet
2023-03-21 07:23:30  451.9 MiB fhvhv_tripdata_2023-01.parquet
2023-03-21 07:23:33    1.4 MiB green_tripdata_2023-01.parquet
2023-03-21 07:23:30   45.5 MiB yellow_tripdata_2023-01.parquet
```

カラムの情報は、[データ提供元（NYC.gov）サイト](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) の `Data Dictionaries and MetaData` にある PDF ファイルを参照すること。
