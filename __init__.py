from mycroft import MycroftSkill, intent_file_handler


class HuitasCalculater(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('calculater.huitas.intent')
    def handle_calculater_huitas(self, message):
        arrival = message.data.get('arrival')
        departure = message.data.get('departure')
        cost = ''

        self.speak_dialog('calculater.huitas', data={
            'arrival': arrival,
            'departure': departure,
            'cost': cost
        })


def create_skill():
    return HuitasCalculater()

