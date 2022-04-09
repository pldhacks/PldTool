# PldTool, an utility to aid with pld hacking
PldTool is a command-line tool that aids in the mounting of the pld partition, and the application of some hacks. It is designed with the goal of automating the repetitive proccess of mounting and `dd`ing files, and to allow everyone to contribute their hacks to a single repository.

## Disclaimer
DO NOT USE THIS IF YOU ARE A SCRIPTKIDDIE!  
This software is experimental, and has a non-zero chance of screwing something up. It takes sheer knowledge and intuition (something scriptkiddies dont have) to fixed a botched run.

## Requirements
### Physical
This script requires the PLD system drive to be plugged into a host device running linux. This can be acheived in the following ways:
- Having a linux dual-boot in the pld (recommended)
- Taking apart the pld

### Packages
`Dislocker` (is required for mounting the partition if it is protected by bitlocker (default))

## Installation
There is no installation. Just install the [needed packages](#packages), clone this repository, and run `pld.py`

## Usage
We briefly explain how to apply hacks and mount the pld system drive using `pldtool`. To see all command line options, run `./pld.py -h`.

### Applying hacks
If the pld is encrypted with bitlocker (default), you will need to pass the bitlocker recovery key to `--bitlocker`.

For example:
```bash
# apply the hack to stop the pld from shutting off at 11pm
./pld.py --bitlocker 991262-991262-991262-991262-991262-991262-991262-991262 --nosleep
```

If the pld is not encrypted with bitlocker, the command is very simple:
```bash
# apply the hack to stop the pld from shutting off at 11pm
./pld.py --nosleep
```

Full hacks list [here](./Hacks/Index.md)

### Mounting the PLD system drive for experimentation or manual hack application
The following command will leave the pld system drive mounted in `./windows-mnt`, and the dislocker file in `./dislocker-mnt`, if the drive was mounted with the `--bitlocker` argument.
```bash
./pld.py --leave-mount [--bitlocker 991262-991262-991262-991262-991262-991262-991262-991262]
```

The following command will unmount the system drive.
```bash
./pld.py --no-mount
```

Remember to unmount, as shutting the system down will not properly flush all the data to disk!

## TODOs
- Make the hacking framework modular, and allow hacks to be easily and cleanly added.

## License
This project uses the GPLv3

# Please [contribute](Contribute) and allow this project to g r o w!
