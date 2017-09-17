Python 3.5.4 (v3.5.4:3f56838, Aug  8 2017, 02:17:05) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> with urllib.request.urlopen("localhost:8080/state") as f:
	print(f.read().decode('utf-8'))

	
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    with urllib.request.urlopen("localhost:8080/state") as f:
NameError: name 'urllib' is not defined
>>> import urllib.request
>>> with urllib.request.urlopen("localhost:8080/state") as f:
	print(f.read().decode('utf-8'))

	
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    with urllib.request.urlopen("localhost:8080/state") as f:
  File "C:\Users\User\AppData\Local\Programs\Python\Python35\lib\urllib\request.py", line 163, in urlopen
    return opener.open(url, data, timeout)
  File "C:\Users\User\AppData\Local\Programs\Python\Python35\lib\urllib\request.py", line 466, in open
    response = self._open(req, data)
  File "C:\Users\User\AppData\Local\Programs\Python\Python35\lib\urllib\request.py", line 489, in _open
    'unknown_open', req)
  File "C:\Users\User\AppData\Local\Programs\Python\Python35\lib\urllib\request.py", line 444, in _call_chain
    result = func(*args)
  File "C:\Users\User\AppData\Local\Programs\Python\Python35\lib\urllib\request.py", line 1324, in unknown_open
    raise URLError('unknown url type: %s' % type)
urllib.error.URLError: <urlopen error unknown url type: localhost>
>>> import urllib.request
>>> with urllib.request.urlopen("http://localhost:8080/state") as f:
	print(f.read().decode('utf-8'))

	
free
>>> 
