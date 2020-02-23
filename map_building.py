'''
Palvo Semchyshyn
22.02.2020
'''

import time
import folium
from geopy.geocoders import Nominatim
from twitter_users import getting_followers, user_input


def get_locations(user: str) -> dict:
    """
    Returns a dictionary with name of user as
    a key and a tuple of coordiantes in latitude
    and longtitude as value
    """
    friends_coordiantes = {}
    friends_locations = getting_followers(user)
    geolocator = Nominatim(user_agent="specify_your_app_name_here")
    for friend in friends_locations:
        location = friends_locations.get(friend)
        try:
            coordinates = geolocator.geocode(location)
            if coordinates is None:
                continue
            elif abs(coordinates.longitude) > 180 or abs(coordinates.latitude) > 90:
                continue
        except Exception:
            continue
        friends_coordiantes[friend] = coordinates.latitude, coordinates.longitude
        print(friend, friends_coordiantes[friend])
    return friends_coordiantes


def map_builder(user: str) -> None:
    """
    A function for generating an html file,
    which represents a map with markers of
    user followers in twitter
    """
    friends_coordiantes = get_locations(user)
    mapp = folium.Map()
    friend_layer = folium.FeatureGroup()
    for friend in friends_coordiantes:
        loc = friends_coordiantes.get(friend)
        url_icon = "static/images/iconfinder_twitter_circle_294709.png"
        icon = folium.features.CustomIcon(url_icon, icon_size=(22, 24))
        marker = folium.Marker(location=loc, icon=icon, popup=friend)
        friend_layer.add_child(marker)
    mapp.add_child(friend_layer)
    mapp.save("static/images/map.html")


def run_map_building(user) -> None:
    """
    A function for running the module
    """
    print("Processing friends....")
    time.sleep(1)
    map_builder(user)
    print("FINISHED....\n" + "_"*30 + "\n")
    time.sleep(1)
    print("Please, have a look at file <map.html>")


if __name__ == "__main__":
    USER = user_input()
    run_map_building(USER)
