# API key: c20ddcfad02c4166a1e08c00c1cbd42f
import requests

url = 'https://newsapi.org/v2/everything?q=tesla&from=2023-01-26&sortBy=publishedAt'

header = {
    "Authorization":"c20ddcfad02c4166a1e08c00c1cbd42f"
}

x = requests.get(url, headers = header)

print(x.text)