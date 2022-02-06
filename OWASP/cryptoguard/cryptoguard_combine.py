import json
import os
import pprint

json_list = os.listdir("./cryptoguard");
parent = "./cryptoguard/"
result = []
for json_file in json_list:
   with open(parent + json_file, 'r') as f:
      js = json.load(f)
      result.append(js)

with open("cryptoguard_combine.json", "w") as result_file:
    json.dump(result, result_file)
