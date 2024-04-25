#!/usr/bin/env python3
import argparse
from lib.func import iterate

cards = {0:"the fool", 1:"the magicican", 2:"the high priestess", 3:"the empress", 4:"the emperor",
         5:"the hirophant", 6:"the lovers", 7:"the chariot", 8:"strength", 9:"the hermit",
         10:"wheel of fortune", 11:"justice", 12:"the hanged man", 13:"death", 14:"temperance",
         15:"the devil", 16:"the tower", 17:"the star", 18:"the moon", 19:"the sun", 
         20:"judgement", 21:"the world"}

parser = argparse.ArgumentParser("forecast.py")
parser.add_argument("-s", help="Start four digit year", required=True, type=int)
parser.add_argument("-e", help="End four digit year", required=True, type=int)
parser.add_argument("-d", help="Your Birth Day of Month", required=True, type=int)
parser.add_argument("-m", help="Your Birth Month of Year", required=True, type=int)
args = parser.parse_args()
for year in range(args.s, (args.e + 1)):
    card = iterate(year + args.m + args.d)
    print(f"Your forcast for the year {year} is number {card} {cards[card]}")