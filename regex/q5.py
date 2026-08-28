# Write a regex to extract `user`, `action`, `branch`, `target`, `result`, and `files`.​
# git user=riya action=merge branch=feature/login target=main result=conflict files=3​

import re
log = "git user=riya action=merge branch=feature/login target=main result=conflict files=3"
pattern = r'^git\s+user=(?P<user>\S+)\s+action=(?P<action>\S+)\s+branch=(?P<branch>\S+)\s+target=(?P<target>\S+)\s+result=(?P<result>\S+)\s+files=(?P<files>\d+)$'
match = re.match(pattern, log)
if match:
    print("User   :", match.group("user"))
    print("Action :", match.group("action"))
    print("Branch :", match.group("branch"))
    print("Target :", match.group("target"))
    print("Result :", match.group("result"))
    print("Files  :", match.group("files"))
else:
    print("No match found")