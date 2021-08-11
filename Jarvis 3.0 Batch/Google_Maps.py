from geopy.distance import great_circle
from geopy.geocoders import Nominatim
import geocoder
import webbrowser as web
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate', 180-200)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def GoogleMaps(Place):

    Url_place = "https://www.google.com/maps/place/" + str(Place)

    geolocator = Nominatim(user_agent="myGeocoder")

    location = geolocator.geocode(Place, addressdetails=True)

    target_latlon = location.latitude, location.longitude

    web.open(url=Url_place)

    location = location.raw['address']

    target = {'city': location.get('city', ''),
              'state': location.get('state', ''),
              'country': location.get('country', '')}

    current_loca = geocoder.ip('me')

    current_latlon = current_loca.latlng

    distance = str(great_circle(current_latlon, target_latlon))
    distance = str(distance.split(' ', 1)[0])
    distance = round(float(distance), 2)

    print(target)
    speak(f"Dhruv, {Place} is {distance} Kilometres away from your current location.")
