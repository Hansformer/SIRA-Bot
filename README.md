# :aries: SIRA (Settlement, Investment & Realty of the Arietis) Discord Bot :robot:

Turn back now.


## Help/Commands

### Remember that slash commands have autocompletion in Discord, you may not need this for usage help

### Basic Commands

- `/active` - *SIRA-only command to toggle active/inactive tag*
- `/lyr` - *SIRA-only command to toggle LYR tag*
- `/mattrade` - *lists the material traders near LP 355-65*
- `/link x` - *links to various web destinations, replaces the old individual !website etc commands*

### EDSM Integration

- `/status` - *checks ED server status per FDev*
- `/sysinf x` - *replace x with a system name to check faction influence/states overview via EDSM*
- `/traffic x` - *replace x with a system name to check EDSM traffic reports*

### Semi-Useful Images

- `/image flag` - *displays the Space Ireland flag*
- `/image logo` - *displays the SIRA logo*

### Memes (don't spam these, consider this a warning)

- `/image x` - *various different meme images*


## Feature Wishlist

- EDSM/EDDN API connection (WIP, basic complete)
- ~Spouting memes~ (more than done)
- Sanity (never)
- Useful features (maybe never)


## Technical Usage

### Alwayse use a venv.

### Install requirements

$ python3 -m pip install -r requirements.txt

### Optionally install

Requires gcc or other compiler but provides a minor performance increase.\
(More efficient compression etc.)\
$ python3 -m pip install hikari[speedups]

Only works on UNIX.\
$ python3 -m pip install uvloop

### Finally run the bot

#### Copy config.py.example to config.py and edit it then:

$ python3 -O main.py
