import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

bucket = "Crypto"
#verify = False
org = "Cislunar Explorers"
token = "r6thR1yHPAJmLQieJLmrismcCirJvIlplkZe9fPMOR6w2dEyVFGHSZ3V1Zd1BSPKkJNr5PnHArSjDYhMf1wUUA=="
# Store the URL of your InfluxDB instance
url = "https://us-east-1-1.aws.cloud2.influxdata.com"

client = influxdb_client.InfluxDBClient(
    url=url,
    token=token,
    org=org
)

# Query script
query_api = client.query_api()
query = 'from(bucket:"Crypto")\
|> range(start: -30d)\
|> filter(fn:(r) => r._measurement == "coindesk")\
|> filter(fn:(r) => r._field == "price")\
|> filter(fn:(r) => r.code == "USD")\
|> filter(fn:(r) => r._value > 20000 )'
result = query_api.query(org=org, query=query)
results = []
for table in result:
    for record in table.records:
        results.append((record.get_field(), record.get_value()))

print(results)
