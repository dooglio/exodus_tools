# About This Repo
This respository is my personal collection of various simple, portable scripts and tools for crypto-wallets, key 
manipulations, etc. Unless otherwise noted, all these are written by me, and can be used, copied, and distributed freely.

## BIP39
This tool is from https://github.com/iancoleman/bip39 full credit to iancoleman for making this fantastic 
tool! Should be downloaded and used offline for security. Supports the generation of, and derivation from, 
mnemonic seeds for many different crypto-currencies.

## verifyLinux.sh
A linux shell script to automatically verify a downloaded Exodus wallet. The script assumes your 
download is in your `~/Downloads` folder. All you need is curl, gnupg CLI tools, and the URL to the newest release 
hashes, available from https://www.exodus.io/releases/

## lastWill
A bash script skeleton made to run continuously in the background of a Linux server. Acts as a 
dead-man switch, performing an operation in the event that the user doesn't check in at least once in the month.

This is my personal workaround to avoid 'burning' all my crypto assets in the event of my untimely death.

A 'check in' can be performed by executing `touch $will_file` to update the will file's last-modified date.

How to transmit the desired data from this script is up to you. I would recommend using either the `mailutils` package, 
or a Slack bot with a webhook and curl to send an automated message:

https://api.slack.com/incoming-webhooks#sending_messages

I strongly recommend PGP encrypting any data you wish to send using your intended recipients' public keys. 
However you do it, you can get pretty creative with what you do here.

You should be very certain you are _confident_ in this script before entering any sensitive data into it, or putting 
faith into it to handle something as important as your last will. *If you can't read the code, don't use it.* It is meant to be 
run constantly in the background on a LINUX server. I use the /etc/init.d/ folder and `screen` to create a detached session 
(bot) that runs the script automatically whenever the server restarts.

## enscript
A program made for use with GPG based encryption of bash scripts that might contain sensitive data. You can use the 
various options to open & edit, `-o` encrypt a file quickly, `-e` decrypt a file, `-d` or execute the enscripted script.

## exodir.py
A python program that will allow Mac and Linux users of Exodus to run multiple wallets with different seeds. Run straight from 
the command line such as `./exodir.py` or `python exodir.py`, it will run interactively, prompting for a wallet data directory. 

You can also run it with an argument, which will be taken and used as the wallet data folder:

```./exodir.py /Users/Bob/Desktop/foo```

Would open a wallet on Bob's desktop with the folder `foo`.

Linux users will need to specify where they have their Exodus program data located, by putting the Exodus executable file's 
location into an environment variable in their `~/.bashrc` file. Add a line like this to the `.bashrc` file:

```export EXODUSPROG="/PATH/TO/EXODUS/EXECUTABLE"```

Mac users should, by default, have Exodus installed in their Applications folder, so that's no concern for you.

Either OS can specify a default wallet data folder for `exodir` to open. This is an easy way to seamlessly open and use 
multiple wallets. Mac users can add this line to their `~/.bash_profile` (create one if it isn't there already) and 
`~/.bashrc` for Linux.

```export EXODUSDIR="/PATH/TO/WALLET/DATA/FOLDER/"```
