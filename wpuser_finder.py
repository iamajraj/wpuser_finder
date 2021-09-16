# DON"T REMOVE BELOW AUTHOR LINE
# AUTHOR => AjRaj
# Github => github/iamajraj
import requests
import json
import os
from os import error, system, name
import time
# COLOR OPTION


class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
# CLEAR FUNCTION


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
# LOGO


def logo():
    print(bcolors.GREEN + bcolors.BOLD + """
           ____                      ,
          /---.'.__  WORDPRESS  ____//
               '--.\ USERNAME  /.---'
          _______  \\ FINDER  //
        /.------.\  \|      .'/  ______
       //  ___  \ \ ||/|\  //  _/_----.\__
      |/  /.-.\  \ \:|< >|// _/.'..\   '--'
         //   \'. | \'.|.'/ /_/ /  \\
        //     \ \_\/" ' ~\-'.-'    \\
       //       '-._| :A: |'-.__     \\
      //           (/'==='\)'-._\     ||
      ||                        \\    \|
      ||                         \\    '
      |/ AUTHOR: github/iamajraj  \\
                                   ||
                                   ||
                                   \\
                                    '""" + bcolors.ENDC)
# MAIN START


def main():
    clear()
    logo()
    print(bcolors.HEADER + "*******" + bcolors.UNDERLINE+"Welcome to WP Username Finder!" +
          bcolors.ENDC + bcolors.HEADER + "******" + bcolors.ENDC)
    print(bcolors.BLUE + "Select Options:")
    print("1. Find Username")
    print("2. Exit")
    inp = input("Choose: ")
    if inp == "1":
        clear()
        logo()
        print(bcolors.BLUE + "Enter the URL (www.example.com): ")
        try:
            url = input(":") + "/wp-json/wp/v2/users"
            response = requests.get(url)
            data = json.loads(response.text)
            result = data[0]["slug"]
            print("We Got It !")
            print("Username found: " + bcolors.GREEN + result + bcolors.ENDC)
        except error as e:
            print(bcolors.FAIL + "Something went wrong !")
    elif inp == "2":
        print("Have a nice day !")
        exit()
    else:
        print(bcolors.FAIL + "Invalid option selected. Exiting...")


main()
