# LBP-Rate
A basic Python Script that scrapes the LBP rate from LiraRate website while bypassing Ogero's block.

# About
Since LiraRate does not have a public API, I have developed a small script that scrapes the price.
The script was written in Python 3.9 by Mrknol.

You'll require to install these modules prior to running the script:

- Selenium
- Chromedriver (place in Python folder or drop anywhere but create a variable that'll link to Chromedriver's path.)

# Errors you might encounter

In the code provided, I have included a proxy which might stop working after a certain period of time. Thus, consider replacing the IP, Port.

https://free-proxy-list.net/ You can select a proxy from here.

If the proxy is too slow, it could cause a timeout which will not yield any result.

The website LiraRate is protected by Cloudflare, so sometimes it asks certain IPs to fill a captcha which will cause the script to show no values.

# Enjoy!

