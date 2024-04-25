# yearly_card.py

This is a simple program that uses numerology as it relates to the Tarot to 
determine your card of the Major Arcana for the year. It uses a very simple
algorithm, adding your birth day and birth month to the year you wish to ask 
about, then adding the digits of that number together, and repeating the second
process until it gets a number less than 22, as the Major Arcana are numbered
0 through 21. I also wrote a second program that does this in a batch for every
year between two different years. All arguments should be whole integer numbers.

## Usage

    usage: yearly_card.py [-h] -d D -m M -y Y

    options:
    -h, --help  show this help message and exit
    -d D        Birth Day of Month
    -m M        Birth Month of Year
    -y Y        Four digit Year for Reading

.

    usage: forecast.py [-h] -s S -e E -d D -m M

    options:
    -h, --help  show this help message and exit
    -s S        Start four digit year
    -e E        End four digit year
    -d D        Your Birth Day of Month
    -m M        Your Birth Month of Year

## Install

This will eventually be a QT framework graphical program, but at the moment,
it is simply a command-line program. The only requirement is argparse. If you
are on a *nix-like, simply run the included install script.

## To-Do

* [x] Implement a QT Graphical Interface
* [ ] Implement a library of readings for each of the Major Arcana

## License

This program is for fun, licensed under the AGPL-3.0. Enjoy, and Blessed Be!
