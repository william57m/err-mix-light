from urllib.request import Request
from urllib.request import urlopen
 
from errbot import botcmd
from errbot import BotPlugin


class LightControl(BotPlugin):

    api_url = URL = 'http://10.3.18.205:8888/{0}'

    @botcmd
    def light(self, msg, args):
        """ Enable/Disable Mix Light """

        # Get state
        state = None
        if args == 'on':
            state = 'activate'
        elif args == 'off':
            state = 'deactivate'
        else:
            return "This is not a valid state man, please use 'on' or 'off'"

        # Request server
        if state:
            url = api_url.replace(state)
            with urlopen(Request(url, {})) as response:
                return response
