#!/usr/bin/python
import os
import sys
import time
import urllib2
import thread

def checkproxy(proxyurl):
   try:
      timeout = 5
      check = 'https://google.com'
      proxyip= proxyurl
      proxy = urllib2.ProxyHandler({'https': proxyip})
      req = urllib2.build_opener(proxy)
      req.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0')]
      response = req.open(check, timeout=timeout)
      myfile = response.read()
      if "google" in myfile:
         print proxyurl
   except:
      m = 0 # bogus variable
