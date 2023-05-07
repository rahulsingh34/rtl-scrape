import requests
import pandas as pd

url_a = "https://ratethelandlord.org/api/get-reviews?page="
url_b = "&sort=new&state=ONTARIO&country&city&zip&search&limit="

df = pd.DataFrame(columns = ["Landlord", "City", "Review"])

for i in range(1, 100):
    try:
        response = requests.request("GET", url_a + str(i) + url_b)
        response = response.json()
        for i in range(len(response["reviews"])):
            df.loc[len(df.index)] = [response["reviews"][i]["landlord"], response["reviews"][i]["city"], response["reviews"][i]["review"]] 
    except:
        print("error")

df.to_csv("./leads.csv")