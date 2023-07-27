#!/usr/bin/env python3

from __future__ import print_function

from sys import stdout
from time import sleep

messages = [
    'announce attributes origin IGP as-path [65000 29608 3356 29396 29396 29396 39686 44953 ] med 13 community [3356:2 3356:22 3356:100 3356:123 3356:503 3356:2067 29608:30600] next-hop self nlri 93.95.248.0/21',
    'announce route 100.10.0.0/24 next-hop self as-path [65000 4818 4788 6300 1200] origin IGP attribute [0x1C 0xC0 0x00]',
    'announce route 200.20.0.0/24 next-hop self as-path [65000 4818 4788 6300 1200] origin IGP attribute [0x1C 0xE0 0x00]',
]

sleep(5)

#Iterate through messages
for message in messages:
    stdout.write(message + '\n')
    stdout.flush()
    sleep(1)

#Loop endlessly to allow ExaBGP to continue running
while True:
    sleep(1)