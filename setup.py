#! /usr/bin/python
import os
import time
if True :
     """ ANSI color codes """
     BLACK = "\033[0;30m"
     RED = "\033[0;31m"
     GREEN = "\033[0;32m"
     BROWN = "\033[0;33m"
     BLUE = "\033[0;34m"
     PURPLE = "\033[0;35m"
     CYAN = "\033[0;36m"
     LIGHT_GRAY = "\033[0;37m"
     DARK_GRAY = "\033[1;30m"
     LIGHT_RED = "\033[1;31m"
     LIGHT_GREEN = "\033[1;32m"
     YELLOW = "\033[1;33m"
     LIGHT_BLUE = "\033[1;34m"
     LIGHT_PURPLE = "\033[1;35m"
     LIGHT_CYAN = "\033[1;36m"
     LIGHT_WHITE = "\033[1;37m"
     BOLD = "\033[1m"
     FAINT = "\033[2m"
     ITALIC = "\033[3m"
     UNDERLINE = "\033[4m"
     BLINK = "\033[5m"
     NEGATIVE = "\033[7m"
     CROSSED = "\033[9m"
     END = "\033[0m"


user_info = os.getuid()
if user_info != 0:
    print(f"{LIGHT_RED}run as root{END}")
    exit()
print(f"""{YELLOW}Tools needed by the application {END}
 [{LIGHT_CYAN}1{END}]{LIGHT_PURPLE} curl{END}
 [{LIGHT_CYAN}2{END}]{LIGHT_PURPLE} msfvenom{END}
 [{LIGHT_CYAN}3{END}]{LIGHT_PURPLE} john{END}
 [{LIGHT_CYAN}4{END}]{LIGHT_PURPLE} gobuster{END}
 [{LIGHT_CYAN}5{END}]{LIGHT_PURPLE} wpscan{END}
""")

#--------------------------------
if os.path.exists("/usr/local/sbin/curl") or os.path.exists("/usr/local/bin/curl") or  os.path.exists("/usr/sbin/curl") or  os.path.exists("/usr/bin/curl") or  os.path.exists("/bin/curl") or  os.path.exists("/usr/local/games/curl") or  os.path.exists("/usr/games/curl") :
    print(f"{LIGHT_GREEN}curl found{END}")
else:
    print(f"{LIGHT_RED}curl not found{END}")
    print("""the option
    [1] download received
    [2] skip""")
    curl = input("Make your choice : ")
    if curl == "1" :
        os.system(f"{END}apt install curl ")
    if curl == "2" :
        print(f"{LIGHT_GREEN}skip is done")
        
#--------------------------------
time.sleep(1)
if os.path.exists("/usr/local/sbin/msfvenom") or os.path.exists("/usr/local/bin/msfvenom") or  os.path.exists("/usr/sbin/msfvenom") or  os.path.exists("/usr/bin/msfvenom") or  os.path.exists("/bin/msfvenom") or  os.path.exists("/usr/local/games/msfvenom") or  os.path.exists("/usr/games/msfvenom") :
    print(f"{LIGHT_GREEN}msfvenom found{END}")
else:
    print(f"{LIGHT_RED}msfvenom not found{END}")
    print(f"""{RED}the option
    [1] download received
    [2] skip""")
    msfvenom = input("Make your choice : ")
    if msfvenom == "1" :
        os.system(f"{END}apt install msfvenom")
    if msfvenom == "2" :
        print(f"{LIGHT_GREEN}skip is done")
#--------------------------------
time.sleep(1)
if os.path.exists("/usr/local/sbin/john") or os.path.exists("/usr/local/bin/john") or  os.path.exists("/usr/sbin/john") or  os.path.exists("/usr/bin/john") or  os.path.exists("/bin/john") or  os.path.exists("/usr/local/games/john") or  os.path.exists("/usr/games/john") :
    print(f"{LIGHT_GREEN}john found{END}")
else:
    print(f"{LIGHT_RED}john not found{END}")
    print(f"""{RED}the option
    [1] download received
    [2] skip""")
    john = input("Make your choice : ")
    if john == "1" :
        os.system(f"{END}apt install john ")
    if john == "2" :
        print(f"{LIGHT_GREEN}skip is done")
#--------------------------------
time.sleep(1)
if os.path.exists("/usr/local/sbin/gobuster") or os.path.exists("/usr/local/bin/gobuster") or  os.path.exists("/usr/sbin/gobuster") or  os.path.exists("/usr/bin/gobuster") or  os.path.exists("/bin/gobuster") or  os.path.exists("/usr/local/games/gobuster") or  os.path.exists("/usr/games/gobuster") :
    print(f"{LIGHT_GREEN}gobuster found{END}")
else:
    print(f"{LIGHT_RED}gobuster not found{END}")
    print(f"""{RED}the option
    [1] download received
    [2] skip""")
    gobuster = input("Make your choice : ")
    if gobuster == "1" :
        os.system(f"{END}apt install gobuster ")
    if gobuster == "2" :
        print(f"{LIGHT_GREEN}skip is done")
#--------------------------------
time.sleep(1)
if os.path.exists("/usr/local/sbin/wpscan") or os.path.exists("/usr/local/bin/wpscan") or  os.path.exists("/usr/sbin/wpscan") or  os.path.exists("/usr/bin/wpscan") or  os.path.exists("/bin/wpscan") or  os.path.exists("/usr/local/games/wpscan") or  os.path.exists("/usr/games/wpscan") :
    print(f"{LIGHT_GREEN}wpscan found{END}")
else:
    print(f"{LIGHT_RED}wpscan not found{END}")
    print(f"""{RED}the option
    [1] download received
    [2] skip""")
    wpscan = input("Make your choice : ")
    if wpscan == "1" :
        os.system(f"{END}apt install wpscan ")
    if wpscan == "2" :
        print(f"{LIGHT_GREEN}skip is done")
#-----------------------
os.system("chmod +x obsidian-tools/* ; chmod +x obsid ; mv obsidian-tools /root/ ; mv obsid /bin;rm *;")
if os.path.exists("/bin/obsid") and os.path.exists("/root/obsidian-tools") :
    print(LIGHT_CYAN+"done")
    print("to start tool type (obsid)"+END)
else :
    print("eror")
