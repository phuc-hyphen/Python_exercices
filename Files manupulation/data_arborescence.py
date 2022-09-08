
import pandas as pnd

import numpy as np

df = pnd.read_excel("jira-xray-test-report.xlsx", sheet_name="Tests per Test Repository Path",
                    header=1)
new_index = list(df.columns.values[0:3])
df.set_index(new_index, inplace=True)
df.head()
pnd.set_option("display.max_rows", len(df.columns), "display.max_columns", len(df))