def list_average(lst):
    """Returns average of a list"""
    return sum(lst)/len(lst)

# BC - Bought call
def BC_revenue_calc(security_price_on_exp,strike_price,contract_cost_per_share,num_contracts):
    """Return the revenue (may be positive or negative) given total information on a "bought call" \n
    transaction.\n\n
    security_price_on_exp: refers to the price of the security on expiration of the contract \n\n
    strike_price: refers to the strike price (duh) \n\n
    contract_cost_per_share: refers to the contract cost for 1 share in a contract. For example, \n
    if the contract_cost_per_share is 10 cents, then the cost for one contract is 10 dollars. \n
    $0.10 x 100 shares/contract. \n\n
    num_contracts: refers to the number of contracts purchased"""
    # Calculating total cost to the option purchaser
    cost = contract_cost_per_share * 100 * num_contracts
    # If the security price on expiry minus the strike price, times 100, times the number of contracts purchased
    # (this is your hypothetical profit), is less than 0, you wouldn't exercise, as you would just lose money.
    # So instead, you just lose the amount of option premium you spent (-cost)
    if ((security_price_on_exp - strike_price) * 100 * num_contracts) <= 0:
        return -cost
    # Otherwise, if the security price on expiry minus the strike price times 100, times the number of contracts,
    # rounded IS greater than zero, of course you would exercise, and you would get that, minus the cost back
    # in revenue
    else:
        return round(((security_price_on_exp - strike_price) * 100 * num_contracts),2)-cost

# BP - Bought put
def BP_revenue_calc(security_price_on_exp,strike_price,contract_cost_per_share,num_contracts):
    """Return the revenue (may be positive or negative) given total information on a "bought call" \n
    transaction.\n\n
    security_price_on_exp: refers to the price of the security on expiration of the contract \n\n
    strike_price: refers to the strike price (duh) \n\n
    contract_cost_per_share: refers to the contract cost for 1 share in a contract. For example, \n
    if the contract_cost_per_share is 10 cents, then the cost for one contract is 10 dollars. \n
    $0.10 x 100 shares/contract. \n\n
    num_contracts: refers to the number of contracts purchased"""
    cost = contract_cost_per_share * 100 * num_contracts
    if ((security_price_on_exp - strike_price) * 100 * num_contracts) >= 0:
        return -cost
    else:
        return round(((strike_price - security_price_on_exp) * 100 * num_contracts),2)-cost

# SC - Sold call
def SC_revenue_calc(security_price_on_exp,strike_price,contract_cost_per_share,num_contracts):
    """Return the revenue (may be positive or negative) given total information on a "bought call" \n
    transaction.\n\n
    security_price_on_exp: refers to the price of the security on expiration of the contract \n\n
    strike_price: refers to the strike price (duh) \n\n
    contract_cost_per_share: refers to the contract cost for 1 share in a contract. For example, \n
    if the contract_cost_per_share is 10 cents, then the cost for one contract is 10 dollars. \n
    $0.10 x 100 shares/contract. \n\n
    num_contracts: refers to the number of contracts purchased"""
    cost = contract_cost_per_share * 100 * num_contracts
    if ((security_price_on_exp - strike_price) * 100 * num_contracts) >= 0:
        return round(((strike_price - security_price_on_exp) * 100 * num_contracts),2)+cost
    else:
        return cost

# SP - Sold put
def SP_revenue_calc(security_price_on_exp,strike_price,contract_cost_per_share,num_contracts):
    """Return the revenue (may be positive or negative) given total information on a "bought call" \n
    transaction.\n\n
    security_price_on_exp: refers to the price of the security on expiration of the contract \n\n
    strike_price: refers to the strike price (duh) \n\n
    contract_cost_per_share: refers to the contract cost for 1 share in a contract. For example, \n
    if the contract_cost_per_share is 10 cents, then the cost for one contract is 10 dollars. \n
    $0.10 x 100 shares/contract. \n\n
    num_contracts: refers to the number of contracts purchased"""
    cost = contract_cost_per_share * 100 * num_contracts
    if ((security_price_on_exp - strike_price) * 100 * num_contracts) <= 0:
        return round(((security_price_on_exp-strike_price) * 100 * num_contracts),2)+cost
    else:
        return cost

def long_revenue_calc(security_price_bought,security_price_sold,number_shares):
    """Calculates the profit from a long buy of stock given the initial price bought at,
    the final price sold at, and the number of shares"""
    return (security_price_sold - security_price_bought) * number_shares

def short_revenue_calc(security_price_sold,security_price_bought,number_shares):
    """Calculates the profit from a short sale of stock given the initial price sold at,
    the final price (re)bought at, and the number of shares"""
    return (security_price_sold - security_price_bought) * number_shares

def visualization_center_func(holdings_chart):
    """Gets the average strike price of all the contracts in a contract chart"""
    # Getting the average strike prices to determine center of visualization
    import pandas as pd
    import numpy as np
    call_count = holdings_chart.count()['calls']
    put_count = holdings_chart.count()['puts']
    stock_count = holdings_chart.count()['stock']
    if call_count > 0:
        call_strike_price_list = []
        for i in range(call_count):
            call_strike_price_list.append(holdings_chart['calls'][i]['strike_price'])
    if put_count > 0:
        put_strike_price_list = []
        for i in range(put_count):
            put_strike_price_list.append(holdings_chart['puts'][i]['strike_price'])
    if stock_count > 0:
        stock_price_list = []
        for i in range(stock_count):
            stock_price_list.append(holdings_chart['stock'][i]['price_at_ps'])
    if call_count > 0:
        call_strike_price_average = list_average(call_strike_price_list)
    else:
        pass
    if put_count > 0:
        put_strike_price_average = list_average(put_strike_price_list)
    else:
        pass
    if stock_count > 0:
        stock_price_average = list_average(stock_price_list)
    else:
        pass
    if (call_count > 0) and (put_count > 0):
        strike_price_average = (call_strike_price_average + put_strike_price_average)/2
    elif (call_count > 0) and (put_count == 0):
        strike_price_average = call_strike_price_average
    elif (call_count == 0) and (put_count > 0):
        strike_price_average = put_strike_price_average
    else:
        return stock_price_average
    return strike_price_average

def total_entrance_cost_func(holdings_chart):
    """Returns the total cost of all the contracts in a contract chart"""
    # Getting total contract cost to determine total initial cost for visualization
    import pandas as pd
    import numpy as np
    prices = [np.nan]
    revenue_chart = pd.DataFrame(prices)
    revenue_chart.columns = ['price']
    call_count = holdings_chart.count()['calls']
    put_count = holdings_chart.count()['puts']
    stock_count = holdings_chart.count()['stock']

    for i in range(call_count):
        if holdings_chart['calls'][i]['type'] == 'bought':
            lst = []
            BC_cost = holdings_chart['calls'][i]['contract_cost_per_share']*100
            lst.append(BC_cost)
            revenue_chart['BC_' + str(i)] = pd.Series(lst)
        elif holdings_chart['calls'][i]['type'] == 'sold':
            lst = []
            SC_cost = holdings_chart['calls'][i]['contract_cost_per_share']*-100
            lst.append(SC_cost)
            revenue_chart['SC_' + str(i)] = pd.Series(lst)

    for i in range(put_count):
        if holdings_chart['puts'][i]['type'] == 'bought':
            lst = []
            BP_cost = holdings_chart['puts'][i]['contract_cost_per_share']*100
            lst.append(BP_cost)
            revenue_chart['BP_' + str(i)] = pd.Series(lst)
        elif holdings_chart['puts'][i]['type'] == 'sold':
            lst = []
            SP_cost = holdings_chart['calls'][i]['contract_cost_per_share']*-100
            lst.append(SP_cost)
            revenue_chart['SP_' + str(i)] = pd.Series(lst)

    for i in range(stock_count):
        if holdings_chart['stock'][i]['type'] == 'long':
            long_price_bought = holdings_chart['stock'][i]['price_at_ps']
            long_num_shares = holdings_chart['stock'][i]['num_shares']
            long_stock_cost = long_price_bought*long_num_shares
            lst = []
            lst.append(long_stock_cost)
            # LS - Long stock
            revenue_chart['LS_' + str(i)] = pd.Series(lst)
        elif holdings_chart['stock'][i]['type'] == 'short':
            short_price_sold = holdings_chart['stock'][i]['price_at_ps']
            short_num_shares = holdings_chart['stock'][i]['num_shares']
            short_stock_cost = short_price_sold*short_num_shares*-1
            lst = []
            lst.append(short_stock_cost)
            # SS - short stock
            revenue_chart['SS_' + str(i)] = pd.Series(lst)

    revenue_chart.index= revenue_chart['price']
    revenue_chart.drop('price',inplace=True,axis=1)
    revenue_chart['revenue'] = revenue_chart.sum(axis=1)
    revenue_chart = pd.DataFrame(revenue_chart['revenue'])
    revenue_chart.reset_index(inplace=True)
    return revenue_chart['revenue'][0]*-1

def total_contract_cost_func(holdings_chart):
    """Returns the total cost of all the contracts in a contract chart"""
    # Getting total contract cost to determine total initial cost for visualization
    import pandas as pd
    import numpy as np
    prices = [np.nan]
    revenue_chart = pd.DataFrame(prices)
    revenue_chart.columns = ['price']
    call_count = holdings_chart.count()['calls']
    put_count = holdings_chart.count()['puts']
    stock_count = holdings_chart.count()['stock']

    for i in range(call_count):
        if holdings_chart['calls'][i]['type'] == 'bought':
            lst = []
            BC_cost = holdings_chart['calls'][i]['contract_cost_per_share']*100
            lst.append(BC_cost)
            revenue_chart['BC_' + str(i)] = pd.Series(lst)
        elif holdings_chart['calls'][i]['type'] == 'sold':
            lst = []
            SC_cost = holdings_chart['calls'][i]['contract_cost_per_share']*-100
            lst.append(SC_cost)
            revenue_chart['SC_' + str(i)] = pd.Series(lst)

    for i in range(put_count):
        if holdings_chart['puts'][i]['type'] == 'bought':
            lst = []
            BP_cost = holdings_chart['puts'][i]['contract_cost_per_share']*100
            lst.append(BP_cost)
            revenue_chart['BP_' + str(i)] = pd.Series(lst)
        elif holdings_chart['puts'][i]['type'] == 'sold':
            lst = []
            SP_cost = holdings_chart['calls'][i]['contract_cost_per_share']*-100
            lst.append(SP_cost)
            revenue_chart['SP_' + str(i)] = pd.Series(lst)

    revenue_chart.index= revenue_chart['price']
    revenue_chart.drop('price',inplace=True,axis=1)
    revenue_chart['revenue'] = revenue_chart.sum(axis=1)
    revenue_chart = pd.DataFrame(revenue_chart['revenue'])
    revenue_chart.reset_index(inplace=True)
    return revenue_chart['revenue'][0]*-1

def get_days_until_exp(holdings_chart):
    import datetime
    import pandas as pd
    now = datetime.datetime.now()
    call_count = holdings_chart.count()['calls']
    put_count = holdings_chart.count()['puts']
    stock_count = holdings_chart.count()['stock']

    if call_count > 0:
        days_until_exp = now - holdings_chart['calls'][0]['expiry_date']
        return days_until_exp.days
    elif put_count > 0:
        days_until_exp = now - holdings_chart['puts'][0]['expiry_date']
        return days_until_exp.days
    else:
        return "There are no contracts in your holdings chart"

def gen_revenue_chart(client,ticker,holdings_chart):
    """Generates a revenue chart from a holdings chart"""
    import pandas as pd
    import numpy as np
    from .data_retrieval import retrieve_current_price

    # setup
    current_price = retrieve_current_price(client,ticker)
    visualization_center = visualization_center_func(holdings_chart)
    total_entrance_cost = total_entrance_cost_func(holdings_chart)

    diff = current_price*0.25

    prices = list(np.linspace((visualization_center-diff),(visualization_center+diff),num=100))
    revenue_chart = pd.DataFrame(prices)
    revenue_chart.columns = ['price']
    call_count = holdings_chart.count()['calls']
    put_count = holdings_chart.count()['puts']
    stock_count = holdings_chart.count()['stock']

    # calls
    for i in range(call_count):
        if holdings_chart['calls'][i]['type'] == 'bought':
            call_strike_price = holdings_chart['calls'][i]['strike_price']
            call_contract_price = holdings_chart['calls'][i]['contract_cost_per_share']
            call_num_contracts = holdings_chart['calls'][i]['num_contracts']
            lst = []
            for j in revenue_chart['price']:
                lst.append(BC_revenue_calc(j,call_strike_price,call_contract_price,call_num_contracts))
            # BC - Bought call
            revenue_chart['BC_' + str(i)] = pd.Series(lst)
        elif holdings_chart['calls'][i]['type'] == 'sold':
            call_strike_price = holdings_chart['calls'][i]['strike_price']
            call_contract_price = holdings_chart['calls'][i]['contract_cost_per_share']
            call_num_contracts = holdings_chart['calls'][i]['num_contracts']
            lst = []
            for j in revenue_chart['price']:
                lst.append(SC_revenue_calc(j,call_strike_price,call_contract_price,call_num_contracts))
            # SC - Sold call
            revenue_chart['SC_' + str(i)] = pd.Series(lst)

    #puts
    for i in range(put_count):
        if holdings_chart['puts'][i]['type'] == 'bought':
            put_strike_price = holdings_chart['puts'][i]['strike_price']
            put_contract_price = holdings_chart['puts'][i]['contract_cost_per_share']
            put_num_contracts = holdings_chart['puts'][i]['num_contracts']
            lst = []
            for j in revenue_chart['price']:
                lst.append(BP_revenue_calc(j,put_strike_price,put_contract_price,put_num_contracts))
            # BP - bought put
            revenue_chart['BP_' + str(i)] = pd.Series(lst)
        elif holdings_chart['puts'][i]['type'] == 'sold':
            put_strike_price = holdings_chart['puts'][i]['strike_price']
            put_contract_price = holdings_chart['puts'][i]['contract_cost_per_share']
            put_num_contracts = holdings_chart['puts'][i]['num_contracts']
            lst = []
            for j in revenue_chart['price']:
                lst.append(SP_revenue_calc(j,put_strike_price,put_contract_price,put_num_contracts))
            # SP - Sold put
            revenue_chart['SP' + str(i)] = pd.Series(lst)

    #stock
    for i in range(stock_count):
        if holdings_chart['stock'][i]['type'] == 'long':
            long_price_bought = holdings_chart['stock'][i]['price_at_ps']
            long_num_shares = holdings_chart['stock'][i]['num_shares']
            lst = []
            for j in revenue_chart['price']:
                lst.append(long_revenue_calc(long_price_bought,j,long_num_shares))
            # LS - Long stock
            revenue_chart['LS_' + str(i)] = pd.Series(lst)
        elif holdings_chart['stock'][i]['type'] == 'short':
            short_price_sold = holdings_chart['stock'][i]['price_at_ps']
            short_num_shares = holdings_chart['stock'][i]['num_shares']
            lst = []
            for j in revenue_chart['price']:
                lst.append(short_revenue_calc(short_price_sold,j,short_num_shares))
            # SS - short stock
            revenue_chart['SS_' + str(i)] = pd.Series(lst)


    # clean up
    revenue_chart.index= revenue_chart['price']
    revenue_chart.drop('price',inplace=True,axis=1)
    revenue_chart['revenue'] = revenue_chart.sum(axis=1)
    revenue_chart = pd.DataFrame(revenue_chart['revenue'])
    revenue_chart.reset_index(inplace=True)

    return revenue_chart

def get_current_revenue(holdings_chart,current_price):
    import pandas as pd
    import numpy as np
    prices = [np.nan]
    revenue_chart = pd.DataFrame(prices)
    revenue_chart.columns = ['price']
    call_count = holdings_chart.count()['calls']
    put_count = holdings_chart.count()['puts']
    stock_count = holdings_chart.count()['stock']

    # calls
    for i in range(call_count):
        if holdings_chart['calls'][i]['type'] == 'bought':
            call_strike_price = holdings_chart['calls'][i]['strike_price']
            call_contract_price = holdings_chart['calls'][i]['contract_cost_per_share']
            call_num_contracts = holdings_chart['calls'][i]['num_contracts']
            lst = []
            lst.append(BC_revenue_calc(current_price,call_strike_price,call_contract_price,call_num_contracts))
            revenue_chart['BC_' + str(i)] = pd.Series(lst)
        elif holdings_chart['calls'][i]['type'] == 'sold':
            call_strike_price = holdings_chart['calls'][i]['strike_price']
            call_contract_price = holdings_chart['calls'][i]['contract_cost_per_share']
            call_num_contracts = holdings_chart['calls'][i]['num_contracts']
            lst = []
            lst.append(SC_revenue_calc(current_price,call_strike_price,call_contract_price,call_num_contracts))
            revenue_chart['SC_' + str(i)] = pd.Series(lst)

    # puts
    for i in range(put_count):
        if holdings_chart['puts'][i]['type'] == 'bought':
            put_strike_price = holdings_chart['puts'][i]['strike_price']
            put_contract_price = holdings_chart['puts'][i]['contract_cost_per_share']
            put_num_contracts = holdings_chart['puts'][i]['num_contracts']
            lst = []
            lst.append(BP_revenue_calc(current_price,put_strike_price,put_contract_price,put_num_contracts))
            revenue_chart['BP_' + str(i)] = pd.Series(lst)
        elif holdings_chart['puts'][i]['type'] == 'sold':
            put_strike_price = holdings_chart['puts'][i]['strike_price']
            put_contract_price = holdings_chart['puts'][i]['contract_cost_per_share']
            put_num_contracts = holdings_chart['puts'][i]['num_contracts']
            lst = []
            lst.append(SP_revenue_calc(current_price,put_strike_price,put_contract_price,put_num_contracts))
            revenue_chart['SP' + str(i)] = pd.Series(lst)

    # stock
    for i in range(stock_count):
        if holdings_chart['stock'][i]['type'] == 'long':
            long_price_bought = holdings_chart['stock'][i]['price_at_ps']
            long_num_shares = holdings_chart['stock'][i]['num_shares']
            lst = []
            lst.append(long_revenue_calc(long_price_bought,current_price,long_num_shares))
            # LS - Long stock
            revenue_chart['LS_' + str(i)] = pd.Series(lst)
        elif holdings_chart['stock'][i]['type'] == 'short':
            short_price_sold = holdings_chart['stock'][i]['price_at_ps']
            short_num_shares = holdings_chart['stock'][i]['num_shares']
            lst = []
            lst.append(short_revenue_calc(short_price_sold,current_price,short_num_shares))
            # SS - short stock
            revenue_chart['SS_' + str(i)] = pd.Series(lst)

    revenue_chart.index= revenue_chart['price']
    revenue_chart.drop('price',inplace=True,axis=1)
    revenue_chart['revenue'] = revenue_chart.sum(axis=1)
    revenue_chart = pd.DataFrame(revenue_chart['revenue'])
    revenue_chart.reset_index(inplace=True)
    return revenue_chart['revenue'][0]

def visualize(client,ticker,holdings_chart):
    from .data_retrieval import retrieve_current_price
    import pandas as pd
    import numpy as np
    import seaborn as sns
    import matplotlib.pyplot as plt
    from matplotlib.ticker import FormatStrFormatter
    revenue_chart = gen_revenue_chart(client,ticker,holdings_chart)
    current_price = retrieve_current_price(client,ticker)
    total_entrance_cost = total_entrance_cost_func(holdings_chart)
    visualization_center = visualization_center_func(holdings_chart)
    call_count = holdings_chart.count()['calls']
    put_count = holdings_chart.count()['puts']
    stock_count = holdings_chart.count()['stock']

    diff = total_entrance_cost * 0.04
    ax = sns.lineplot(x=revenue_chart.columns[0],y=revenue_chart.columns[1],data=revenue_chart)
    if np.abs(revenue_chart['revenue'][0]) > np.abs(revenue_chart['revenue'][99]):
        ylimit = np.abs(revenue_chart['revenue'][0]*1.5)
    else:
        ylimit = np.abs(revenue_chart['revenue'][99]*1.5)
    plt.ylim(-ylimit,ylimit)
    ax.axhline(y=0,xmin=0,xmax=1,color="black",alpha=0.3)
    ax.axvline(x=current_price,ymin=0,ymax=1,color="blue",alpha=0.5,label='Current Price',linestyle='--')
    plt.title("Options Strategy Chart\n")
    plt.ylabel("REVENUE")
    plt.xlabel("SECURITY PRICE")
    plt.legend()
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles[::-1], labels[::-1],loc=2,bbox_to_anchor=(1, 1.03),prop={'size': 11})
    ax.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    plt.show()
