# pwn_wp_duplicator


Find some possible targets with thjis google dork:
inurl:"/wp-content/plugins/duplicator/"

-------------------------------------

You can generate a list of all IPv4 Addresses on the internetr with the one script and then try to nslookup them and create a list to try to pwn....or however you wanna use it.

Just look at the code and figure out how to use PoC (which isnt acutally a PoC just a tool)

```python
PoC_duplicator.py example.com
PoC_duplicator.py www.example.com

NOT http:// or https://
```

I hope someone takes this code an re-writes it a little smarter, it is very eeasy too check version of duplicator before stupidly trying to run this. As well as obfuscate the payload as EVERY WAF picks it up instnant.
