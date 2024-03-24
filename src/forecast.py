import argparse
from lib.func import iterate

cards = {0:"The Fool", 1:"The Magicican", 2:"The High Priestess", 3:"The Empress", 4:"The Emperor",
         5:"The Hirophant", 6:"The Lovers", 7:"The Chariot", 8:"Strength", 9:"The Hermit",
         10:"Wheel of Fortune", 11:"Justice", 12:"The Hanged Man", 13:"Death", 14:"Temperance",
         15:"The Devil", 16:"The Tower", 17:"The Star", 18:"The Moon", 19:"The Sun", 
         20:"Judgement", 21:"The World"}

parser = argparse.ArgumentParser("forecast.py", help="Forecast for your yearly card")
parser.add_argument("-s", help="Start four digit year", required=True, type=int)
parser.add_argument("-e", help="End four digit year", required=True, type=int)
parser.add_argument("-d", help="Your Birth Day of Month", required=True, type=int)
parser.add_argument("-m", help="Your Birth Month of Year", required=True, type=int)
args = parser.parse_args()
for year in range(args.s, (args.e + 1)):
    card = iterate(year + args.m + args.d)
    print(f"Your forcast for the year {year} is number {card} {cards[card]}")