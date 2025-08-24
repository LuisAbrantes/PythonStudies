from pytrends.request import TrendReq
from prophet import Prophet
import pandas as pd
import matplotlib.pyplot as plt

pytrends = TrendReq(hl='pt-BR', tz=360)
pytrends.build_payload(["academia"], timeframe="2018-01-01 2023-12-31", geo="BR")
data = pytrends.interest_over_time()

df = data.reset_index()[["date","academia"]]
df.columns = ["ds","y"]

model = Prophet()
model.fit(df)

future = model.make_future_dataframe(periods=180)  # 6 meses
forecast = model.predict(future)

model.plot(forecast)
plt.show()


print(data.head())
