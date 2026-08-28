# Write a regex to extract `timestamp`, `host`, `process`, `pid`, `attempted_user`, `source_ip`, and `source_port`.​
# May 20 10:45:12 app-prod sshd[9214]: Failed password for invalid user admin from 203.0.113.9 port 51422 ssh2​

import re
log = "May 20 10:45:12 app-prod sshd[9214]: Failed password for invalid user admin from 203.0.113.9 port 51422 ssh2"
pattern = r'^(?P<timestamp>[A-Z][a-z]{2}\s+\d+\s+\d{2}:\d{2}:\d{2})\s+(?P<host>\S+)\s+(?P<process>\w+)\[(?P<pid>\d+)\]:\s+Failed password for invalid user\s+(?P<attempted_user>\S+)\s+from\s+(?P<source_ip>\d{1,3}(?:\.\d{1,3}){3})\s+port\s+(?P<source_port>\d+)\s+ssh2$'
match = re.match(pattern, log)
if match:
    print("Timestamp:", match.group("timestamp"))
    print("Host:", match.group("host"))
    print("Process:", match.group("process"))
    print("PID:", match.group("pid"))
    print("Attempted User:", match.group("attempted_user"))
    print("Source IP:", match.group("source_ip"))
    print("Source Port:", match.group("source_port"))
else:
    print("No match found")