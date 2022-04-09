# (Teams)[./Teams.py] exploits
- `./pld.py --break-teams`:
	- Replaces the `Update.exe` that autolaunches on boot with `nop.exe`
- `./pld.py --nosleep`:
	- Replaces the `Update.exe` that autolaunches with [`NoSleep.exe`](../files/Files.md) to stop the pld from shutting down at 11pm
