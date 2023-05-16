import requests
import pandas as pd

print("running")

url_a = "https://ratethelandlord.org/api/get-reviews?page="
url_b = "&sort=new&state=&country&city&zip&search&limit="

df = pd.DataFrame(columns = ["Landlord", "City", "State", "Zip", "Review", "Repair", "Health", "Stability", "Privacy", "Respect"])

for i in range(1, 500):
    try:
        response = requests.request("GET", url_a + str(i) + url_b)
        response = response.json()
        for i in range(len(response["reviews"])):
            df.loc[len(df.index)] = [response["reviews"][i]["landlord"],
                                      response["reviews"][i]["city"],
                                      response["reviews"][i]["state"],
                                      response["reviews"][i]["zip"],
                                      response["reviews"][i]["review"],
                                      response["reviews"][i]["repair"],
                                      response["reviews"][i]["health"],
                                      response["reviews"][i]["stability"],
                                      response["reviews"][i]["privacy"],
                                      response["reviews"][i]["respect"]]
    except:
        print("error")

df.to_csv("./leads.csv")