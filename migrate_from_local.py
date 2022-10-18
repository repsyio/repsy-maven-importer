#!/usr/bin/env python3

# local maven repo #############################################################

# Fix the URL
local_repo_path = '/path/to/repo'

# repsy repo ###################################################################

# Fix the URL (Do NOT forget trailing slash)
repsy_repo_link = 'https://repo.repsy.io/mvn/MYUSERNAME/MYREPO/'
repsy_repo_username = 'fixme'
repsy_repo_password = 'fixme'

################################################################################

import requests
import base64
from os import walk

maven_headers = {}

def basic_auth(username: str, password: str):
    return base64.b64encode((username + ':' + password).encode('ascii')).decode('ascii')

repsy_headers = {'Authorization': 'Basic ' + basic_auth(repsy_repo_username, repsy_repo_password)}

def upload_to_repsy(path: str):
    with open(path, 'rb') as file:
        requests.put(repsy_repo_link + path.replace(local_repo_path, ''), data = file.read(), headers = repsy_headers)


for (dir_path, dir_names, file_names) in walk(local_repo_path):
    for dir_name in dir_names:
        walk(dir_path + '/' + dir_name)
    for file_name in file_names:
        upload_to_repsy(dir_path + '/' + file_name)
