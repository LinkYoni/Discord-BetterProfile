import os, colorama, discord, json, requests, atexit
from colorama import Fore, Style
from getpass import getpass
from time import sleep

import logos

with open('config.json', encoding="utf-8") as i:
    config = json.load(i)
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
BetterProfile = discord.Client()
token = None

def loop():
    while True:
        try:
            BetterProfile.run(token, bot=False)
        except:
            break
    clear()
    exit()

def streaming():
    clear()
    print(logos.correct)
    StreamingName = input(f'{Fore.GREEN} [-] {Fore.RESET}Name (press enter to get it from the config): ')
    clear()
    print(logos.correct)
    @BetterProfile.event
    async def on_ready():
        StreamingDefault = config['StreamingDefault']
        if StreamingName != "":
            print(f" {Fore.YELLOW}Assigned presence with{Fore.RED} Streaming {Fore.YELLOW}mode and name {Fore.RED}{StreamingName}")
            await BetterProfile.change_presence(activity=discord.Streaming(name=StreamingName, url='https://www.twitch.tv/yoni'))
        else:
            print(f" {Fore.YELLOW}Assigned presence with{Fore.RED} Streaming {Fore.YELLOW}mode and name {Fore.RED}{StreamingDefault}")
            await BetterProfile.change_presence(activity=discord.Streaming(name=StreamingDefault, url='https://www.twitch.tv/yoni'))
    loop()

def playing():
    clear()
    print(logos.correct)
    PlayingName = input(f'{Fore.GREEN} [-] {Fore.RESET}Name (press enter to get it from the config): ')
    clear()
    print(logos.correct)
    @BetterProfile.event
    async def on_ready():
        PlayingDefault = config['PlayingDefault']
        if PlayingName != "":
            print(f" {Fore.YELLOW}Assigned presence with{Fore.RED} Playing {Fore.YELLOW}mode and name {Fore.RED}{PlayingName}")
            await BetterProfile.change_presence(activity=discord.Game(name=PlayingName))
        else:
            print(f" {Fore.YELLOW}Assigned presence with{Fore.RED} Playing {Fore.YELLOW}mode and name {Fore.RED}{PlayingDefault}")
            await BetterProfile.change_presence(activity=discord.Game(name=PlayingDefault))
    loop()

def watching():
    clear()
    print(logos.correct)
    WatchingName = input(f'{Fore.GREEN} [-] {Fore.RESET}Name (press enter to get it from the config): ')
    clear()
    print(logos.correct)
    @BetterProfile.event
    async def on_ready():
        WatchingDefault = config['WatchingDefault']
        if WatchingName != "":
            print(f" {Fore.YELLOW}Assigned presence with{Fore.RED} Watching {Fore.YELLOW}mode and name {Fore.RED}{WatchingName}")
            await BetterProfile.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=WatchingName))
        else:
            print(f" {Fore.YELLOW}Assigned presence with{Fore.RED} Watching {Fore.YELLOW}mode and name {Fore.RED}{WatchingDefault}")
            await BetterProfile.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=WatchingDefault))
    loop()

def listening():
    clear()
    print(logos.correct)
    ListeningName = input(f'{Fore.GREEN} [-] {Fore.RESET}Name (press enter to get it from the config): ')
    clear()
    print(logos.correct)
    @BetterProfile.event
    async def on_ready():
        ListeningDefault = config['ListeningDefault']
        if ListeningName != "":
            print(f" {Fore.YELLOW}Assigned presence with{Fore.RED} Listening {Fore.YELLOW}mode and name {Fore.RED}{ListeningName}")
            await BetterProfile.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=ListeningName))
        else:
            print(f" {Fore.YELLOW}Assigned presence with{Fore.RED} Listening {Fore.YELLOW}mode and name {Fore.RED}{ListeningDefault}")
            await BetterProfile.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=ListeningDefault))
    loop()

def animated_status():
    clear()
    print(logos.correct)
    dic = {
        "1": [config['animated_status']['messages']['1'], config['animated_status']['emojis']['1']],
        "2": [config['animated_status']['messages']['2'], config['animated_status']['emojis']['2']],
        "3": [config['animated_status']['messages']['3'], config['animated_status']['emojis']['3']],
        "4": [config['animated_status']['messages']['4'], config['animated_status']['emojis']['4']]
    }
    if config['animated_status']['messages']['1'] == '' and config['animated_status']['emojis']['1'] == '': del dic['1']
    if config['animated_status']['messages']['2'] == '' and config['animated_status']['emojis']['2'] == '': del dic['2']
    if config['animated_status']['messages']['3'] == '' and config['animated_status']['emojis']['3'] == '': del dic['3']
    if config['animated_status']['messages']['4'] == '' and config['animated_status']['emojis']['4'] == '': del dic['4']

    def all_blank(number):
        try:
            dic[f'{number}']
            return ''
        except:
            return '(Will not run)'

    try:
        int(config['animated_status']['interval'])
    except:
        try:
            float(config['animated_status']['interval'])
        except:
            clear()
            print(logos.fail)
            print(f'{Fore.RED} [-] {Fore.RESET}Interval (in config.json) must be a number\n')
            getpass("")

    print(f" {Fore.MAGENTA}Interval: {Fore.GREEN}{config['animated_status']['interval']}\n")
    print(f" {Fore.CYAN}1 {Fore.YELLOW}-> {Fore.MAGENTA}Message: {Fore.GREEN}{config['animated_status']['messages']['1'] if config['animated_status']['messages']['1'] != '' else f'{Fore.RED}-'} {Fore.RESET}| {Fore.MAGENTA}Emoji: {config['animated_status']['emojis']['1'] if config['animated_status']['emojis']['1'] != '' else f'{Fore.RED}-'} {all_blank(1)}")
    print(f" {Fore.CYAN}2 {Fore.YELLOW}-> {Fore.MAGENTA}Message: {Fore.GREEN}{config['animated_status']['messages']['2'] if config['animated_status']['messages']['2'] != '' else f'{Fore.RED}-'} {Fore.RESET}| {Fore.MAGENTA}Emoji: {config['animated_status']['emojis']['2'] if config['animated_status']['emojis']['2'] != '' else f'{Fore.RED}-'} {all_blank(2)}")
    print(f" {Fore.CYAN}3 {Fore.YELLOW}-> {Fore.MAGENTA}Message: {Fore.GREEN}{config['animated_status']['messages']['3'] if config['animated_status']['messages']['3'] != '' else f'{Fore.RED}-'} {Fore.RESET}| {Fore.MAGENTA}Emoji: {config['animated_status']['emojis']['3'] if config['animated_status']['emojis']['3'] != '' else f'{Fore.RED}-'} {all_blank(3)}")
    print(f" {Fore.CYAN}4 {Fore.YELLOW}-> {Fore.MAGENTA}Message: {Fore.GREEN}{config['animated_status']['messages']['4'] if config['animated_status']['messages']['4'] != '' else f'{Fore.RED}-'} {Fore.RESET}| {Fore.MAGENTA}Emoji: {config['animated_status']['emojis']['4'] if config['animated_status']['emojis']['4'] != '' else f'{Fore.RED}-'} {all_blank(4)}")

    def exit_handler():
        requests.patch("https://discord.com/api/v9/users/@me/settings", headers={"authorization": token,"content-type": "application/json"}, data=json.dumps({"custom_status":None}))

    atexit.register(exit_handler)
    while True:
        try:
            for a in dic:
                requests.patch("https://discord.com/api/v9/users/@me/settings", headers={"authorization": token,"content-type": "application/json"}, data=json.dumps({"custom_status":{"text":dic[a][0],"emoji_name":dic[a][1]}}))
                try:
                    sleep(int(config['animated_status']['interval']))
                except:
                    sleep(float(config['animated_status']['interval']))
        except:
            clear()
            break