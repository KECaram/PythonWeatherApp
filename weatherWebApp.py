#!/usr/bin/python
# Keith Caram
# INFO.305.061: Survey of Python, Perl, and PHP
# Assignment #4 - Complex Python Program
#								Program Summary
# This is a python web app that returns weather conditions using the openweathermap API. The program
# uses the Flask web framework to create a development server that hosts the program on the address
# localhost:5000. After starting up the program from the command line and entering localhost:5000
# in the url bar of a web browser, the home page of the weather app is displayed. The page promts
# the user to enter a term to gather weather information from - Zip, Name, or 'Local. If a valid 
# term is entered into the form, then a results page is generated with information from the 
# openweathermap API as related to the searched term is displayed clearly. If an empty search term,
# or a term that returns invalid results (i.e. a 404 web response), the home page is redisplayed 
# with a simple error message. My API key is stored in a seperate config.init file - you may need
# to create your own init file containing your own API key. I have included a virtual environment
# through virtualenv that can be run with the script 'source env/bin/activate'.

from flask import Flask, render_template, request
import requests
import configparser

app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET'])
def weather_dashboard():
	return render_template('home.html')

@app.route('/results', methods=['POST'])
def render_results():
	location = request.form['location']

	if(len(location) == 0):
		return render_template('home.html', Invalid="Empty search! Please enter valid City, Zip, \
								or 'Local'.")
	else:
		api_key = get_api_key()
		data = get_weather_results(location, api_key)

		if(int(data['cod']) >= 400):
			return render_template('home.html', Invalid="Invalid Search: " + location + \
									"! Please enter valid City, Zip, or 'Local'.")
		else:
			temp = "{0:.2f}".format(data["main"]["temp"])
			feels_like = "{0:.2f}".format(data["main"]["feels_like"])
			weather = data["weather"][0]["main"]
			location = data["name"]

			return render_template('results.html', 
    						location=location, 
    						temp=temp, 
    						feels_like=feels_like, 
    						weather=weather)

def get_api_key():
	config = configparser.ConfigParser()
	config.read('config.ini')
	return config['openweathermap']['api']

def get_weather_results(location, api_key):
	if(location.upper() == 'LOCAL'):	
		res = requests.get('https://ipinfo.io/')
		loc_dat = res.json()
		location = loc_dat['loc'].split(',')
		lat = location[0]
		lon = location[1]
		url = 'http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}&units=imperial'\
				.format(lat, lon, api_key)
	elif(location.isdecimal() == True):
		url = "https://api.openweathermap.org/data/2.5/weather?zip={}&units=imperial&appid={}"\
				.format(location, api_key)
	else:
		url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=imperial'\
				.format(location, api_key)
	
	res = requests.get(url)
	data = res.json()
	return data

if __name__ == '__main__':
	app.run()
