# Write a regex to extract `container`, `event`, `exit_code`, `reason`, and `image`.​
# container=api-server event=die exit_code=137 reason=OOMKilled image=client-api:2026.05.20​

import re
log = "container=api-server event=die exit_code=137 reason=OOMKilled image=client-api:2026.05.20"
pattern = r'^container=(?P<container>\S+)\s+event=(?P<event>\S+)\s+exit_code=(?P<exit_code>\d+)\s+reason=(?P<reason>\S+)\s+image=(?P<image>\S+)$'
match = re.match(pattern, log)
if match:
    print("Container :", match.group("container"))
    print("Event     :", match.group("event"))
    print("Exit Code :", match.group("exit_code"))
    print("Reason    :", match.group("reason"))
    print("Image     :", match.group("image"))
else:
    print("No match found")