
# Prevent your MAC's screen from going to sleep!

### Do you also find it annoying when your mac's screen keeps going to sleep?

### This tool's got you covered!



## installation:

This package is NOT distributed to pypi, please install the package directly from this repo:<br>
<li>If a virtualenv is activated:</li>

`python3 -m pip install git+git://github.com/uryyakir/mover.git#egg=mover`
<li>If you want to install globally:</li>

`sudo python3 -m pip install git+git://github.com/uryyakir/mover.git#egg=mover`


## usage:

simply type `mover` and let the tool take control!

All the tool does is pressing the <i>Capslock</i> key <b>twice</b> every 30 seconds, thus manipulating your OS and preventing it from detecting that you're AFK. The key is pressed twice instantaneously to alternate its status back to the original state without the user actually noticing.



you may also use the `--run-time-hours` argument to control the tool's total run-time; it will automatically stop after that period is exceeded. Notice that the default run-time period is (currently) 30 minutes.

Example:

`mover --run-time-hours 3` --> Running for 3 hours before quitting.

`mover -rt 2` --> same concept, but using the argument's shortcut.
