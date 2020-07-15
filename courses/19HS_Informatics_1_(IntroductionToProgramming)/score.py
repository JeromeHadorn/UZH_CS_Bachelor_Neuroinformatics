import requests
import json
import os

import requests
# Script that fetches and summarises points given in exercises



Bearer = "Bearer " + replaceWithYourBearerToken
url = "https://info1-exercises.ifi.uzh.ch/api/students/courses/034d9e52-e0d1-3a94-a39a-457191a4e129/results"

headers = {
    'Authorization': Bearer,
    'User-Agent': "PostmanRuntime/7.20.1",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "e3ae8e17-1ad4-4f8c-af60-5a747fc663f1,239d0d91-929f-4ff8-8dab-2aed8b242b6c",
    'Host': "info1-exercises.ifi.uzh.ch",
    'Accept-Encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
}

response = requests.request("GET", url, headers=headers)

# print(response.text)


parsed_json = (json.loads(response.text))


maxScore = 0
myScore = 0
print("Max Score  -  My Score")
for item in parsed_json:
    maxScore += item["maxScore"]
    myScore += item["studentScore"]
    print(item["maxScore"], "      ", item["studentScore"])

print("-----------------------------------")
print("Sum: " + str(maxScore) + "  " + str(myScore))


percentage = round((myScore / maxScore) * 100)
print("Status: " + str(percentage) + "%")

FILE = os.path.dirname(__file__) + "/score.md"

with open(FILE, "w") as f:
    f.write("# Current Stats")
    f.write("\n")
    f.write("Max Score: " + str(maxScore) + "  " + "My Score: " + str(myScore))
    f.write("\n")
    f.write("**"+str(percentage)+"%"+"**")
