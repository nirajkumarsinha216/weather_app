from flask import Flask, render_template,request
import requests
import json

# Get your API key from https://openweathermap.org/api
api_key = "588c7a625b997778ddacc41b3abed663"

app = Flask(__name__)

@app.route("/")
def index():
    city = request.args.get("city")
    if not city:
        city = "San Francisco, CA"

    # Get the current weather for the city
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city, api_key)
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        data = json.loads(response.content)

        # Get the weather details
        status = data["weather"][0]["main"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]

        return str(humidity)
    else:
        return "Error getting weather data"

if __name__ == "__main__":
    app.run(debug=True)
