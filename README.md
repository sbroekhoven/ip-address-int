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

Thins work quite simple.

```
# run command with input file
$ python maxmind_example.py input/samples.txt

# Get some output
/home/sebastian/Code/ip-address-int/output/samples.txt.json
/home/sebastian/Code/ip-address-int/output/samples.txt.csv
Total IP addresses: 6084
Unique IP addresses: 5389

AS-COLOCROSSING                              846
SERVER-MANIA                                 818
JSC ER-Telecom Holding                        97
PT Telekomunikasi Indonesia                   91
Aljeel-net                                    89
DIGITALOCEAN-ASN                              86
COMCAST-7922                                  77
OVH SAS                                       53
EPM Telecomunicaciones S.A. E.S.P.            46
Triple T Broadband Public Company Limited     45
TV AZTECA SUCURSAL COLOMBIA                   42
TOT Public Company Limited                    41
Zwiebelfreunde e.V.                           37
NEDETEL S.A.                                  35
Contabo GmbH                                  33
Chinanet                                      30
ATT-INTERNET4                                 28
UFINET PANAMA S.A.                            28
Alibaba US Technology Co., Ltd.               28
VNPT Corp                                     27
Name: organization, dtype: int64

United States     2055
Indonesia          619
Russia             292
Colombia           208
Brazil             203
India              188
Germany            142
Thailand           137
Ukraine            112
Mexico             112
Libya              107
China              106
Bangladesh         101
Argentina           74
Ecuador             72
United Kingdom      69
Iran                62
Iraq                58
France              57
Peru                56
Name: country, dtype: int64

Buffalo          380
Los Angeles      258
Chicago           92
Tripoli           90
New York          84
Jakarta           72
Dallas            69
Moscow            67
San Jose          52
Atlanta           45
Seattle           45
Bekasi            40
Bangkok           36
Bogotá            36
Dhaka             34
San Francisco     33
Denver            32
Salem             31
Honolulu          30
Singapore         30
Name: city, dtype: int64

                                           organization  organization
AS-COLOCROSSING                                     846      0.139076
SERVER-MANIA                                        818      0.134473
JSC ER-Telecom Holding                               97      0.015946
PT Telekomunikasi Indonesia                          91      0.014960
Aljeel-net                                           89      0.014631
DIGITALOCEAN-ASN                                     86      0.014138
COMCAST-7922                                         77      0.012658
OVH SAS                                              53      0.008713
EPM Telecomunicaciones S.A. E.S.P.                   46      0.007562
Triple T Broadband Public Company Limited            45      0.007398
TV AZTECA SUCURSAL COLOMBIA                          42      0.006904
TOT Public Company Limited                           41      0.006740
Zwiebelfreunde e.V.                                  37      0.006083
NEDETEL S.A.                                         35      0.005754
Contabo GmbH                                         33      0.005425
Chinanet                                             30      0.004932
ATT-INTERNET4                                        28      0.004603
UFINET PANAMA S.A.                                   28      0.004603
Alibaba US Technology Co., Ltd.                      28      0.004603
VNPT Corp                                            27      0.004439
```

And in CSV format:

| ip_address      | country_code | country       | subdivisions               | city                     | asn    | organization                                     |
| --------------- | ------------ | ------------- | -------------------------- | ------------------------ | ------ | ------------------------------------------------ |
| 129.159.88.228  | US           | United States | Virginia                   | Ashburn                  | 31898  | ORACLE-BMC-31898                                 |
| 129.18.210.126  | NG           | Nigeria       | Lagos                      | Lagos                    | 36923  | SWIFTNG-ASN                                      |
| 129.205.118.226 | NG           | Nigeria       | Lagos                      | Lagos                    | 37148  | globacom-as                                      |
| 129.222.7.145   | US           | United States | Illinois                   | Chicago                  | 14593  | SPACEX-STARLINK                                  |
| 129.227.133.105 | HK           | Hong Kong     |                            |                          | 21859  | ZEN-ECN                                          |
| 129.41.171.244  | US           | United States |                            |                          | 2002   | IBM-PV-AS                                        |
| 130.185.213.146 | BG           | Bulgaria      | Yambol                     | Yambol                   | 48917  | Optinet Ltd                                      |
| 130.193.43.127  | RU           | Russia        |                            |                          | 200350 | Yandex.Cloud LLC                                 |
| 131.0.226.198   | BR           | Brazil        | Pernambuco                 | Recife                   | 52965  | 1TELECOM SERVICOS DE TECNOLOGIA EM INTERNET LTDA |
| 131.100.49.23   | CO           | Colombia      | Departamento del Magdalena | Florencia                | 270062 | FIBERNET TV SAS                                  |
| 131.100.51.250  | CO           | Colombia      | Departamento del Caqueta   | El Doncello              | 270062 | FIBERNET TV SAS                                  |
| 131.108.118.27  | BR           | Brazil        | Goias                      | Catalao                  | 264353 | Catalao Bandnet Servicos Multimidia LTDA - ME    |
| 131.108.220.49  | BR           | Brazil        | Sergipe                    | Nossa Senhora do Socorro | 61693  | RODRIGO MATTARAGGIA - ME                         |
| 131.108.51.5    | BR           | Brazil        | Bahia                      | Jeremoabo                | 61687  | PRO NET EMPREENDIMENTOS TECNOLOGICOS LTDA        |