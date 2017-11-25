# for py3
import flask
import requests
import json
import random

app = flask.Flask(__name__)

# SERVER_PUB_KEY = 
exclude_pasa = ["360969"]

def getRandomFreePASA():
	operation = '{"jsonrpc":"2.0","method":"getwalletaccounts","id":123}'
	rcv = requests.post("http://127.0.0.1:4003", data=operation)
	rcv_fmt = json.loads(rcv.text)
	print(rcv_fmt)
	if rcv_fmt.get("error", None) is not None:
		print(rcv_fmt.get("message", "No message"))
	else:
		pasa_list = []
		for i in rcv_fmt.get("result"):
			if int(i["balance"]) == 0:
				pasa_list.append(i["account"])
		print(pasa_list)
		return random.sample(pasa_list, 1)[0]


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/getpasa/<id>/<pub_key>')
def getpasa(id, pub_key):
	pasa = getRandomFreePASA()
	# if pasa = None:

	operation = '{"jsonrpc":"2.0","method":"changekey","params":{"account":%s,"new_b58_pubkey":"%s","fee":0.0000,"payload":"","payload_method":"none"},"id":123}' % (pasa, pub_key, )
	rcv = requests.post("http://127.0.0.1:4003", data=operation)
	rcv_fmt = json.loads(rcv.content)
	if rcv_fmt.get("error", None) is not None:
		print(rcv_fmt.get("message", "No message"))
	else:
		print(rcv_fmt.get("ophash"))
	return "Finished"

if __name__ == '__main__':
    app.run()
    