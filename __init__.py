from mycroft import MycroftSkill, intent_file_handler
#from geopy.distance import geodesic
#from geopy.geocoders import Nominatim

class HuitasCalculater(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('calculater.huitas.intent')
    def handle_calculater_huitas(self, message):
        arrival = message.data.get('arrival')
        departure = message.data.get('departure')
        cost = ''
#---------------------------------------------------------
"""	self.log.info("Code start")
	#berechen Coordinaten
	geolocator = Nominatim(user_agent="Huitas calculator")
	locarrival = geolocator.geocode(arrival)
	locdeparture = geolocator.geocode(departure)
	corarrival = (locarrival.latitude, locarraval.longitude)
	cordeparture = (locdeparture.latitude, locdeparture.longitude)
	
	self.log.info(corarrical, cordeparutre)
	#berechne Distanz
	distance = geodesic(corarrival, cordeparure).km
	
	self.log.info("distance: " + distance)
	#brechne kosten
	cost = distance*10"""
#-----------------------------------------------------------
	self.speak_dialog('calculater.huitas', data= \
            'arrival': arrival, \
            'departure': departure, \
            'cost': cost \
	)


def create_skill():
    return HuitasCalculater()

