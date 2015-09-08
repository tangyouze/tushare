import pandas as pd
from tushare import get_h_data, get_realtime_quotes


# p = get_h_data('600000', start='2010-01-01', autype='nodrop')
# print(p)

pd.set_option('display.width', 1000)
x = get_realtime_quotes(['150150', '150151'])
print(x)
print(x.loc[0].bids)
