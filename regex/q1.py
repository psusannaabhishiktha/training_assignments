# Write a regex to extract `timestamp`, `level`, `user`, `endpoint`, `status`, and `latency_ms`.​
# 2026-05-20 10:15:22 ERROR user=alice endpoint=/api/payments status=500 latency_ms=842​

import re
log = "2026-05-20 10:15:22 ERROR user=alice endpoint=/api/payments status=500 latency_ms=842"
pattern = r'^(?P<timestamp>\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2})\s(?P<level>\w+)\suser=(?P<user>\w+)\sendpoint=(?P<endpoint>\S+)\sstatus=(?P<status>\d+)\slatency_ms=(?P<latency_ms>\d+)$'
match = re.match(pattern, log)
if match:
    print("Timestamp :", match.group("timestamp"))
    print("Level     :", match.group("level"))
    print("User      :", match.group("user"))
    print("Endpoint  :", match.group("endpoint"))
    print("Status    :", match.group("status"))
    print("Latency   :", match.group("latency_ms"))
else:
    print("No match found")
