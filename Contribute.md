# How to contribute: an example
Let's say that you want to add the functionality of making a text file containing "hello world" in the root of the system, to this project... How would you do it?

1. Create a markdown file documenting the feature you want to add, in `Hacks/<Module>.md`
   ```md
   + Hacks/HelloWorld.md:
   + 1 | # (HelloWorld)[HelloWorld.py] exploits
   + 2 | - `./pld.py --hello-world`:
   + 2 |   - Places a text file with "hello world" into the root of the system drive
   ```
2. Place all your needed resources into the `files` folder
   ```
   + files/HelloWorld.txt:
   + 1 | Hello World!
   ```
3. Add the file to the `files/Files.md` index
   ```md
   files/Files.md:
   + 14 | - [`HelloWorld.txt`](./HelloWorld.txt)
   + 15 |   - A text file with "Hello World"
   ```
4. Try to implement it with the Hacks api with `/Hacks/<Module>.py`
   ```py
   + Hacks/HelloWorld.py:
   + 1  | from .Framework import *
   + 2  | from .Utils import *
   + 3  | 
   + 4  | # Makes a text file with "Hello world" in the root of the windows fs
   + 5  | 
   + 6  | #                               |   help text shown  |
   + 7  | #     argument that will run it v   with -h          v
   + 8  | helloworld=SimpleHack("hello-world","Make a hello world")
   + 9  | hacks.addHack(helloworld) # register it into the list of hacks
   + 10 | 
   + 11 | # The code that actually makes the hello world
   + 12 | @helloworld.hack
   + 13 | def mkhello(self,args):	
   + 14 |     info("Making the hello world...")
   + 15 |     handleBash("cp ./files/HelloWorld.txt ./windows-mnt/")
   + 16 | 
   ```
5. Append your module to `Hacks/__init__.py`
   ```py
   Hacks/__init__.py:
   + 4 | from .HelloWorld import *
