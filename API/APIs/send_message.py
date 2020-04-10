from flask import Flask, request
import requests
import json
import pymongo


############## Bot details ##############

bot_name = 'extra_lessons@webex.bot'
roomId = "Y2lzY29zcGFyazovL3VzL1JPT00vZTQ4MjhlOTAtNzliZS0xMWVhLWE1YjctYWRiMmUxMDFiOWRi"
token = 'M2FiNGM1NzItMGZhZi00OGUxLWFjMjItNzMxMDIyNzE3ZDU2NTE0YmE3YzEtNGRm_PF84_consumer'
header = {"content-type": "application/json; charset=utf-8",
		  "authorization": "Bearer " + token}


############## MONGODB CONNECTIVITY ##############
url = "mongodb://svetlana:123456789@localhost:27017/Private_Lessons"

with pymongo.MongoClient(url) as client:
	db = client.Private_Lessons
	collection = db.Teachers_Information
############## Flask Application ##############

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def sendMessage():
	webhook = request.json
	url = 'https://api.ciscospark.com/v1/messages'
	msg = {"roomId": webhook["data"]["roomId"]}
	sender = webhook["data"]["personEmail"]
	subjects= ["english", "spanish", "maths", "chemistry", "physics"]
	subjects_Cap = ["English", "Spanish", "Maths", "Chemistry", "Physics"]
	output = ''
	message = getMessage()
	if (sender != bot_name):
		if (message.lower() == "hello" or message.lower() == "hi"):
			msg["markdown"] = "Welcome to your personal private class teacher advisor!  \n List of available options: \n" \
							  "- Available subjects: Subjects. \n" \
							  "- Available teachers for one particular subject: the name of the subject, for example: english. \n" \
							  "- Filter by type of classes: individual or collective."

		elif (message == "Subjects"):
			msg["markdown"] = "The offered subjects are: \n" \
							  "- English \n" \
							  "- Spanish \n" \
							  "- Maths. \n" \
							  "- Chemistry \n" \
							  "- Physics."

		elif (message.lower() in subjects):
			message=message.lower()
			cursor = collection.find({'Subject': message})
			for result in cursor:
				output = output + "- " +result['Name'] + ": " + result['Phone_number'] + ", " + result['Type'] + " classes, " + result['Price'] + " per student per hour \n"
			msg["markdown"] = output

		elif (message.lower() == "individual" or message.lower() == "collective"):
			message=message.lower()
			output = "The teachers for " + message + " classes are: \n"
			cursor = collection.find({'Type': message})
			for result in cursor:
				output = output + "- " + result['Name'] + ": " + result['Phone_number'] + ", " + result['Subject'] + ", " + result['Price'] + " per student per hour \n"
			msg["markdown"] = output #sustituir por la variable con el contenido, un json o algo

		elif(message == "help"):
			output= "The possible commands are: \n" \
					"- \"Subjects\" \n" \
					"- the names of the subjects like \"spanish\", \"maths\", \"physics\", etc. \n" \
					"- the type of the classes: \"individual\" or \"collective\" \n " \
					""
			msg["markdown"] = output

		else:
			msg["markdown"] = "Sorry! I didn't recognize that command. Type **help** to see the list of available commands."
		requests.post(url,data=json.dumps(msg), headers=header, verify=True)

def getMessage():
	webhook = request.json
	url = 'https://api.ciscospark.com/v1/messages/' + webhook["data"]["id"]
	get_msgs = requests.get(url, headers=header, verify=True)
	message = get_msgs.json()['text']
	return message

app.run(debug = True)