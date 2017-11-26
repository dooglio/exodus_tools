#!/usr/bin/env python3
#GHOST TX DESTROYER 9000

import os, sys, csv, glob, time

print( "\n==== WELCOME TO GHOST TX DESTROYER 9000 ====")
print( "============= DOOM AWAITS ==================\n")

def csvSearch(location):
    try:
        os.chdir(os.path.expanduser(location))
        files = glob.glob('%s*.csv' % coin)
        file = files[0]
        print('%s TX file = ' % symbol + os.getcwd() + '/' + file, '\n')
        return file
    except NotADirectoryError:
        #check if the supplied argument is the .csv file itself:
        if '.csv' in location:
            file = location
            print('file = ' + os.getcwd() + '/' + file, '\n')
            return file
        else:
            print('Error - Directory not found; please ensure you\'re entering a valid directory path.')
            sys.exit(1)
    except FileNotFoundError:
        print('Error - Directory not found; please ensure you\'re entering a valid directory path.')
        sys.exit(1)
    except IndexError:
        print('Error - file not found; please ensure you\'re entering the correct directory path.')
        sys.exit(1)
    except:
        print('Unknown error occurred')



def btc():
    print('Bitcoin selected\n')
    time.sleep(0.5)
    global coin, symbol
    coin = 'bitcoin'
    symbol = 'BTC'
def bch():
    print('Bitcoin Cash selected\n')
    time.sleep(0.5)
    global coin, symbol
    coin = 'bcash'
    symbol = 'BCH'
def ltc():
    print('Litecoin selected\n')
    time.sleep(0.5)
    global coin, symbol
    coin = 'litecoin'
    symbol = 'LTC'
def eth():
    print('Ethereum selected\n')
    time.sleep(0.5)
    global coin, symbol
    coin = 'ethereum'
    symbol = 'ETH'
def dash():
    print('Dash selected\n')
    time.sleep(0.5)
    global coin, symbol
    coin = 'dash'
    symbol = 'DASH'
def decred():
    print('Decred selected\n')
    time.sleep(0.5)
    global coin, symbol
    coin = 'decred'
    symbol = 'DCR'

options = {
1 : btc,
2 : bch,
3 : ltc,
4 : eth,
5 : dash,
6 : decred,
}
# allow the user to choose their exported currency
try:
    selection = int(input('Choose your currency:\n  1 - Bitcoin\n  2 - Bitcoin Cash\n  3 - Litecoin\n  4 - Ethereum\n  5 - Dash\n  6 - Decred\n ---> '))
    options[selection]()
except:
    print('Please choose a valid number')
    sys.exit(1)








if len(sys.argv) == 2:
    #If the user supplies an argument, assume that's the directory and handle it as the input.
    loc = sys.argv[1]
    file = csvSearch(loc)

elif len(sys.argv) > 2:
    #Checks for more than one argument
    print("Only one argument is supported; Calm down, we can ice them one at a time!")
    sys.exit(1)

else:
    print("Please enter the folder location containing the .csv file to be ghost-destroyified below.")
    loc = input("If the file is in the current directory, leave this field blank: -->: ")
    print('')

    if len(loc) != 0:
        file = csvSearch(loc)
    else:
        file = glob.glob('%s*.csv' % coin)
        file = file[0]
        print('file = ' + os.getcwd() + '/' + file, '\n')

#file = str.format(file)
#file = "bitcoin-txs-2017-11-20_17-44-48.csv"
#ile = file.strip()

deposits = []
withdrawals = []
fees = []

with open(file) as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader, None)
    for row in csvreader:
        if row[4]:
            f_amount = row[4].strip(" %s" % symbol)
            f_amount = f_amount.strip("-")
            f_amount = f_amount.strip()
            f_amount = float(f_amount)
            #print(f_amount)
            fees.append(f_amount)
        if "-" in row[3]:
            w_amount = row[3].strip(" %s" % symbol)
            w_amount = w_amount.strip("-")
            w_amount = float(w_amount)
            #print(w_amount)
            withdrawals.append(w_amount)
        else:
            d_amount = row[3].strip(" %s" % symbol)
            d_amount = float(d_amount)
            #print(d_amount)
            deposits.append(d_amount)

deposits_total = sum(deposits)
withdrawal_total = sum(withdrawals)
fees_total = sum(fees)

print ("Deposits: ", round(deposits_total, 8), symbol)
print ("Withdrawals: ", round(withdrawal_total, 8), symbol)
print ("Fees: ", round(fees_total, 8), symbol)
print ("Total :" , round(deposits_total - (withdrawal_total + fees_total), 8), symbol)
