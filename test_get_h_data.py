from tushare import get_h_data

__author__ = 'tyz'

p = get_h_data('600000', start='2010-01-01', autype='nodrop')
print(p)
