import requests


def main():
    #Find the endpoint on the CSO website and request it
    url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"
    response = requests.get(url)

    #Write it to a JSON
    with open("cso.json", "wb") as f:
        f.write(response.content)

if __name__ == '__main__':
    main()