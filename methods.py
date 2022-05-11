from hashlib import sha256
import github
import base64
import sys

def getRepos(user):
    try:
        repos = list(user.get_repos())
    except github.GithubException:
        print("Token Invalid")
        sys.exit()
    return repos

def getRecord(files):
    text = ""
    for f in files:
        lines = "".join(base64.b64decode(f).decode("ascii").split("\r"))
        text += lines
    return sha256(text.encode("ascii")).hexdigest()

def checkRepoExists(name,repoNames):
    if name not in repoNames:
        print("Repo Not Found")
        sys.exit()

def getFiles(name,client,names=True):
    r = getRepos(client.get_user())
    nm = [rpo.name for rpo in r]
    checkRepoExists(name,nm)
    if names == False:
        return [ f.content for f in r[nm.index(name)].get_contents("")]
    return { f.name:f.content for f in r[nm.index(name)].get_contents("")}
