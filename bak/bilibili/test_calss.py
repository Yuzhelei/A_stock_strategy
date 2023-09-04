from time import sleep
from datetime import datetime, time, timedelta
import requests
import pandas as pd


class astocktrading(object):
    def __init__(self, strategy_name):
        self.strategy_name = strategy_name
        self.Dt = []
        self.Open = []
        self.High = []
        self.Low = []
        self.Close = []
        self.Volume = []
        self.tick = []
        self.last_bar_start_minute = None
        self.ma20 = None
        self.isNewBar = False
        self.orderNumbers = 0
        self.current_orders = {}
        self.history_orders = {}

    def getTick(self):
        page = requests.get("http://hq.sinajs.cn/format=text&list=sh600519")
        stock_info = page.text
        mt_info = stock_info.split(",")
        last = float(mt_info[1])
        trade_datetime = mt_info[30] + ' ' + mt_info[31]
        self.tick = (trade_datetime, last)

    def get_history_data_from_local_machine(self):
        self.Open = [1, 2, 3]
        self.High = [2, 3, 4]
        return 1

    def bar_generator(self):
        # 创建新bar
        if self.tick[0].minute % 5 == 0 and \
                self.tick[0].minute != self.last_bar_start_minute:
            self.Open.insert(0, self.tick[1])
            self.High.insert(0, self.tick[1])
            self.Low.insert(0, self.tick[1])
            self.Close.insert(0, self.tick[1])
            self.Dt.insert(0, self.tick[0])

            self.isNewBar = True
        # 更新bar1
        else:
            self.High[0] = max(self.High[0], self.tick[1])
            self.Low[0] = min(self.High[0], self.tick[1])
            self.Close[0] = self.tick[1]
            self.Dt[0] = self.tick[0]

            self.isNewBar = False

    def strategy(self):
        if self.isNewBar:
            sum_ = 0
            for item in self.Close[1:21]:
                sum_ = sum_ + item
            self.ma20 = sum_ / 20

        if 0 == len(self.current_orders):
            if self.Close[0] < 0.95 * self.ma20:
                volume = int(1000000 / self._Close[0] / 100) * 100
                self.buy(self._Close[0] + 0.01, volume)
        elif 1 == len(self.current_orders):
            if self.Close[0] > self.ma20 * 1.05:
                key = self.current_orders.keys()[0]
                self.sell(key, self._Close[0] - 0.01)
        else:
            raise ValueError("we have more than 1 orders!")

    def buy(self, price, volume):
        self.orderNumbers += 1
        key = "order" + str(self.orderNumbers)
        self.current_orders[key] = {
            "open_datetime": self.Dt[0],
            "open_price": price,
            "volume": volume
        }

    def sell(self, key, price):
        self.current_orders[key]['close_price'] = price
        self.current_orders[key]['close_datetime'] = self.Dt[0]
        self.history_orders = self.current_orders.pop(key)


def string_toDatetime(st):
    return datetime.datetime.strptime(st, "%Y-%m-%d %H:%M:%S")


ast = astocktrading('ma')
ast.get_history_data_from_local_machine()
while time(9, 26) < datetime.now().time() < time(11, 32) or \
        time(13) < datetime.now().time() < time(15, 2):
    ast.getTick()
    ast.bar_generator()
    ast.strategy()
    sleep(3)
