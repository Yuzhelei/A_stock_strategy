import os.path
from datetime import datetime

import pandas as pd
import numpy as np
from datetime import datetime, time, timedelta
from test_calss import string_toDatetime
from dateutil import parser

bar_5m = pd.read_excel('E:\\trade_data\\002980.xlsx')
bar_5m.head(5)
bar_5m.tail(5)

ticks = []
for index, row in bar_5m.head(5).iterrows():
    if row['open'] < 30:
        step = 0.01
    elif row['open'] < 60:
        step = 0.02
    elif row['open'] < 90:
        step = 0.03
    else:
        step = 0.05

    arr = np.arange(row['open'], row['high'], step)
    arr = np.append(arr, row['high'])
    arr = np.append(arr, np.arange(row['open'] - step, row['low'], -step))
    arr = np.append(arr, row['low'])
    arr = np.append(arr, row['close'])

    i = 0
    dt = row['date'] - timedelta(minutes=5)
    for item in arr:
        ticks.append((dt + timedelta(seconds=0.1 * i), item))
        i += 1
ticks_df = pd.DataFrame(ticks, columns=['datetime', 'price'])
# 保存ticks_df
tick_path = 'E:\\trade_data\\ticks\\002980_ticks.xlsx'
# if os.path.exists(tick_path):
ticks_df.to_excel(tick_path, sheet_name="ticks", index=False, header=True)
