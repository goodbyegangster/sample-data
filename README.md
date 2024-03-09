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

## リスティング広告のインプレッション・ログ

> s3://elasticmapreduce/samples/hive-ads/tables/impressions

- hive パーティション
- 半構造化
- JSONL
- 時系列

```sh
$ aws s3 --profile cdk-individual ls s3://elasticmapreduce/samples/hive-ads/tables/impressions/ | head -n 5
                           PRE dt=2009-04-12-13-00/
                           PRE dt=2009-04-12-13-05/
                           PRE dt=2009-04-12-13-10/
                           PRE dt=2009-04-12-13-15/
                           PRE dt=2009-04-12-13-20/
```

```json
$ aws s3 cp s3://elasticmapreduce/samples/hive-ads/tables/impressions/dt=2009-04-14-13-00/ec2-0-51-75-39.amazon.com-2009-04-14-13-00.log - | head -
n 3
{"number": "67714", "referrer": "barnesandnoble.com", "processId": "1731", "adId": "jHbQTXDanFeH35aWABcv8ojPmGWi3P", "browserCookie": "jierghcdpw", "userCookie": "ijQ5rO83dpwe3IJQPAfhOO9hhN4qPA", "requestEndTime": "1239714065000", "impressionId": "ujWT6KxNd4l4AC2IwcCouFciah5bHS", "userAgent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1) Gecko/20090624 Firefox/3.5", "timers": {"modelLookup":"0.3242","requestTime":"0.9436"}, "threadId": "34", "ip": "49.175.133.253", "modelId": "bxxiuxduad", "hostname": "ec2-0-51-75-39.amazon.com", "sessionId": "qPw4Jnvm0sgTxwth4RtqndSBbnuGDH", "requestBeginTime": "1239714064000"}
{"number": "92579", "referrer": "coursera.org", "processId": "1065", "adId": "k1QLH7LTw84LgVCiqJI2f0UmnE85CG", "browserCookie": "bhqcuhghei", "userCookie": "qJ8qKu8Oh5QLeBQsmr4GbFIEmuAF83", "requestEndTime": "1239714064000", "impressionId": "4gwUbsdduFM1eogBVttg110IUsJGnK", "userAgent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.20) Gecko/20081217 Firefox/2.0.0.20", "timers": {"modelLookup":"0.2968","requestTime":"0.9222"}, "threadId": "81", "ip": "52.144.233.240", "modelId": "bxxiuxduad", "hostname": "ec2-0-51-75-39.amazon.com", "sessionId": "GDnUUwcWed7EVDKQohvOd7DXUBVLvt", "requestBeginTime": "1239714063000"}
{"number": "117696", "referrer": "lastwordonnothing.com", "processId": "1359", "adId": "VwDSV7xmA2Ns6CSOf3KDBKBlRVNGjl", "browserCookie": "kfrcxtpooj", "userCookie": "Uk6rKHDXWoRDuqjC0KbSo02tKiKQUs", "requestEndTime": "1239714063000", "impressionId": "XC4oxemubWvG0LVV0FCNwgLqGfBhvm", "userAgent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; InfoPath.1;", "timers": {"modelLookup":"0.3824","requestTime":"0.7426"}, "threadId": "64", "ip": "52.172.179.99", "modelId": "bxxiuxduad", "hostname": "ec2-0-51-75-39.amazon.com", "sessionId": "vhwAi3xxnvp3ViaVKVch6BcqbiLfX3", "requestBeginTime": "1239714062000"}
```
