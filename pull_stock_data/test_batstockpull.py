from util.save_stock_data2Local import BaoStockConnection

if __name__ == "__main__":
    connect = BaoStockConnection("600036", "2023-08-01", "2023-08-31", "5")
    connect.download_data()
