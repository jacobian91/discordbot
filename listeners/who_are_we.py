import re

from datetime import datetime
from listeners import Listener

YELL = 2
EMPHASIZE = 5

class WhoAreWe(Listener):
    regex = re.compile("^\*?\*?who are we\?\*?\*?$", re.IGNORECASE)
    timer = datetime.now()

    def condition(self, message):
        return self.regex.match(message.content)

    async def action(self, message):
        now = datetime.now()
        delta = (now - self.timer).total_seconds()

        if delta < YELL:
            await message.channel.send('IRON RIDERS!!!')
        elif delta < EMPHASIZE:
            await message.channel.send('Iron Riders!!')
        else:
            await message.channel.send('Iron Riders!')

        self.timer = now