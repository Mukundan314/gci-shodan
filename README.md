# A Shodan scanner for you terminal

### Installing Dependencies

```
pip install -r requirements.txt
```

### Usage

Getting you ip address:
```
$ python main.py myip
IP Address: <Your-IP-Address>
```

Getting information about a host:
```
$ python main.py host 8.8.8.8
city: None
region_code: None
os: None
tags: 
ip: 134744072
isp: Google
area_code: None
dma_code: None
last_update: 2019-12-20T15:10:16.017305
country_code3: USA
country_name: United States
hostnames: dns.google
postal_code: None
longitude: -97.822
country_code: US
ip_str: 8.8.8.8
latitude: 37.751000000000005
org: Google
asn: AS15169
ports: 53,443
```

Searching shodan:
```
$ python main.py search google
23.83.58.9           9001       Nobis Technology Group, LLC                        
154.212.165.11       9443       Abcde Group Company Limited                        
35.244.182.194       80         Google Cloud                                       194.182.244.35.bc.googleusercontent.com
154.201.53.4         9002       CloudInnovation infrastructure                     
35.244.220.241       80         Google Cloud                                       241.220.244.35.bc.googleusercontent.com
23.107.193.149       9000       Ubiquity Server Solutions Los Angeles              
13.76.46.245         8080       Microsoft Azure                                    
137.175.28.3         8139       Peg Tech                                           
35.186.231.240       80         Google Cloud                                       240.231.186.35.bc.googleusercontent.com
35.197.223.183       3306       Google Cloud                                       183.223.197.35.bc.googleusercontent.com
108.177.121.108      993        Google                                             
107.178.252.221      80         Google Cloud                                       221.252.178.107.bc.googleusercontent.com
35.244.243.50        80         Google Cloud                                       50.243.244.35.bc.googleusercontent.com
216.58.193.211       80         Google                                             lax02s23-in-f211.1e100.net,lax02s23-in-f19.1e100.net
173.194.176.200      554        Google                                             
104.198.240.123      25565      Google Cloud                                       123.240.198.104.bc.googleusercontent.com
34.102.151.47        80         Google                                             47.151.102.34.bc.googleusercontent.com
35.241.62.85         80         Google Cloud                                       85.62.241.35.bc.googleusercontent.com
192.145.98.50        8880       Tentorium Welnes LLC                               
14.128.36.169        444        BGPNET Global                                      
168.206.135.201      9000       The Atomic Energy Board                            
156.226.32.28        9002       CloudInnovation infrastructure                     
108.59.82.143        3306       Google Cloud                                       143.82.59.108.bc.googleusercontent.com
35.186.238.101       80         Google Cloud                                       101.238.186.35.bc.googleusercontent.com
...
34.98.102.10         80         Google Cloud                                       10.102.98.34.bc.googleusercontent.com
130.211.29.72        80         Google Cloud                                       72.29.211.130.bc.googleusercontent.com
35.247.219.100       3306       Google Cloud                                       100.219.247.35.bc.googleusercontent.com
34.73.186.111        3306       Google Cloud                                       111.186.73.34.bc.googleusercontent.com
173.194.176.20       554        Google                                             
35.201.66.130        80         Google Cloud                                       130.66.201.35.bc.googleusercontent.com
156.225.141.154      9943       CloudInnovation infrastructure                     
3.135.195.162        8081       Amazon.com                                         ec2-3-135-195-162.us-east-2.compute.amazonaws.com
195.154.30.192       80         Iliad-Entreprises                                  cdn2.lequipe.fr
34.98.68.92          80         Google Cloud                                       92.68.98.34.bc.googleusercontent.com
35.227.200.224       80         Google Cloud                                       224.200.227.35.bc.googleusercontent.com
156.225.143.123      9943       CloudInnovation infrastructure                     
34.102.183.255       80         Google                                             255.183.102.34.bc.googleusercontent.com
136.243.173.219      81         Hetzner Online GmbH                                static.219.173.243.136.clients.your-server.de
52.44.237.240        80         Amazon.com                                         ec2-52-44-237-240.compute-1.amazonaws.com
147.255.55.203       9943       Leaseweb USA                                       
173.194.54.70        554        Google                                             
35.201.109.138       80         Google Cloud                                       138.109.201.35.bc.googleusercontent.com
74.125.99.8          554        Google                                             
156.225.141.242      9000       CloudInnovation infrastructure                     
49.212.219.107       9000       SAKURA Internet                                    www9093ug.sakura.ne.jp
88.39.53.178         9000       Telecom Italia Business                            host178-53-static.39-88-b.business.telecomitalia.it
156.225.139.180      9000       CloudInnovation infrastructure                     
34.96.93.170         80         Google Cloud                                       170.93.96.34.bc.googleusercontent.com
35.197.190.178       3306       Google Cloud                                       178.190.197.35.bc.googleusercontent.com
```
