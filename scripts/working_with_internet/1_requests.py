import requests

# Specify the URL
url = "https://en.wikipedia.org/wiki/Monaco"

# Make the GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Print a snippet of the page content
    print(response.text[:500])  # Display the first 500 characters of the page content
else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")


print("_____________________-")
print(response.headers)