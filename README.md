# Command Injection Automation
usage: cmd_inj.py [-h] -u URL -p PARAM -m METHOD [-w WHITELIST_CHARACTER]

Simple Automated Command Injection

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     Enter the target url
  -p PARAM, --param PARAM
                        Enter parameter to pass the injection
  -m METHOD, --method METHOD
                        Choose POST or GET method
  -w WHITELIST_CHARACTER, --whitelist_character WHITELIST_CHARACTER
                        Specify if any whitelisted characters have to be passed
