def covered_call_hc(strike_price,expiry_date,contract_cost_per_share,num_contracts,price_at_ps,num_shares):
    import numpy as np
    import pandas as pd
    holdings_dict = {'calls':[{'strike_price':strike_price,'expiry_date':expiry_date,'contract_cost_per_share':contract_cost_per_share,'num_contracts':num_contracts,'type':'sold'}],
                     'puts':[np.nan],
                     'stock':[{'price_at_ps':price_at_ps,'num_shares':num_shares,'type':'long'}]}
    holdings_chart = pd.DataFrame(holdings_dict)
    return holdings_chart

def simple_call_hc(strike_price,expiry_date,contract_cost_per_share,num_contracts):
    import numpy as np
    import pandas as pd
    holdings_dict = {'calls':[{'strike_price':strike_price,'expiry_date':expiry_date,'contract_cost_per_share':contract_cost_per_share,'num_contracts':num_contracts,'type':'bought'}],
                     'puts':[np.nan],
                     'stock':[np.nan]}
    holdings_chart = pd.DataFrame(holdings_dict)
    return holdings_chart

def purchase_stock(price_at_ps,num_shares):
    import numpy as np
    import pandas as pd
    holdings_dict = {'calls':[np.nan],
                     'puts':[np.nan],
                     'stock':[{'price_at_ps':price_at_ps,'num_shares':num_shares,'type':'long'}]}
    holdings_chart = pd.DataFrame(holdings_dict)
    return holdings_chart
