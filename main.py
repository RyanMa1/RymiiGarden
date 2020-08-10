from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/pi', methods=['POST'])
def pi():

	print("Temperature: "+str(request.json['temp'])+
			 "Moisture: "+str(request.json['moist']), flush=True)
	return '200'

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = False, port = os.environ['PORT'])
