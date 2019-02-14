from yaks import *
from papero import Property
import jsonpickle
import random
import sys
import time

filter = "x > 50"

def update_filter(kvs):
    global filter
    for kv in kvs:
        _,v = kv
        filter = v.value
        print('New Filter: {}'.format(v))


def main(addr):
    y = Yaks.login(addr)
    ws = y.workspace('/demo/fprod')
    ws.subscribe('/demo/fprod/filter', update_filter)

    while True:
        f = input(':> input a filter expression in x, such as \"x > 40\", \"x%2 == 0\":\n:>')
        print('Setting the new filter: {}'.format(f))
        ws.put('/demo/fprod/filter', Value(f, encoding=Encoding.STRING))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('[Usage] {} <yaks server address>'.format(sys.argv[0]))
        exit(-1)

    addr = sys.argv[1]
    main(addr)

