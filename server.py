# for py3
import flask
import requests
import json
import random
import logging
import threading

import sys
if sys.version_info.major is 2:
    import Queue as queue
else:
    import queue

app = flask.Flask(__name__)

### DIY Area ###

WALLET_ADDR = "http://127.0.0.1:4003"

PASC_Receiver = "360969" # Maybe one of 

PASA_Receiver = "3GhhbonhKfpLAZYurzU2TAbiCF2gjSgyx896sTKVVLRp8jCZY9ehUuDsZLzT5DVNAdH98Co62v3PEv5yYLR7xsHcCULmy236ir6xwt"

Excluded_PASA = [PASC_Receiver, ] # You can add more pasa which you didn't wanna share

################


LastHeight = 0

# Pending_Pool = []
Pending_Pool = queue.Queue()


def getCurrentHeight():
    op = '{"jsonrpc":"2.0","method":"getblockcount","id":123}'
    rcv = requests.post(WALLET_ADDR, data=op)
    rcv_fmt = json.loads(rcv.text)
    print(rcv_fmt)
    if rcv_fmt.get("error", None) is None:
        height = int(rcv_fmt.get("result"))
        logging.info("Current Height: ", height)
        return height
    else:
        logging.fatal("Error on get height:" + rcv_fmt.get("error"))


def getRandomFreePASA():
    operation = '{"jsonrpc":"2.0","method":"getwalletaccounts","id":123}'
    rcv = requests.post(WALLET_ADDR, data=operation)
    rcv_fmt = json.loads(rcv.text)
    print(rcv_fmt)
    if rcv_fmt.get("error", None) is None:
        pasa_list = []
        for i in rcv_fmt.get("result"):
            if int(i["balance"]) == 0 and i["account"] not in Excluded_PASA:
                pasa_list.append(i["account"])
        print(pasa_list)
        return random.sample(pasa_list, 1)[0]
    else:
        logging.fatal(rcv_fmt.get("message", "No message"))


@app.route('/')
def hello_world():
    # return 'Hello World!'
    return flask.render_template("index.html")


@app.route('/getpasa/<pub_key>')
def getpasa(pub_key):
    if getCurrentHeight() is LastHeight:
        # means that no free tx
        todo = pub_key
        Pending_Pool.put(todo)
        return "Success, but needs wait"
    pasa = getRandomFreePASA()
    rcv_fmt = sendPASA(pasa, pub_key)
    if rcv_fmt.get("error", None) is None:
        return "Luckily, Finished with message:" + rcv_fmt.get("message", "No message")
    else:
        return "Error"


@app.route('/getpasa')
def getpasa_guider():
    return flask.render_template("guider.html")

def sendPASA(pasa, pub_key):
    operation = '{"jsonrpc":"2.0","method":"changekey","params":{"account":%s,"new_b58_pubkey":"%s","fee":0.0000,"payload":"","payload_method":"none"},"id":123}' % (
        pasa, pub_key, )
    rcv = requests.post(WALLET_ADDR, data=operation)
    return json.loads(rcv.content)


@app.route('/donate')
def donate():
    return ("PASC:Account: ", str(PASC_Receiver) ". <br>PASA:PublicKey: ", PASA_Receiver) 


@app.route('/verify/nano')
def nanoVerify():
    return ""


# a new thread for dealing with the pending pool
class Service(threading.Thread):
    """docstring for Service"""

    def __init__(self, Pending_Pool):
        super(Service, self).__init__()
        self.pool = Pending_Pool

    def run(self):
        while True:
            newTarget = self.pool.get()
            pasa = getRandomFreePASA()
            rcv_fmt = sendPASA(pasa, newTarget)


if __name__ == '__main__':
    pasaService = Service(Pending_Pool)
    pasaService.daemon = True
    pasaService.start()

    LastHeight = getCurrentHeight()
    app.run("0.0.0.0", port=8888)
