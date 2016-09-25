def atbash(plain):

    cipher=[' ']
    for i in range(0,len(plain)):
        print (str)(128-ord(plain[i]))
        cipher.append((chr)(128-ord(plain[i])))
        out ="".join(cipher)
        #print "test cipher print"+"".join(cipher)
    return out

def atbash_text(plain):

    cipher=[]
    for i in range(0,len(plain)):
        #print (str)(159-ord(plain[i]))
        cipher.append((chr)(159-ord(plain[i])))
        out ="".join(cipher)
        #print "test cipher print"+"".join(cipher)
    return out

def caesar(plain,key):
    cipher = []

    out="hello"
    for i in range(0, len(plain)):
        cipher.append((chr)(((ord(plain[i])-33+key)%94)+33))
        out = "".join(cipher)
    return out



def banner():
    print"\n\033[1m\n _   _                       _  \n"\
 "| \ | |                     | |           \n"\
 "|  \| | ___ _ __ _   _ _ __ | |_ ___ _ __ \n"\
 "| . ` |/ __| '__| | | | '_ \| __/ _ \ '__|\n"\
 "| |\  | (__| |  | |_| | |_) | ||  __/ |   \n"\
 "|_| \_|\___|_|   \__, | .__/ \__\___|_|   \n"\
 "                  __/ | |                 \n"\
 "                 |___/|_|                 \n"+'\033[92m'


    print"Please Select Encryption Metod.\n" \
     "0- Caesar Reverse\n" \
     "1- Caesar\n" \
     "2- Atbash [Text]\n" \
     "3- Atbash [Binary]\n" \
     "4- Custom Script\n"



def main():
    banner()


    method = raw_input("Method:\033[0m")
    plain = raw_input("\033[92m\033[1mInput:\033[0m")
    if (method == "0"):
        key = input("\033[92m\033[1mCaesar Key:\033[0m")
        print "\033[92m\033[1mOutput:\033[0m" + caesar(plain, -(key%94))
    elif (method=="1"):
        key = input("\033[92m\033[1mCaesar Key:\033[0m")
        print "\033[92m\033[1mOutput:\033[0m" + caesar(plain, key%94)

    elif (method == "2"):
        print "\033[92m\033[1mOutput:\033[0m" + atbash_text(plain)
    main()
    #print "\033[92m\033[1mOutput:\033[0m" + atbash_text(plain)
    #print "\033[92m\033[1mOutput:\033[0m" + caesar(plain,2)

main()


