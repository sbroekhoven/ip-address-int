import sys
import os
import geoip2.database
import socket
import csv
import json
from pathlib import Path
import pandas as pd
from dotenv import dotenv_values

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

# input_filename = Path(filepath)
input_filename = os.path.basename(Path(filepath))

# print(input_filename)
# output_file_json = filename_replace_ext = input_filename.with_suffix('.json')
# output_file_csv = filename_replace_ext = input_filename.with_suffix('.csv')

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
                ip_intel['country'] = response.country.name
                ip_intel['subdivisions'] = response.subdivisions.most_specific.name
                ip_intel['city'] = response.city.name
            except geoip2.errors.AddressNotFoundError:
                pass
            except:
                print("Something else went wrong") 

        with geoip2.database.Reader(config.get("MAXMIND_ASN_MMDB")) as asn_reader:
            try:
                asn_response = asn_reader.asn(ip_address)
                ip_intel['asn'] = asn_response.autonomous_system_number
                ip_intel['organization'] = asn_response.autonomous_system_organization
            except geoip2.errors.AddressNotFoundError:
                ip_intel['asn'] = ""
                ip_intel['organization'] = ""
            except:
                print("Something else went wrong") 
        
        # print(ip_intel)
        ip_intel_bucket.append(ip_intel)

keys = ip_intel_bucket[0].keys()

with open(output_file_csv, 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(ip_intel_bucket)

with open(output_file_json, 'w', encoding='utf-8') as fj:
    json.dump(ip_intel_bucket, fj, ensure_ascii=False, indent=2)

csv_data = pd.read_csv(output_file_csv)

print(f"Total IP addresses: { len(csv_data) }")
print(f"Unique IP addresses: { len(csv_data['ip_address'].unique()) }")

top_20_organizations = csv_data['organization'].value_counts(normalize=False).head(20)
top_20_organizations_n = csv_data['organization'].value_counts(normalize=True).head(20)
top_20_countries = csv_data['country'].value_counts(normalize=False).head(20)
top_20_cities = csv_data['city'].value_counts(normalize=False).head(20)

print(top_20_organizations)
print(top_20_countries)
print(top_20_cities)

top_20_organizations_ntf = pd.concat([top_20_organizations, top_20_organizations_n], axis=1).reindex(top_20_organizations.index)

print(top_20_organizations_ntf)

# with pd.ExcelWriter(output_file_xlsx, engine='xlsxwriter') as writer:  
#     top_20_organizations.to_excel(writer, sheet_name='top_20_organizations')
#     top_20_countries.to_excel(writer, sheet_name='top_20_countries')
#     top_20_cities.to_excel(writer, sheet_name='top_20_cities')
#     csv_data.to_excel(writer, sheet_name='all')

