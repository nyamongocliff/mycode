#!/usr/bin/env python3
"""Returning the location of the ISS in latitude/longitude"""
import requests
import datetime
import reverse_geocoder as rg


URL= "http://api.open-notify.org/iss-now.json"
def main():
    resp= requests.get(URL).json()
    longitude = resp["iss_position"]["longitude"]
    latitude= resp["iss_position"]["latitude"] 
    timestamp = resp["timestamp"]
    timestamp = datetime.datetime.fromtimestamp(timestamp)
     
    locator_resp= rg.search((latitude, longitude))

    # slice that object to return the city name only
    city= locator_resp[0]["name"]

    # slice the object again to return the country
    country= locator_resp[0]["cc"]

    print(f"Timestamp: {timestamp}")
    print(f"CURRENT LOCATION OF THE ISS:\nLon: {longitude}\nLat: {latitude}")
    print(f"City/Country: {city}, {country}")
if __name__ == "__main__":
    main()
