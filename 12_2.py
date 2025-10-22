'''
Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api.
Kirjoita ohjelma, joka kysyy käyttäjältä paikkakunnan nimen ja tulostaa sitä vastaavan säätilan tekstin
sekä lämpötilan Celsius-asteina. Perehdy rajapinnan dokumentaatioon riittävästi.
palveluun rekisteröityminen on tarpeen, jotta saat rajapintapyynnöissä tarvittavan API-avaimen (API key).
Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi.
'''

import json
import requests

kaupunki = input("Anna kaupungin nimi: ")
api="844d488cedce88c6a8f8d4e32e4f3416"
pyyntö1=f"http://api.openweathermap.org/geo/1.0/direct?q={kaupunki}&limit=5&appid={api}"


vastaus=requests.get(pyyntö1).json()
#print(json.dumps(vastaus, indent=2))
koord=vastaus[0]["lat"], vastaus[0]["lon"]
pyyntö=f"https://api.openweathermap.org/data/2.5/weather?lat={koord[0]}&lon={koord[1]}&units=metric&appid={api}"

vastaus2=requests.get(pyyntö).json()
print(json.dumps(vastaus2, indent=2))
lämpötila=f"{vastaus2['main']['temp']}"
säätila = f"{vastaus2['weather'][0]['main']}"
print(f"säätilana on: {säätila}")
print(f"lämpötila on: {lämpötila} celsiusta")
