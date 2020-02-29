# 検証で利用するデータをまとめたもの

## タイタニック乗船客リスト

[データはここ](./data/titanic-passengers.csv)

### Redshift

**テーブル作成**

```sql
CREATE TABLE IF NOT EXISTS public.titanic
(
  passenger_id DECIMAL(4,0),
  survived BOOLEAN,
  pclass DECIMAL(2,0),
  name VARCHAR(100),
  sex VARCHAR(10),
  age DECIMAL(4,1),
  sib_sp DECIMAL(3,1),
  parch DECIMAL(3,1),
  ticket VARCHAR(20),
  fare DECIMAL(6,1),
  cabin VARCHAR(50),
  embarked VARCHAR(1),
  PRIMARY KEY (passenger_id)
)
DISTSTYLE EVEN
COMPOUND SORTKEY(passenger_id);
```

**データロード**

```sql
COPY public.titanic 
FROM 's3://<path-to-object>'
IAM_ROLE 'arn:aws:iam::<aws-account-id>:role/<role-name>'
REGION 'ap-northeast-1'
DELIMITER AS ';'
IGNOREHEADER AS 1;
```
