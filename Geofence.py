import requests
import geopy
from geopy.distance import geodesic
import folium

# Ola Maps API credentials
api_key = "tiWQNrtr3tGyzh9uoxuJAKnUFBcrJgdbWR3Yd4kc"
api_secret = "BLPJlG22BcZg8OphZVTArxUO1cyAcsGTT"

# Geofence coordinates and radius
geofence_center = (18.621577, 73.800344)
geofence_radius = 200  # meters

# Function to get user location
def get_user_location():
    # Replace with actual user location retrieval logic
    return (18.623456, 73.801234)

# Function to check if user is within geofence
def check_geofence(user_location):
    distance = geodesic(geofence_center, user_location).meters
    if distance <= geofence_radius:
        print("User is within geofence")
    else:
        print("User is outside geofence")

# Function to draw geofence on map (optional)
def draw_geofence():
    map = folium.Map(location=geofence_center, zoom_start=15)
    folium.Circle(geofence_center, radius=geofence_radius, color='red').add_to(map)
    map.save('geofence_map.html')

# Main function
def main():
    user_location = get_user_location()
    check_geofence(user_location)
    # draw_geofence()  # Uncomment to visualize geofence on map

if __name__ == "__main__":
    main()