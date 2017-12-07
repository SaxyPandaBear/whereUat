# Python class wrapper for the SQLite database rows
# IP: The IP that was logged									|	ip		= text
# Host: The host of the source IP								|	host	= text
# City: The name of the city of origin							|	city	= text
# Country : The 2 digit ISO code for the country of origin		|	country	= text
# Latitude: The latitude for the location of the IP				|	lat		= real
# Longitude: The longitude for the location of the IP			|	lng		= real
# Frequency: The number of times this particular IP has 		|	freq	= integer
class IpInfo():
    def __init__(self, **kwargs):
        self.ip = kwargs.get('ip')
        self.hostname = kwargs.get('host')
        self.city = kwargs.get('city')
        self.country = kwargs.get('country')
        self.latitude = kwargs.get('latitude')
        self.longitude = kwargs.get('longitude')
        self.freq = kwargs.get('freq')

    def __str__(self):
        return '{%s, %s, %s, %s, %s, %s, %s}' % (self.ip, 
                                                 self.hostname, 
                                                 self.city, self.country, 
                                                 self.latitude, 
                                                 self.longitude, 
                                                 self.freq)

    def __repr__(self):
        return self.__str__()

    def serialize(self):
        return {
            'ip': self.ip,
            'hostname': self.hostname,
            'city': self.city,
            'country': self.country,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'freq': self.freq
        }

# Object wrapper for just the geolocation data.
class Geolocation():
    def __init__(self, **kwargs):
        self.latitude = kwargs.get('latitude')
        self.longitude = kwargs.get('longitude')
    
    def __str__(self):
        return '( %s,%s )' % (self.latitude, self.longitude)

    def __repr__(self):
        return self.__str__()

    def serialize(self):
        return {
            'latitude': self.latitude,
            'longitude': self.longitude
        }
