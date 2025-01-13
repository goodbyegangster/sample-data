import os

import tomllib

from main.export_parquet import ExportParquet
from main.load_parquet import LoadParquet
from main.upload_parquet import UploadParquet

TARGETS = [
    "HumanResources.Department",
    "HumanResources.Employee",
    "HumanResources.EmployeeDepartmentHistory",
    "HumanResources.EmployeePayHistory",
    "HumanResources.JobCandidate",
    "HumanResources.Shift",
    "Person.Address",
    "Person.AddressType",
    "Person.BusinessEntity",
    "Person.BusinessEntityAddress",
    "Person.BusinessEntityContact",
    "Person.ContactType",
    "Person.CountryRegion",
    "Person.EmailAddress",
    "Person.Password",
    "Person.Person",
    "Person.PersonPhone",
    "Person.PhoneNumberType",
    "Person.StateProvince",
    "Production.BillOfMaterials",
    "Production.Culture",
    "Production.Document",
    "Production.Illustration",
    "Production.Location",
    "Production.Product",
    "Production.ProductCategory",
    "Production.ProductCostHistory",
    "Production.ProductDescription",
    "Production.ProductDocument",
    "Production.ProductInventory",
    "Production.ProductListPriceHistory",
    "Production.ProductModel",
    "Production.ProductModelIllustration",
    "Production.ProductModelProductDescriptionCulture",
    "Production.ProductPhoto",
    "Production.ProductProductPhoto",
    "Production.ProductReview",
    "Production.ProductSubcategory",
    "Production.ScrapReason",
    "Production.TransactionHistory",
    "Production.TransactionHistoryArchive",
    "Production.UnitMeasure",
    "Production.WorkOrder",
    "Production.WorkOrderRouting",
    "Purchasing.ProductVendor",
    "Purchasing.PurchaseOrderDetail",
    "Purchasing.PurchaseOrderHeader",
    "Purchasing.ShipMethod",
    "Purchasing.Vendor",
    "Sales.CountryRegionCurrency",
    "Sales.CreditCard",
    "Sales.Currency",
    "Sales.CurrencyRate",
    "Sales.Customer",
    "Sales.PersonCreditCard",
    "Sales.SalesOrderDetail",
    "Sales.SalesOrderHeader",
    "Sales.SalesOrderHeaderSalesReason",
    "Sales.SalesPerson",
    "Sales.SalesPersonQuotaHistory",
    "Sales.SalesReason",
    "Sales.SalesTaxRate",
    "Sales.SalesTerritory",
    "Sales.SalesTerritoryHistory",
    "Sales.ShoppingCartItem",
    "Sales.SpecialOffer",
    "Sales.SpecialOfferProduct",
    "Sales.Store",
]


def migration():
    config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../config.toml")
    with open(config_file, "r") as f:
        config = tomllib.loads(f.read())

    ep = ExportParquet(
        server=config["SQLServer"]["SERVER"],
        database=config["SQLServer"]["DATABASE"],
        port=config["SQLServer"]["PORT"],
        user=config["SQLServer"]["USER"],
        password=config["SQLServer"]["PASSWORD"],
    )

    up = UploadParquet(bucket=config["GCS"]["BUCKET"])

    lp = LoadParquet(project=config["BIGQUERY"]["PROJECT"], region=config["BIGQUERY"]["REGION"])

    for target in TARGETS:
        schema = target.split(".")[0].lower()
        table = target.split(".")[1].lower()

        output_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"../outputs/{schema}/{table}")
        os.makedirs(os.path.dirname(output_file), exist_ok=True)

        ep.export(query=f"select * from {target}", output=output_file)
        up.upload(source=output_file, target=f"parquet/{schema}/{table}.parquet")
        lp.load(gcs=f"gs://{config['GCS']['BUCKET']}/parquet/{schema}/{table}.parquet", schema=schema, table=table)


def main():
    migration()


if __name__ == "__main__":
    main()
