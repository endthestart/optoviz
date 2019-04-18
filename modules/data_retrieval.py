def login_robinhood(path_to_credentials):
    from fast_arrow import Client
    credentials = open(path_to_credentials,'r').read()
    credentials = credentials.split("\n")
    client = Client(username=credentials[0],password=credentials[1])
    print(client.authenticate())
    return client

def retrieve_current_price(client,ticker):
    from fast_arrow import StockMarketdata
    stock = StockMarketdata.quote_by_symbol(client, ticker)
    stock_price = round((float(stock['ask_price']) + float(stock['bid_price']))/2,2)
    return stock_price
