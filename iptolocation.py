from ipstack import GeoLookup
import pandas as pd
def orient(ip):
  #geo_lookup = GeoLookup("431c444c2d03ca049a4356d7d7c897b7")
  geo_lookup = GeoLookup("f02b34fc34b84c40be72c2299657cef0")
  location = geo_lookup.get_location(ip)
  return(location)
k=orient(input())#ip
print("city",k['city'])
print("country",k['country_name'])
print("Latitude",k['latitude'])
print("Longitude",k['longitude'])


"""
Spyder Editor

This is a temporary script file.
"""

