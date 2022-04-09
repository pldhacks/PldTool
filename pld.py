#!/bin/python3
from os import path
from subprocess import run
import argparse
from sys import stdout

from Hacks import *
from Hacks.Utils import *

parser = argparse.ArgumentParser()
for hack in hacks.hacks:
	hack.init(hack,parser)

args = parser.parse_args()
toRun=set()

for hack in hacks.hacks:
	if hack.test(hack,args):
		toRun.add(hack)

toRun=sorted(list(toRun),reverse=True,key=lambda hack: hack.priority)

rprint(hidecursor)
for running in toRun:
	running.apply(running,args)

nprint(f"{green}Done!{default}{showcursor}")