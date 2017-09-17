import urllib.request
import time

url = "http://localhost:8080/"

def executeRequest(url):
    with urllib.request.urlopen(url) as response:
        return response.read().decode('utf-8')

def executeTests():

    if executeRequest(url + "start") == "started":
        print("Tester started")
    else:
        print("Tester not started")
        return False

    while executeRequest(url + "state") != "finish":
        time.sleep(2)

    if executeRequest(url + "success") == "true":
        print("0 errors")
        return True
    else:
        print(executeRequest(url + "report"))
        return False

if not executeTests():
    raise Exception('Error during testing. See log for details.')