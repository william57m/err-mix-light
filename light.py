from urllib.request import Request
from urllib.request import urlopen
 
from errbot import botcmd
from errbot import BotPlugin


class LightControl(BotPlugin):

    def get_configuration_template(self):
        return {'API_URL': 'http://localhost:8888'}

    @botcmd
    def light(self, msg, args):
        """ Enable/Disable Mix Light """

        # Documentation
        if not args:
            return self.return_doc()

        # Get state
        if args == 'on' or args == 'off':
            return self.change_state(args)
        elif args == 'status':
            return self.return_status()
        else:
            return self.return_doc()

    def change_state(self, state):
        url = self.config['API_URL'] + '/' + state
        with urlopen(Request(url, {})) as response:
            return response

    def return_status(self):
        url = self.config['API_URL'] + '/status'
        with urlopen(url) as response:
            return response

    def return_doc(self):
        return "This is not a valid command man, please use 'on' or 'off' or 'status'"
