import sys
import os
import geoip2.database
import socket
import csv
import json
from pathlib import Path
import pandas as pd
from dotenv import dotenv_values

import folium
from folium.plugins import MarkerCluster

# Cload configuration from .env file
config = dotenv_values(".env")

if len(sys.argv) > 1:
    filepath = sys.argv[1]
else:
    print("Please specify a filename")
    sys.exit()

if not os.path.isfile(filepath):
    print("File path {} does not exist. Exiting...".format(filepath))
    sys.exit()

# Generate output filenames
input_filename = os.path.basename(Path(filepath))
output_file_json = config.get("OUTPUT") + input_filename + ".json"
output_file_csv = config.get("OUTPUT") + input_filename + ".csv"
print(output_file_json)
print(output_file_csv)

ip_intel_bucket = []

with open(filepath) as fp:
    for line in fp:
        ip_intel = {}
        ip_address = format(line.strip())
        try:
            socket.inet_aton(ip_address)
        except socket.error:
            continue

        ip_intel['ip_address'] = ip_address

        with geoip2.database.Reader(config.get("MAXMIND_CITY_MMDB")) as reader:
            try:
                response = reader.city(ip_address)
                ip_intel['country_code'] = response.country.iso_code
                ip_intel['city'] = response.city.name
                ip_intel['lat'] = response.location.latitude
                ip_intel['lon'] = response.location.longitude
            except geoip2.errors.AddressNotFoundError:
                pass
            except:
                print("Something else went wrong") 
        
        # print(ip_intel)
        ip_intel_bucket.append(ip_intel)

keys = ip_intel_bucket[0].keys()

with open(output_file_csv, 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(ip_intel_bucket)

csv_data = pd.read_csv(output_file_csv)

print(f"Total IP addresses: { len(csv_data) }")
print(f"Unique IP addresses: { len(csv_data['ip_address'].unique()) }")
print(f"Unique Cities: { len(csv_data['city'].unique()) }")

csv_data.groupby('city').count()
df = csv_data.groupby(['city','country_code','lat','lon']).size().reset_index(name='counts')
print(df)


# df = top_cities.to_frame()
# df.reset_index(inplace=True)
# df = df.rename(columns = {'index':'cityname'})
# print(df)

#for index, row in df.iterrows():
#    print(index)
#    print(row['country_code'])
#    print(geolocate(row['country_code']))

#empty map
world_map= folium.Map(tiles="cartodbpositron")
marker_cluster = MarkerCluster().add_to(world_map)
#for each coordinate, create circlemarker of user percent
for i in range(len(df)):
        lat = df.iloc[i]['lat']
        long = df.iloc[i]['lon']
        radius=5
        popup_text = """City : {}<br>
                    %of Users : {}<br>"""
        popup_text = popup_text.format(df.iloc[i]['city'],
                                   df.iloc[i]['counts']
                                   )
        folium.CircleMarker(location = [lat, long], radius=radius, popup= popup_text, fill =True).add_to(marker_cluster)
#show the map
#world_map

world_map.save("citymap.html")