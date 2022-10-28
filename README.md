# ip-address-int

Add some extra information about an IP address to the output files.
Make sure that you have the geolite databases ad an abuseipdb.com API key

In my `.env` file i have

```
# Development settings
OUTPUT=/home/sebastian/Code/ip-address-int/output/
ABUSEIPDB_KEY=key
MAXMIND_CITY_MMDB=maxmind/GeoLite2-City.mmdb
MAXMIND_ASN_MMDB=maxmind/GeoLite2-ASN.mmdb
```