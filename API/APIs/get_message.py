import requests

roomId = 'Y2lzY29zcGFyazovL3VzL0FQUExJQ0FUSU9OLzk4MDdjY2I5LTFlZDItNGZlNy1iMTg4LTA5MDFiZDk0ODM3Ng'
token = 'M2FiNGM1NzItMGZhZi00OGUxLWFjMjItNzMxMDIyNzE3ZDU2NTE0YmE3YzEtNGRm_PF84_consumer'

url = "https://api.ciscospark.com/v1/messages?roomId=" + roomId

header = {"content-type": "application/json; charset=utf-8",
		  "authorization": "Bearer " + token}

response = requests.get(url, headers = header, verify = True)

print(response.json())
