from time import sleep

import requests
from dateutil import parser
from datetime import datetime, time


def getTick(stock_code):
    if stock_code[0] == '6':
        prefix = 'sh'
    elif stock_code[0] == '0':
        prefix = 'sz'
    else:
        raise Exception("error code!")
    page = requests.get("https://qt.gtimg.cn/q=" + prefix + stock_code)
    stock_info = page.text
    stock_info = stock_info.split("~")
    op = float(stock_info[5])
    high = float(stock_info[3])
    low = float(stock_info[34])
    close = float(stock_info[5])
    trade_time = parser.parse(stock_info[30])
    return [trade_time, close]


if __name__ == "__main__":
    while True:
        code = '002364'
        dt, close = getTick(code)
        if dt.time() > time(15, 2):
            break
        sleep(3)
