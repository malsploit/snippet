#!/usr/bin/python
import os
import sys
import pygeoip
import urllib2
import StringIO
import gzip
#sys.tracebacklimit = 0
def ipLocator(ip):
	GeoIPDatabase = 'GeoLiteCity.dat'
	ipData = pygeoip.GeoIP(GeoIPDatabase)
	record = ipData.record_by_name(ip)
	print("%s %s,%s" % (ip, record['city'], record['country_name']))

def read_file_parse_ip():
	for ip in open(sys.argv[1], 'r'):
		try:
			ip=ip.strip()
			ipLocator(ip)
  		except TypeError as e:
			print("Ip invalid: %s" % (ip))
read_file_parse_ip()


def download_db():
	baseURL = "http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz"
	outFilePath = "GeoLiteCity.dat"
	response = urllib2.urlopen(baseURL)
	compressedFile = StringIO.StringIO()
	compressedFile.write(response.read())
	compressedFile.seek(0)
	decompressedFile = gzip.GzipFile(fileobj=compressedFile, mode='rb')
	with open(outFilePath, 'w') as outfile:
		outfile.write(decompressedFile.read())

if not os.path.exists('GeoLiteCity.dat'):
	download_db()
	print("Fisierul a fost descarcat")


