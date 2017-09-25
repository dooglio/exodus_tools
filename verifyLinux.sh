#!/bin/sh

if ! which gpg > /dev/null ; then
	alias gpg='gpg2'

elif ! which gpg2 > /dev/null ; then
	echo "GnuPG not installed. Exiting..."
	exit 1
fi

if ! which curl > /dev/null ; then
	echo "Curl not installed. Exiting..."
	exit 1
fi

# Prompt for release hash URL
read -p "Input full URL for release hashes> " hashes

# Define JP's key
jpKey='https://keybase.io/jprichardson/pgp_keys.asc?fingerprint=12408650e2192febe4e7024c9d959455325b781a'


echo ; echo


# If JP's key doesn't exist...
if ! gpg -k | grep -q JP ; then 
	# ...Import JP Richardson's Public Key
	curl -s $jpKey | gpg --import -q
fi

# Verify release hashes
curl -s $hashes | gpg --verify


echo ; echo 


# Compare published hashes to downloaded package
compareHashes () {
    curl -s $hashes | grep linux
    eval shasum -a 256 $pathName
}

if [ -f ~/Downloads/exodus-linux* ] ; then
    eval pathName="~/Downloads/exodus-linux*.zip"
    compareHashes
    
# If no downloaded package found, prompt for pathname
else
    echo "No Exodus download found in ~/Downloads/"
    read -p "Specify absolute path to exodus-linux-x64-x.xx.x> " pathName
    if ! eval ls $pathName | grep -q exodus ; then
        echo "No Exodus package found. Exiting..."
        exit
    fi
    compareHashes
fi
