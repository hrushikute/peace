
import urllib,re,time,logging
import threading as mt


symbols=['IDEA','AAPL']


def fun1(symbols):
    for symbol in symbols:
        url = 'https://www.google.com/finance?q=' + symbol
        url_obj = urllib.urlopen(url)

        content = url_obj.read()
        # print content
        match = re.search('<span id="ref_\d+_\w">(.*)<', content)

        if match:
            print 'The price of {} is {}\n'.format(symbol, match.group(1))
        else:
            pass