
import csv

def  read_prices(filename):
    prices={}
    f = open('Data/prices.csv', 'r')
    rows = csv.reader(f)
    for row in rows:
        try:
            prices[row[0]]=float(row[1])
        except IndexError:
            pass

    return prices   