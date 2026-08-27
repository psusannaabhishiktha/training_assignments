#Write a regex to extract `ip`, `timestamp`, `method`, `path`, `status`, `bytes`, and `user_agent`.​
#10.2.4.8 - - [20/May/2026:10:21:09 +0000] "POST /api/orders HTTP/1.1" 201 342 "curl/8.1"​

import re
log = '10.2.4.8 - - [20/May/2026:10:21:09 +0000] "POST /api/orders HTTP/1.1" 201 342 "curl/8.1"'
pattern = r'^(?P<ip>\d{1,3}(?:\.\d{1,3}){3})\s-\s-\s\[(?P<timestamp>[^\]]+)\]\s"(?P<method>GET|POST|PUT|DELETE|PATCH|HEAD|OPTIONS)\s(?P<path>\S+)\sHTTP\/(?P<http_version>\d\.\d)"\s(?P<status>\d{3})\s(?P<bytes>\d+)\s"(?P<user_agent>[^"]+)"$'
match = re.match(pattern, log)
if match:
    print("IP:", match.group("ip"))
    print("Timestamp:", match.group("timestamp"))
    print("Method:", match.group("method"))
    print("Path:", match.group("path"))
    print("Status:", match.group("status"))
    print("Bytes:", match.group("bytes"))
    print("User Agent:", match.group("user_agent"))
else:
    print("No match found")