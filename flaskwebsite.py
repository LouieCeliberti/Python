import requests
import json
r = requests.get('https://www.instagram.com/explore/tags/louiedasboot/')


j = '{"action":"louie","Method":"ondata","img":"https://instagram.fewr1-4.fna.fbcdn.net/vp/1da8505ddcb07e1125e45e99b172897a/5B318150/t51.2885-15/s640x640/sh0.08/e35/29087460_187159325397878_8115219016483602432_n.jpg"}'
class Payload(object):
    def __init__(self, j):
        self.__dict__ = json.loads(j)

p = Payload(j)




from flask import Flask,redirect
app = Flask(__name__)

url_image = p.img
@app.route("/")
def hello():
    return '<html><HEAD><TITLE>'+p.action + '</TITLE></HEAD><img src='+url_image+'></html>'

if __name__ == "__main__":
    app.run(debug=True)