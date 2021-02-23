from surrortg.inputs import Switch
from games.ninswitch.ns_gamepad_serial import NSDPad


class NSDPadSwitch(Switch):
    def __init__(self, nsg1, nsg2, nsg3, nsg4, dpad_dir, key):
        self.nsg1 = nsg1
        self.nsg2 = nsg2
        self.nsg3 = nsg3
        self.nsg4 = nsg4
        self.dpad_dir = dpad_dir
        self.key = key

    async def on(self, seat=0):
        if seat == 0:
            self.nsg1.dPad(self.dpad_dir)
        elif seat == 1:
            self.nsg2.dPad(self.dpad_dir)
        elif seat == 2:
            self.nsg3.dPad(self.dpad_dir)
        elif seat == 3:
            self.nsg4.dPad(self.dpad_dir)

    async def off(self, seat=0):
        if seat == 0:
            self.nsg1.dPad(NSDPad.CENTERED)
        elif seat == 1:
            self.nsg2.dPad(NSDPad.CENTERED)
        elif seat == 2:
            self.nsg3.dPad(NSDPad.CENTERED)
        elif seat == 3:
            self.nsg4.dPad(NSDPad.CENTERED)