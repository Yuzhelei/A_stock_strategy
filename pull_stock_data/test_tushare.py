# 导入tushare
import tushare as ts

# 初始化pro接口
pro = ts.pro_api('610de4f90e9ff349d90f86c38b9721d7a7cbf90cdeaecd30c56c7e16')

# 拉取数据
df = pro.daily(**{
    "ts_code": "000001.SZ",
    "trade_date": "",
    "start_date": 20180701,
    "end_date": 20180718,
    "offset": "",
    "limit": ""
}, fields=[
    "ts_code",
    "trade_date",
    "open",
    "high",
    "low",
    "close",
    "pre_close",
    "change",
    "pct_chg",
    "vol",
    "amount"
])
print(df)

