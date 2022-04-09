from sys import stdout
from subprocess import run

hidecursor="\033[?25l"
showcursor="\033[?25h"

def rprint(*stuff):
	if len(stuff)>1:
		stdout.write("\033[0K"+" ".join(stuff)+"\r")
	else:
		stdout.write("\033[0K"+stuff[0]+"\r")
	stdout.flush()

_exit=exit
def exit(n):
	rprint(showcursor)
	_exit(n)

nprint=lambda text: print("\033[0K"+text)

bold="\033[1m"
dim="\033[2m"
italic="\033[3m"
underline="\033[4m"

resetweight="\033[22m"

red="\033[31m"
green="\033[32m"
yellow="\033[33m"
blue="\033[34m"
magenta="\033[35m"
cyan="\033[36m"
default="\033[39m" #reset text color

def runBash(bash):
	result=run(['bash', '-c', bash], capture_output=True, text=True)
	return result

counter=-1
def handleBash(bash):
	global counter
	result=runBash(bash)
	if result.returncode!=0:
		print(f"{red}Command `{bash}` returned \n{result.stdout+result.stderr}".rstrip("\n"))
		exit(counter)
	counter-=1

info=lambda txt: print(f"{green}{txt}{default}")