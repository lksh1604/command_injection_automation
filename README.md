# Command Injection Automation

&nbsp; &nbsp; &nbsp; &nbsp;A Command Injection vulnerability is among the most critical types of vulnerabilities. It allows us to execute system commands directly on the back-end hosting server, which could lead to compromising the entire network. If a web application uses user-controlled input to execute a system command on the back-end server to retrieve and return specific output, we may be able to inject a malicious payload to subvert the intended command and execute our commands.

 &nbsp; &nbsp; &nbsp; &nbsp;This python program uses requests module to interact with the website. When the target url and the parameters are given it checks for the valid command separator symbol and passes the "whoami" command to check whether the website is vulnerable to command injection. It also obfuscates the commands to bypass if the command is blacklisted by the website.

    usage:  cmd_inj.py [-h] -u URL -p PARAM -m METHOD [-w WHITELIST_CHARACTER]


## optional arguments:


      -h, --help                  show this help message and exit
      -u URL, --url URL           Enter the target url
      -p PARAM, --param PARAM     Enter parameter to pass the injection
      -m METHOD, --method METHOD  Choose POST or GET method
      -w WHITELIST_CHARACTER, --whitelist_character WHITELIST_CHARACTER
                                  Specify if any whitelisted characters have to be passed

## Example:

      python3 command_injection.py -u http://127.0.0.1/test.php -m post -p link -w http://

