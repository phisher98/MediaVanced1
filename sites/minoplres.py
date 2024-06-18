from requests import get, post
from bs4 import BeautifulSoup
import re

mDefaultDomain = "https://minoplres.xyz/"
mTargetUrl = "https://minoplres.xyz/embed-wsv3xpda8n5j.html"
mHeaders = {
    'Referer': mDefaultDomain
}

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(f"\n{Colors.OKCYAN}TARGET: minoplres.xyz{Colors.ENDC}")

mPageResponse = get(mTargetUrl,headers = mHeaders)
mPageHtml = mPageResponse.text
print(mPageHtml)
mRegex = r'file:"([^"]+)"'
mMatch = re.search(mRegex, mPageHtml)
if mMatch:
    mUrl = mMatch.group(1)
    new_url = mUrl.replace(",l,h,.urlset/master.m3u8", "h/encryption.key")
    mPageResponse = get(new_url, headers=mHeaders)
    print(mPageResponse.text)
    print("######################")
    print("######################")
    print(f"Captured URL: {Colors.OKGREEN}{mUrl}{Colors.ENDC}")
    print("######################")
    print("######################\n")
    print(f"\n{Colors.WARNING}###Please use header Referer: https://minoplres.xyz or host to access the url")
    
else:
    print("URL not found.")
