#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

import urllib
import json
import os
from flask import Flask, render_template
import sys
import logging

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):
    if req.get("result").get("action") != "get_task":
        return {}
    result = req.get("result")
    parameters = result.get("parameters")
    floor = parameters.get("floor")
    office = parameters.get("office")
    if floor < 2**100:
        floor = "на " + floor + " этаже"
    elif floor == "нижнем":
        floor = "на " + floor + " этаже"
    elif floor == "верхнем":
        floor = "на " + floor + " этаже"
    else:
        floor = "на " + floor + " этажах"
        
    speech = "Hello!"

    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

app.run(debug=True, port=port, host='0.0.0.0')
