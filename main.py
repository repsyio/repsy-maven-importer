#!/usr/bin/env python3

# external maven repo ##########################################################

# Fix the URL
maven_repo_link = 'https://MYUSERNAME.bintray.com/repo/'
maven_repo_username = ''
maven_repo_password = ''

# repsy repo ###################################################################

# Fix the URL
repsy_repo_link = 'https://repo.repsy.io/mvn/MYUSERNAME/MYREPO/'
repsy_repo_username = 'fixme'
repsy_repo_password = 'fixme'

################################################################################

import requests
import re
import base64

anchor_regex = re.compile('<a.*<\/a>')
anchor_link_regex = re.compile('.*href="(.*)"')
repsy_headers = {
    'Authorization': 'Basic ' + base64.b64encode((repsy_repo_username + ':' + repsy_repo_password).encode('ascii')).decode('ascii')
}

def upload_repsy(path: str):
    response = requests.get(maven_repo_link + path)
    upload_response = requests.put(repsy_repo_link + path, data = response.content, headers = repsy_headers)


def walk(path: str):
    response = requests.get(maven_repo_link + path)

    for match in anchor_regex.finditer(response.text):
        link_matches = anchor_link_regex.match(match.group())

        if len(link_matches.groups()) > 0:
            child_path = link_matches.group(1)

            if child_path.endswith('/'):
                walk(path + child_path)
            else:
                print('uploading ' + path + child_path)
                upload_repsy(path + child_path)


walk('')
