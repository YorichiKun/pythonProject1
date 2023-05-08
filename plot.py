import datetime

import matplotlib.pyplot as plo
import yfinance as yf
import pandas_datareader.data as web

def plot_r_u():
    yf.pdr_override()
    s = web.DataReader("USDRUB=X",datetime.datetime.today()-datetime.timedelta(days=1460))
    plo.plot(s.index,s["Close"])
    plo.show()
# plot_r_u()


def ():
    yf.pdr_override()
    s = web.DataReader("BTC-USD",datetime.datetime.today()-datetime.timedelta(days=1460))
    plo.plot(s.index,s["Close"])
    plo.show()
plot_b_u()







# plo.plot([100,3,3,55,4,58,29,39,91],[11,6,4,33,66,34,27,69,37])
# plo.show()