from surrortg.inputs import Switch


class NSSwitch(Switch):
    def __init__(self, nsg1, nsg2, nsg3, nsg4, button, key):
        self.nsg1 = nsg1
        self.nsg2 = nsg2
        self.nsg3 = nsg3
        self.nsg4 = nsg4
        self.button = button
        self.key = key

    async def on(self, seat=0):
        if seat == 0:
            self.nsg1.press(self.button)
        elif seat == 1:
            self.nsg2.press(self.button)
        elif seat == 2:
            self.nsg3.press(self.button)
        elif seat == 3:
            self.nsg4.press(self.button)

    async def off(self, seat=0):
        if seat == 0:
            self.nsg1.release(self.button)
        elif seat == 1:
            self.nsg2.release(self.button)
        elif seat == 2:
            self.nsg3.release(self.button)
        elif seat == 3:
            self.nsg4.release(self.button)
