import phonenumbers
from phonenumbers import geocoder, carrier
import folium
from opencage.geocoder import OpenCageGeocode

# OpenCage API Key
Key = "28296721f958445aafcbca9f600c0043"

# Input phone number with country code
number = input("Enter phone number with country code: ")

# Parse the phone number
check_number = phonenumbers.parse(number)

# Get location information
number_location = geocoder.description_for_number(check_number, "en")
print(f"Location: {number_location}")

# Get service provider information
service_provider = phonenumbers.parse(number)
print(f"Service Provider: {carrier.name_for_number(service_provider, 'en')}")

# Get coordinates using OpenCage Geocoding API
geocoder = OpenCageGeocode(Key)
results = geocoder.geocode(number)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(f"Latitude: {lat}, Longitude: {lng}")

# Create a folium map and add a marker for the location
map_location = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=f"{number_location}<br>{number}<br>{carrier.name_for_number(service_provider, 'en')}").add_to(map_location)

# Save the map to an HTML file
map_location.save("mylocation.html")
