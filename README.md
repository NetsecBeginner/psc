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
### Q&A
```
Q: My password is being interpreted strangely, how can I fix that?
A: This is probably because the password string is not escaped, try adding single quotes around the password('PASSWORD')
```
```
Q: I'm a developer, and I want to implement a password policy, what do you recommend?
A: Password policies don't stop users from using bad passwords, they just force them to be a bit more creative.  It's easier to just not attempt to implement one.  Instead you should focus your efforts on using a secure hashing algorithm and salting your hashes.
```
```
Q: Will your program ever have a graphical version?
A: Possibly in the future, but probably not anytime soon.
```
```
Q: I want to use part of your code in my program, can I do that?
A: Yes, feel free to use any parts of this program, but please give credit, either in the code or in the readme file
```
```
Q: How can I make a secure password
A: Select four random words(preferrably uncommon ones), and combine them [Relevant xkcd](https://www.xkcd.com/936/)
```
