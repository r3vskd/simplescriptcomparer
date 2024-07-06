import difflib
from colorama import Fore, Style, init

def display_banner():
    print(Fore.RED + '''   
███████  ██████  ██████ ██████  ██ ██████  ████████      ██████  ██████  ███    ███ ██████   █████  ██████  ███████ ██████  
██      ██      ██      ██   ██ ██ ██   ██    ██        ██      ██    ██ ████  ████ ██   ██ ██   ██ ██   ██ ██      ██   ██ 
███████ ██      ██      ██████  ██ ██████     ██        ██      ██    ██ ██ ████ ██ ██████  ███████ ██████  █████   ██████  
     ██ ██      ██      ██   ██ ██ ██         ██        ██      ██    ██ ██  ██  ██ ██      ██   ██ ██   ██ ██      ██   ██ 
███████  ██████  ██████ ██   ██ ██ ██         ██         ██████  ██████  ██      ██ ██      ██   ██ ██   ██ ███████ ██   ██                                                                                                                                                                                                                                                                                                                            
 Author: r3vskd                 
          ''' + Style.RESET_ALL)
    
script1=input("Por favor ingresa el nombre del primer archivo con su ruta ===> ")
script2=input("Ahora ingresa el combre del segundo archivo que quieras comparar ===> ")

try:
    with open(script1, 'r') as file1:
        file1_info = file1.readlines()
        
        with open(script2, 'r') as file2:
            file2_info = file2.readlines()
            
            diff = difflib.unified_diff(
                file1_info, file2_info, fromfile=script1,
                tofile=script2, lineterm = '' 
            )
            
            for line in diff:
                print(line)
                
except FileNotFoundError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error has occurred : {e}")            
                

#def comparador():
#    difflib.SequenceMatcher(None, script1.read(), script2.read())
#    for line in difflib.unified_diff(script1, script2):
#        print(line)
#        comparador()
#
#def func():
#    #text1 = open('sample1.txt').readlines()
#    #text2 = open('sample2.txt').readlines()
#    for line in difflib.unified_diff(script1, script2):
#        print(line)
#
#func()