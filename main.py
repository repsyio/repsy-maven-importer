#!/usr/bin/env python3

# external maven repo ##########################################################

# Fix the URL (Do NOT forget trailing slash)
maven_repo_link = 'https://MYUSERNAME.bintray.com/repo/'
maven_repo_username = '' # keep empty string if repo is public
maven_repo_password = ''

# repsy repo ###################################################################

# Fix the URL (Do NOT forget trailing slash)
repsy_repo_link = 'https://repo.repsy.io/mvn/MYUSERNAME/MYREPO/'
repsy_repo_username = 'fixme'
repsy_repo_password = 'fixme'

################################################################################

import requests
import re
import base64

anchor_regex = re.compile('<a.*<\/a>')
anchor_link_regex = re.compile('.*href="(.*)"')
maven_headers = {}

def basic_auth(username: str, password: str):
    return base64.b64encode((username + ':' + password).encode('ascii')).decode('ascii')

if maven_repo_username != '':
    maven_headers = {'Authorization': 'Basic ' + basic_auth(maven_repo_username, maven_repo_password)}

repsy_headers = {'Authorization': 'Basic ' + basic_auth(repsy_repo_username, repsy_repo_password)}

def upload_repsy(path: str):
    response = requests.get(maven_repo_link + path, headers = maven_headers)
    requests.put(repsy_repo_link + path, data = response.content, headers = repsy_headers)


def walk(path: str):
    response = requests.get(maven_repo_link + path, headers = maven_headers)

    for match in anchor_regex.finditer(response.text):
        link_matches = anchor_link_regex.match(match.group())

        if len(link_matches.groups()) > 0:
            child_path = re.sub("\?.*", "a", link_matches.group(1))

            if child_path.endswith('/'):
                walk(path + child_path)
            else:
                print('uploading ' + path + child_path)
                upload_repsy(path + child_path)


walk('')
