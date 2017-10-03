#!/usr/bin/python

import os
import sys
import platform

def interactive(prompt):
    return raw_input(prompt)


# To create a default wallet path, add the following line to your ~/.bash_profile or ~/.bashrc
# export EXODUSDIR="/PATH/TO/YOUR/WALLET/DIRECTORY"
if "EXODUSDIR" in os.environ:
    directory = os.environ["EXODUSDIR"]
else:
    # You can specify, on the command line, the folder you want to use. 
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    # If neither of these are supplied, the program prompts you.
    else:
        directory = interactive("Specify directory to use: ")
        
# Expand directory if user input shortcuts
directory = os.path.expanduser(directory)
    
# If the directory specified doesn't exist, prompt to create it
if not os.path.isdir(directory):
    print("Specified directory '%s' does not exist" % directory)
    answer = interactive("Would you like to create a new wallet here? ")
    if answer not in ["yes", "y", "Y", "Yes", "YES"]:
        print("Exiting...")
        sys.exit(1)
        
# If running Mac OS:
if 'Darwin' in platform.system():
    # Check if Exodus is installed
    if not os.access("/Applications/Exodus.app/Contents/MacOS/Exodus", os.X_OK):
        print("Exodus is not installed in /Applications/ Folder. Exiting...")
        sys.exit(1)
    print "Launching with wallet %s" % directory
    os.system("/Applications/Exodus.app/Contents/MacOS/Exodus --datadir " + directory)
        
# If running Linux:
elif 'Linux' in platform.system():
    try:
        # To specify the default Exodus program executable location, add this line to your ~/.bashrc file:
        # export EXODUSPROG="/PATH/TO/EXODUS/EXECUTABLE"
        if "EXODUSPROG" not in os.environ:
            answer = os.path.expanduser(interactive("Linux Detected; Specify path to Exodus program folder: "))
            
            # If the user supplies a folder, append a "/Exodus" to it, hoping they provided the Exodus program directory
            if os.path.isdir(answer):
                if answer[-1] != "/":
                    answer += "/"
                executable = answer + "Exodus"
                
            # If they supplied the executable, label it as such
            elif os.path.isfile(answer):
                executable = answer
        else:
            executable = EXODUSPROG
        # Check if the file is actually executable
        if not os.access(executable, os.X_OK):
            print("Supplied file is not an executable. Exiting...")
            sys.exit(1)
        # Otherwise, proceed with launch
        print "Launching with wallet %s" % directory
        os.system(executable + " --datadir " + directory)
        
    except:
        print "Unknown error occurred."
        sys.exit(1)