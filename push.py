from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner
from twisted.internet.defer import inlineCallbacks
from collections import namedtuple

Tick = namedtuple("Tick", ["currency_pair",
                           "last",
                           "lowest_ask",
                           "highest_bid",
                           "percent_change",
                           "base_volume",
                           "quote_volume",
                           "is_frozen",
                           "high_24hr",
                           "low_24hr"])

class MyComponent(ApplicationSession):
    @inlineCallbacks
    def onJoin(self, details):
        print("session ready")

        def ontick(*args):
            tick = Tick(*args)
            print(tick)

        try:
            yield self.subscribe(ontick, u'ticker')
            print("subscribed to ticker")
        except Exception as e:
            print("could not subscribe to ticker: {0}".format(e))

runner = ApplicationRunner(url=u"wss://api.poloniex.com", realm=u"realm1")
runner.run(MyComponent)
