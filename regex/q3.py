# Write a regex to extract `level`, `process`, `pid`, `queue`, `retry`, and `message`.​
# WARN payment-worker pid=3421 queue=refunds retry=3 message="timeout calling bank gateway"​

import re
log = 'WARN payment-worker pid=3421 queue=refunds retry=3 message="timeout calling bank gateway"'
pattern = r'^(?P<level>\w+)\s+(?P<process>[\w-]+)\s+pid=(?P<pid>\d+)\s+queue=(?P<queue>\w+)\s+retry=(?P<retry>\d+)\s+message="(?P<message>[^"]+)"$'
match = re.match(pattern, log)
if match:
    print(match.groupdict())
else:
    print("Log format is invalid")    