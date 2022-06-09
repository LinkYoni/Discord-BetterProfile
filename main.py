import os, colorama, json, requests
from colorama import Fore
from getpass import getpass

import logos

colorama.init()

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
clear()

with open('config.json', encoding="utf-8") as i:
    config = json.load(i)

users_list = []
tkns_checked = 0

for use_tkn in config['tokens']:
	tkns_checked += 1
	headers={"authorization": config['tokens'][use_tkn],"content-type": "application/json"}
	res = requests.get(f'https://discordapp.com/api/v6/users/@me', headers=headers) #check if the given token is valid
	if config['tokens'][use_tkn] == '':
		users_list.append('X')
	elif res.status_code == 200:
		res_json = res.json()
		user_name = f"{res_json['username']}#{res_json['discriminator']}"
		users_list.append(user_name)
	else:
		clear()
		print(logos.fail)
		print(f'{Fore.RED} [-] {Fore.RESET}One/some of the tokens provided is/are invalid\n     Error in {Fore.RED}token{tkns_checked} {Fore.RESET}and/or more')
		getpass("")

if users_list[0] == 'X' and users_list[1] == 'X' and users_list[2] == 'X':
	clear()
	print(logos.fail)
	print(f'{Fore.RED} [-] {Fore.RESET}There must be at least 1 valid token\n')
	getpass("")

print(logos.default)
print(f" {Fore.CYAN}Account 1{Fore.YELLOW} --> {Fore.MAGENTA}{users_list[0] if users_list[0] != 'X' else f'{Fore.RED}-'}")
print(f" {Fore.CYAN}Account 2{Fore.YELLOW} --> {Fore.MAGENTA}{users_list[1] if users_list[1] != 'X' else f'{Fore.RED}-'}")
print(f" {Fore.CYAN}Account 3{Fore.YELLOW} --> {Fore.MAGENTA}{users_list[2] if users_list[2] != 'X' else f'{Fore.RED}-'}")

choose_tkn = input(f"\n{Fore.CYAN} [-] {Fore.RESET}Choose an account (type -> {f'{Fore.GREEN}' if users_list[0] != 'X' else f'{Fore.RED}'}1{Fore.RESET}, {f'{Fore.GREEN}' if users_list[1] != 'X' else f'{Fore.RED}'}2{Fore.RESET} or {f'{Fore.GREEN}' if users_list[2] != 'X' else f'{Fore.RED}'}3{Fore.RESET}): ")
if (choose_tkn == '1' and users_list[0] == 'X') or (choose_tkn == '2' and users_list[1] == 'X') or (choose_tkn == '3' and users_list[2] == 'X'):
	clear()
	print(logos.fail)
	print(f'{Fore.RED} [-] {Fore.RESET}Invalid Account choosen\n')
	getpass("")
if choose_tkn == '1': token = config['tokens']['token1']
elif choose_tkn == '2': token = config['tokens']['token2']
elif choose_tkn == '3': token = config['tokens']['token3']
else:
	clear()
	print(logos.fail)
	print(f'{Fore.RED} [-] {Fore.RESET}Invalid Option\n')
	getpass("")
clear()

user_name = users_list[int(choose_tkn)-1]
print(logos.default)
print(f' {Fore.YELLOW}Logged as {Fore.RED}{user_name}\n{Fore.RESET}')
print(f''' {Fore.GREEN}Presences:
  {Fore.CYAN}1{Fore.YELLOW} --> {Fore.MAGENTA}Streaming
  {Fore.CYAN}2{Fore.YELLOW} --> {Fore.MAGENTA}Playing
  {Fore.CYAN}3{Fore.YELLOW} --> {Fore.MAGENTA}Watching
  {Fore.CYAN}4{Fore.YELLOW} --> {Fore.MAGENTA}Listening
 {Fore.GREEN}Animated:
  {Fore.CYAN}5{Fore.YELLOW} --> {Fore.MAGENTA}Animated status
{Fore.RESET}''')

option = input(f'{Fore.CYAN} [-] {Fore.RESET}Option: ')

import options
options.token = token
if option == '1': options.streaming()
elif option == '2': options.playing()
elif option == '3': options.watching()
elif option == '4': options.listening()
elif option == '5': options.animated_status()
else:
	clear()
	print(logos.fail)
	print(f'{Fore.RED} [-] {Fore.RESET}Invalid Option\n')
	getpass("")