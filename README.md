# Cyborg Challenge
A Chips Challenge clone written in RapydScript (last tested with 0.1.6).

It will require updates to work with the latest version of RapydScript.

## Features

This clone supports a limited feature set.  It will play the first few
levels of the original game without any problems.  I may try to document
the list of missing features at some point.


## Using custom Level Files

If you have a `.dat` file (the original game has a `CHIPS.DAT` file) you must
first convert it to an ascii format using `parser3.py`.  You can then point
to the file by updating the path in `Controller.__init__`,
`LevelLoader(self, 'full.txt')`

It should be possible to update this code to skip this conversion, but first
I would like to get this working with the latest RapydScript.

