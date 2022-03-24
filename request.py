from random import random

import requests
from urllib import parse,request
# payload={'key1':"value1", 'key2':'value2'}
# r=requests.get('http://github.com')
# print(r.url)
# print(r.status_code)
# print(r.cookies)
# print(r.history)

# print(r.json())
# print(r.encoding)
# print(r.content)
def parses(s):
   list=[]
   strings=[]
   i=0
   while i<len(s):
       if s[i]=='?' or s[i]=='&':
           list.append(i)
       i=i+1
   # list.append(len(s))
   i=0
   while i<len(list)-1:
       strings.append(s[list[i]+1:list[i+1]])
       i=i+1

   for s in strings:
       print(parse.unquote(s))

# string='/ptqrlogin?u1=https%3A%2F%2Fqzs.qq.com%2Fqzone%2Fv5%2Floginsucc.html%3Fpara%3Dizone&ptqrtoken=792063322&ptredirect=0&h=1&t=1&g=1&from_ui=1&ptlang=2052&action=1-1-1646622674793&js_ver=22022415&js_type=1&login_sig=0i68fra2b76diBNDH4C3CBN*oNEbmHSjCx-AxAirxJ6H*hRCMEEAjjCDX6yTI6qF&pt_uistyle=40&aid=549000912&daid=5&ptdrvs=OuNBRhkUMj*oCSDEtv1Gm3o0dXaPkTexe2bJkI-lggn3nBDC2xAsRhmLLHXpJ72J&sid=4702533340117694413& HTTP/1.1'
# #decode url_encode from string to ascii
# # s=parse.unquote(string)
#
# # print(string)
# # print(s)
# parses(string)

url='http://docs.python-requests.org/zh_CN/latest/_static/requests-sidebar.png'
headers = {
  "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}
r=requests.get(url,headers=headers)
# print(r.status_code)
# print(r.text)
# print(r.headers)
# print(r.request.headers)
with open('image.png','wb') as f:
  f.write(r.content)

