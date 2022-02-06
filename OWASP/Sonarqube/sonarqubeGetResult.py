import json
import requests
import pprint
import csv

number_needed = []
categories = ['hash', 'crypto', 'weakrand']
with open("/home/x/Benchmark/expectedresults-1.2.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row[' category'] in categories:
            number_needed.append(row['# test name'])

s = requests.Session()
s.auth = ('admin', 'admin')
resp = s.get("http://localhost:9000/api/hotspots/search", params={'projectKey': 'OWASP', "p": 1, "ps": 500})
result = resp.json()
for i in range(2, result["paging"]["total"] // 500 + 2):
    resp = s.get("http://localhost:9000/api/hotspots/search", params={'projectKey': 'OWASP', "p": i, "ps": 500})
    result['hotspots'].extend(resp.json()['hotspots'])
# query to get all the issues
# result = resp.json()
# total = result['total']
# print(total)
# result['issues'] = []
# for i in number_needed:
#     print(i)
#     try:
#         resp = s.get("http://localhost:9000/api/issues/search", params={'componentKeys': 'OWASP', 'files': f'src/main/java/org/owasp/benchmark/testcode/{i}.java', 'ps': '500'})
#         if result == None:
#             result = resp.json()
#         else:
#             result['issues'].extend(resp.json()['issues'])
#             result['components'].append(resp.json()['components'][1])
#     except:
#         pprint.pprint(resp.json())
#         exit(0)

# try:
#     resp = s.get("http://localhost:9000/api/issues/search", params={'componentKeys': 'OWASP', "cwe": "327", "ps": 500})
#     if result == None:
#         result = resp.json()
#     else:
#         result['issues'].append(resp.json()['issues'])
# except:
#     pprint.pprint(resp.json())

with open("/home/x/Benchmark/results/sonarqube_owasp_result.json", "w") as f:
    json.dump(result, f, indent=4)

