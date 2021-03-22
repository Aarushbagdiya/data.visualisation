import pandas as pd

import plotly.express as px

df = pd.read_csv("line_chart.csv")

fig = px.line(df, x="country", y="cases", color="Country", title='covid cases')

fig.show()