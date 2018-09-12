#!/usr/bin/env python

import argparse
import csv
import collections

def parse_command_args():
    """
    Parse command line arguments
    """
    parser = argparse.ArgumentParser(description="Trade Reconciler")
    parser.add_argument('-f', '--firm',
        help='url to list of firm trades',
        required=True
    )
    parser.add_argument('-e', '--exchange',
        help='local path to exchange trades file',
        required=True
    )
    
    return parser.parse_args()

def get_exchange_trades(csvfile):
    """
    Read in the CSV file and return a counter of the trades.
    """
    trades_counter = collections.Counter()
    print("Processing {}".format(csvfile))
    reader = csv.DictReader(open(csvfile, 'r'))
    for data in reader:
            trade = (
                data['Symbol'],
                data['Side'],
                data['Quantity'],
                data['Price']
            )
            trades_counter.update([trade])
    return trades_counter

if __name__ == "__main__":
    args = parse_command_args()
    exchange_trades = get_exchange_trades(args.exchange)
    from pprint import pprint
    pprint(exchange_trades)
    
