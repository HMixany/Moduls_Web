from http import client


h1 = client.HTTPConnection('localhost', 5353)
h1.request("GET", "/")

res = h1.getresponse()
print(res.status, res.reason)
print(res)

data = res.read()
print(data)