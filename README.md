# Py-Installer-Template
The code I use for my install.py files. It's not the best, but enjoy.

This has only been tested on Fedora Linux

# How do I use this?
To use this, download the installer template based on where you are getting packages from.

EX: I only have things that are from PIP, use the file ending in _pip
    If you need things from APT and PIP, use the _aptpip etc...

Then edit the names of anything that is in [] 

Finally, run `pip freeze > requirements.txt` to get your requirements.
For anything else, add them where there is [APT], [DNF] or [GIT]

