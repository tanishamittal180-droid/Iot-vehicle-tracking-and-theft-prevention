import math

SAFE_LAT = 31.3260
SAFE_LON = 75.5762

SAFE_RADIUS = 0.005

def distance(lat1, lon1,
             lat2, lon2):

    return math.sqrt(
        (lat1-lat2)**2 +
        (lon1-lon2)**2
    )

def check_geofence(
        current_lat,
        current_lon):

    d = distance(
        current_lat,
        current_lon,
        SAFE_LAT,
        SAFE_LON
    )

    if d > SAFE_RADIUS:

        return False

    return True