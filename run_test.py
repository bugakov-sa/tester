import urllib.request
with urllib.request.urlopen("http://localhost:8080/state") as f:
    print(f.read().decode('utf-8'))
