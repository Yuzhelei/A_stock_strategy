from jqdatasdk import *

if __name__ == '__main__':
    auth('13335756885', 'Yzl1234567')
    count = get_query_count()
    print(count)

    # df = get_bars(normalize_code("002980"), 10000, unit='5m',
    #               fields=['date', 'open', 'close', 'high', 'low', 'volume', 'money'],
    #               include_now=False, end_dt='2022-01-08')
    #
    # address = "E:\\trade_data\\" + "002980" + ".xlsx"
    #
    # df.to_excel(address, sheet_name="test", index=False, header=True)

    # print(df)

    count = get_query_count()
    print(count)

