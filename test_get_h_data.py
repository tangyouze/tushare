from tushare import get_h_data, get_realtime_quotes


# p = get_h_data('600000', start='2010-01-01', autype='nodrop')
# print(p)

x = get_realtime_quotes(['150150', '150151'])
print(x)
