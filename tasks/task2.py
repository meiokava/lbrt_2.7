#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = input('enter a sentence: ')
    p1 = set(s.replace(' ', ''))
    s = input('enter a sentence: ')
    p2 = set(s.replace(' ', ''))
    print('The total amount of common symbols = ', p1.intersection(p2))