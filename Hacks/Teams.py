from .Framework import *
from .Utils import *

# Stop teams from autolaunching by replacing the update executable (that autolaunches) with nop.exe
breakteams=SimpleHack("nolaunch-teams","Stop teams from autolaunching")
hacks.addHack(breakteams)

@breakteams.hack
def replaceNop(self,args):	
	info("NOP'ing the teams updater...")
	handleBash("dd if=./files/nop.exe of='./windows-mnt/Program Files (x86)/Teams Installer/Teams.exe'")

# Prevent PLD from shutting down by replacing the teams installer (that starts automatically) with 
# an executable that abouts shutdowns every 750ms
nosleep=SimpleHack("nosleep","Stop the pld from shutting down by replacing the Teams installer with NoSleep.exe")
hacks.addHack(nosleep)

@nosleep.hack
def replacenosleep(self,args):	
	info("Changing the teams installer to nosleep")
	handleBash("dd if=./files/NoSleep.exe of='./windows-mnt/Program Files (x86)/Teams Installer/Teams.exe'")

nosleep.priority=1.0 # last
breakteams.priority=1.1 # first