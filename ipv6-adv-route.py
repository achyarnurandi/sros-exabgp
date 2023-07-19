#!/usr/bin/env python3

from __future__ import print_function

from sys import stdout
from time import sleep

messages = [
    'announce route fc00:0000:0000:1::/64 next-hop self',
    'announce route fc00:0000:0000:2::/64 next-hop self',
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