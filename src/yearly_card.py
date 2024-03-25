#!/usr/bin/env python3

import argparse
from lib.func import iterate


cards = {0:"The Fool", 1:"The Magicican", 2:"The High Priestess", 3:"The Empress", 4:"The Emperor",
         5:"The Hirophant", 6:"The Lovers", 7:"The Chariot", 8:"Strength", 9:"The Hermit",
         10:"Wheel of Fortune", 11:"Justice", 12:"The Hanged Man", 13:"Death", 14:"Temperance",
         15:"The Devil", 16:"The Tower", 17:"The Star", 18:"The Moon", 19:"The Sun", 
         20:"Judgement", 21:"The World"}

parser = argparse.ArgumentParser(prog="yearly_card.py")
parser.add_argument("-d", help="Birth Day of Month", type=int, required=True)
parser.add_argument("-m", help="Birth Month of Year", type=int, required=True)
parser.add_argument("-y", help="Four digit Year for Reading", type=int, required=True)
args = parser.parse_args()

card = iterate(args.d + args.m + args.y)
print(f"Your card is number {card}")
print(f"Your card is {cards[card]}")
