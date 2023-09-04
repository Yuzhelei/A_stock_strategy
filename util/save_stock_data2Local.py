import baostock as bs
import pandas as pd


class BaoStockConnection:
    def __init__(self, code, start_date, end_date, frequency):
        self.code = code
        self.start_date = start_date
        self.end_date = end_date
        self.frequency = frequency

    def download_data(self):
        lg = bs.login()
        if self.code[0] == '6':
            self.code = 'sh.' + self.code
        else:
            self.code = 'sz.' + self.code
        # 显示登陆返回信息
        print('login respond error_code:' + lg.error_code)
        print('login respond  error_msg:' + lg.error_msg)
        # 如果传入的是日，星期，月，取的字段不同
        if self.frequency in ['d', 'w', 'm']:
            fields = "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,isST"
        else:
            fields = "date,time,code,open,high,low,close,volume,amount,adjustflag"
        rs = bs.query_history_k_data_plus(self.code,
                                          fields,
                                          self.start_date,
                                          self.end_date,
                                          self.frequency,
                                          "2")
        df = pd.DataFrame(rs.data)
        df.columns = fields.split(",")
        if self.frequency not in ['d', 'w', 'm']:
            df['time'] = [t[:-3] for t in df['time']]
            df['time'] = pd.to_datetime(df['time'])
            df.rename(columns={'time': 'datetime'}, inplace=True)

            df = df.loc[:, ['datetime', 'code', 'open', 'high', 'low', 'close', 'volume', 'amount']]
            df.to_csv("E:\\stock_data\\%s\\%s.csv" % (self.frequency, self.code), index=False)
