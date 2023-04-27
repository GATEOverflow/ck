import sys
import os
import cmind as cm
import check as checks
import json

files=sys.argv[1:]

for file in files:
  if not file.endswith("_cm.json"):
    continue
  script_path = os.path.dirname(file)
  f = open(file)
  data = json.load(f)
  automation_uid = data['automation_uid']
  r = cm.access({'action':'doc', 'automation':f'script,{automation_uid}', 'quiet': 'yes'})
  checks.check_return(r)
