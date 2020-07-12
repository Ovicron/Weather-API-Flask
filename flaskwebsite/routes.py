from flask import render_template, request
from flaskwebsite import app, db
from flaskwebsite.models import City
import requests


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        new_city = request.form.get('city')

        if new_city:
            new_city_obj = City(name=new_city)
            db.session.add(new_city_obj)
            db.session.commit()

    cities = City.query.all()
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}' \
          '&appid=b36abf1270c3c4f229ce68a06d5ddd11&mode=json&units=imperial'

    weather_data = []

    for city in cities:
        r = requests.get(url.format(city.name)).json()

        weather = {
            'city': r['name'],
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon']
        }

        weather_data.append(weather)
    return render_template('home.html', title='Home',  weather_data=weather_data)
