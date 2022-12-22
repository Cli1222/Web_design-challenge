import pandas as pd

pd.read_csv("cities.csv",index_col=0).to_html('data.html')