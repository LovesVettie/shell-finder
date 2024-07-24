import urllib.request
import os
import time
import sys
import colorama
from colorama import Fore, Back, Style

colorama.init()

banner = """
 $$$$$$\  $$\                 $$\ $$\        $$$$$$\  $$\                 $$\                     
$$  __$$\ $$ |                $$ |$$ |      $$  __$$\ \__|                $$ |                    
$$ /  \__|$$$$$$$\   $$$$$$\  $$ |$$ |      $$ /  \__|$$\ $$$$$$$\   $$$$$$$ | $$$$$$\   $$$$$$\  
\$$$$$$\  $$  __$$\ $$  __$$\ $$ |$$ |      $$$$\     $$ |$$  __$$\ $$  __$$ |$$  __$$\ $$  __$$\ 
 \____$$\ $$ |  $$ |$$$$$$$$ |$$ |$$ |      $$  _|    $$ |$$ |  $$ |$$ /  $$ |$$$$$$$$ |$$ |  \__|
$$\   $$ |$$ |  $$ |$$   ____|$$ |$$ |      $$ |      $$ |$$ |  $$ |$$ |  $$ |$$   ____|$$ |      
\$$$$$$  |$$ |  $$ |\$$$$$$$\ $$ |$$ |      $$ |      $$ |$$ |  $$ |\$$$$$$$ |\$$$$$$$\ $$ |      
 \______/ \__|  \__| \_______|\__|\__|      \__|      \__|\__|  \__| \_______| \_______|\__|      
                                                                                                  
                                                                                                  
                                [BY H04x - For TurkHackTeam.org]
                                                                                                  
"""

print(Fore.MAGENTA)
print(banner)
print(Fore.RED)
print("[i] Tüm Sorumluluk Kullanıcıya Aittir")

print(Fore.BLUE)

print("                                                                       ")
url = input("WebShell Taranacak Website\n > ")

print("                                                                                        ")
passe = ('a.php','b.php','c.php','1.php','2.php','3.php','alfa.php','alpha.php','marujiana.php','backdoor.php','shell.php','admin/a.php','admin/b.php','admin/c.php','admin/1.php','admin/2.php','admin/3.php','admin/alfa.php','admin/alpha.php','admin/marujiana.php','admin/backdoor.php','admin/shell.php',)
for hani in passe :
    curl = url+hani
    try :
        openurl = urllib.request.urlopen(curl)
        print(Fore.GREEN)
        print("[+]Bulundu  " +curl)
    except urllib.error.URLError as msg :
        print(Fore.RED)
        print ("[-]Bulunamadı  " +curl)