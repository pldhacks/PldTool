from .Framework import *
from .Utils import *
from os import path

#this mounts the drive if not no_mount
mount=Hack() 
mount.priority=float("inf")
hacks.addHack(mount)

@mount.initialiser
def addArgs(self,parser):
	parser.add_argument("--no-mount", help="Assume drive already mounted, skip mounting",action="store_true")
	parser.add_argument("--bitlocker", help="Bitlocker recovery key")
	parser.add_argument("--partition", help="PLD system partition device file (default: /dev/mmcblk0p3)",default="/dev/mmcblk0p3")

@mount.hack
def mountDrive(self,args):
	runBash("mkdir dislocker-mnt windows-mnt")
	if args.bitlocker:
		info("Fusing bitlocker drive to /mnt/fromdsk with dislocker")
		handleBash(f"dislocker {args.partition} ./dislocker-mnt -p{args.bitlocker}")

		info("Mounting partition...")
		handleBash(f"mount ./dislocker-mnt/dislocker-file ./windows-mnt")
	else:
		info("Mounting partition...")
		handleBash(f"mount {args.partition} ./windows-mnt")

mount.test=lambda self,args: not args.no_mount

# This unmounts the drive if not leave_mount
unmount=SimpleHack("leave-mount","Leave the drive mounted",negated=True)
hacks.addHack(unmount)

@unmount.hack
def unmountp(self,args):
	info("Unmounting partition")
	handleBash("umount ./windows-mnt")

	if args.bitlocker or (args.no_mount and path.exists("./dislocker-mnt/dislocker-file")):
		info("Unmounting dislocker-file")
		handleBash("umount ./dislocker-mnt")

unmount.priority=float("-inf") # last