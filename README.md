Maven repo importer for repsy

This small script helps importing an external repository into repsy. Please fill the variables section in the script first.

```python
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
```

then you can start the migration:

```bash
python3 ./main.py
```