import sys
import requests
import my_module

print("Python version:", sys.version)
print("Platform:", sys.platform)

response = requests.get("https://en.wikipedia.org/wiki/April_Fools%27_Day")
print("Status Code:", response.status_code)

my_module.greetings()

