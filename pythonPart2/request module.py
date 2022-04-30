import requests

r = requests.get("https://www.geeksforgeeks.org/inheritance-in-python/?ref=lbp")
print(r.text)
