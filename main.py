import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

YOUR_CSV_FILE: str = ""
OUTPUT_NAME: str = "output.parquet"

df = pd.read_csv(YOUR_CSV_FILE)
table = pa.Table.from_pandas(df)
pq.write_table(table, OUTPUT_NAME)
