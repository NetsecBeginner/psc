# psc
Password Strength Checker
### About
psc aims to determine the strength of a password against brute force and dictionary attacks.
### Installation
Linux:

1. From the Terminal Enter 'sudo git clone https://github.com/NetsecBeginner/psc'
2. Navigate to the psc directory
3. Either run the python script(psc.py), or the compiled program(psc)

  Optional:

4. Make the psc.py file executable with the command 'sudo chmod +x psc.py'
5. Copy either the psc or psc.py files to the /usr/local/bin, so the program can be run outside of the psc directory
### Usage
Basic Brute Force Testing:
```
psc [PASSWORD] or python psc.py [PASSWORD]
```
Dictionary Attack Testing:
```
psc -d [PATH/TO/DICTIONARY] [PASSWORD]
```
