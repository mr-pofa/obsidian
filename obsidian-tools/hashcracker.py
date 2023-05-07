import os
hash = input("print your hash : ")
wordlist_ask = input("you have a wordlist : Y/n : ")
if wordlist_ask.lower() == "y" :
    wordlist = input("print wordlist path : ")
    os.system(f"echo {hash} > /tmp/john-hash.txt ; john -w={wordlist} /tmp/john-hash.txt")
if wordlist_ask.lower() == "n" :
    os.system(f"echo {hash} > /tmp/john-hash.txt ; john /tmp/john-hash.txt")