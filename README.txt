This respository is my personal collection of various simple, portable scripts and tools for crypto-wallets, key manipulations, etc.

BIP39: This tool is from https://github.com/iancoleman/bip39 full credit to iancoleman for making this fantastic tool! Should be downloaded and used offline for security. Supports the generation of, and derivation from, mnemonic seeds for many different crypto-currencies. 

verifyLinux.sh: A linux shell script to automatically verify a downloaded Exodus wallet. The script assumes your download is in your ~/Downloads folder. All you need is curl, gnupg CLI tools, and the URL to the newest release hashes, available from https://www.exodus.io/releases/

lastWill: A bash script skeleton made to run continuously in the background of a linux server. Acts as a dead-man switch, performing an operation in the event that the user doesn't check in at least once in the month.
	This is my personal workaround to avoid 'burning' all my crypto assets in the event of my untimely death. 
	A 'check in' can be performed by executing `touch $will_file` to update the will file's last-modified date.
	How to transmit the desired data from this script is up to you. I would recommend using either the mailutils package, or a Slack bot with a webhook and curl to send an automated message:
	https://api.slack.com/incoming-webhooks#sending_messages
	I strongly recommend using PGP encrypting any data you wish to send using your intended recipients' public keys. However you do it, you can get pretty creative with what you do here.
	You should be very certain you are confident in this script before entering any sensitive data into it, or putting faith into it to handle something as important as your last will. If you can't read the code, don't use it. It is meant to be run constantly in the background on a LINUX server. I use the /etc/init.d/ folder and `screen` to create a detached session (bot) that runs the script automatically whenever the server restarts.
