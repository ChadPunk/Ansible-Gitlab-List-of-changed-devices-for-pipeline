import requests
import json
import re
import sys
import os
import yaml

header = {
    "PRIVATE-TOKEN": "!!!PUT YOUR TOKEN HERE!!!"
}

mergeId = sys.argv[1]

url = f"https://YOUR URL HERE/api/v4/projects/YOUR PROJECT ID HERE/merge_requests/{mergeId}/diffs"
# Project ID can be found in GitLab URL while viewing the project.



r = requests.get(url, headers=header, verify=False)
r = r.json()

changeddevices = []


for item in r:
    '''
    This piece takes the API Resp. and loops through the changes detected. 
    If the word "Compiled" is in the change path we take and modify it to the desired output and save that to a file.
    '''
    if "compiled" in item['new_path']:
        changeddevices.append(re.sub("^compiled(/([^;]*)/)", "", item['new_path']))



my_list = ','.join(changeddevices)
print(f"Devices being changed: {my_list}")

#Saves device list as a single line to be stored in the file.
with open("my_list.env", "w") as f:
    f.write(f"DEVICES={my_list}")
    




