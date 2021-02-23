from surrortg import Game
from games.ninswitch.ns_gamepad_serial import NSGamepadSerial, NSButton, NSDPad
from games.ninswitch.ns_dpad_switch_four import NSDPadSwitch
from games.ninswitch.ns_joystick_four import NSJoystick
from games.ninswitch.ns_switch_four import NSSwitch
import asyncio
import logging

import sys
import serial
import pigpio

pigpio.exceptions = False
pi = pigpio.pi()
nsg_1_reset = 19
nsg_2_reset = 16
nsg_3_reset = 26
nsg_4_reset = 20
ON = 0
OFF = 1


async def reset_trinket():
    pi.write(nsg_1_reset, ON)
    pi.write(nsg_2_reset, ON)
    pi.write(nsg_3_reset, ON)
    pi.write(nsg_4_reset, ON)
    logging.info(f"\t TRINKET_RESET down")
    await asyncio.sleep(0.5)
    pi.write(nsg_1_reset, OFF)
    pi.write(nsg_2_reset, OFF)
    pi.write(nsg_3_reset, OFF)
    pi.write(nsg_4_reset, OFF)
    logging.info(f"\t... TRINKET_RESET up")
    await asyncio.sleep(2)


class NinSwitchFourPlayers(Game):
    async def on_init(self):
        # init controls
        self.nsg_1 = NSGamepadSerial()
        self.nsg_2 = NSGamepadSerial()
        self.nsg_3 = NSGamepadSerial()
        self.nsg_4 = NSGamepadSerial()

        try:
            # RX -> TXD | GPIO00 | TX -> RXD | GPIO01
            SERIAL_1 = serial.Serial('/dev/ttyAMA1', 2000000, timeout=0)
            # RX -> TXD | GPIO04 | TX -> RXD | GPIO05
            SERIAL_2 = serial.Serial('/dev/ttyAMA2', 2000000, timeout=0)
            # RX -> TXD | GPIO08 | TX -> RXD | GPIO09
            SERIAL_3 = serial.Serial('/dev/ttyAMA3', 2000000, timeout=0)
            # RX -> TXD | GPIO12 | TX -> RXD | GPIO13
            SERIAL_4 = serial.Serial('/dev/ttyAMA4', 2000000, timeout=0)
            logging.info(f"Found ttyAMA1/ttyAMA2/ttyAMA3/ttyAMA4")
        except:
            logging.critical(f"NSGadget serial port not found")
            sys.exit(1)

        self.nsg_1.begin(SERIAL_1)
        self.nsg_2.begin(SERIAL_2)
        self.nsg_3.begin(SERIAL_3)
        self.nsg_4.begin(SERIAL_4)

        self.io.register_inputs(
            {
                "left_joystick": NSJoystick("Left",
                    self.nsg_1.leftXAxis, self.nsg_1.leftYAxis,
                    self.nsg_2.leftXAxis, self.nsg_2.leftYAxis,
                    self.nsg_3.leftXAxis, self.nsg_3.leftYAxis,
                    self.nsg_4.leftXAxis, self.nsg_4.leftYAxis),
                "right_joystick": NSJoystick("Right",
                    self.nsg_1.rightXAxis, self.nsg_1.rightYAxis,
                    self.nsg_2.rightXAxis, self.nsg_2.rightYAxis,
                    self.nsg_3.rightXAxis, self.nsg_3.rightYAxis,
                    self.nsg_4.rightXAxis, self.nsg_4.rightYAxis),
                "dpad_up": NSDPadSwitch(
                    self.nsg_1, self.nsg_2,
                    self.nsg_3, self.nsg_4,
                    NSDPad.UP, "UP"),
                "dpad_left": NSDPadSwitch(
                    self.nsg_1, self.nsg_2,
                    self.nsg_3, self.nsg_4,
                    NSDPad.LEFT, "LEFT"),
                "dpad_right": NSDPadSwitch(
                    self.nsg_1, self.nsg_2,
                    self.nsg_3, self.nsg_4,
                    NSDPad.RIGHT, "RIGHT"),
                "dpad_down": NSDPadSwitch(
                    self.nsg_1, self.nsg_2,
                    self.nsg_3, self.nsg_4,
                    NSDPad.DOWN, "DOWN"),
                "Y": NSSwitch(
                    self.nsg_1, self.nsg_2,
                    self.nsg_3, self.nsg_4,
                    NSButton.Y, "Y"),
                "X": NSSwitch(
                    self.nsg_1, self.nsg_2,
                    self.nsg_3, self.nsg_4,
                    NSButton.X, "X"),
                "A": NSSwitch(
                    self.nsg_1, self.nsg_2,
                    self.nsg_3, self.nsg_4,
                    NSButton.A, "A"),
                "B": NSSwitch(
                    self.nsg_1, self.nsg_2,
                    self.nsg_3, self.nsg_4,
                    NSButton.B, "B"),
                "minus": NSSwitch(
                    self.nsg_1, self.nsg_2,
                    self.nsg_3, self.nsg_4,
                    NSButton.MINUS, "MINUS"),
                "plus": NSSwitch(
                    self.nsg_1, self.nsg_2,
                    self.nsg_3, self.nsg_4,
                    NSButton.PLUS, "PLUS"),
                "left_throttle": NSSwitch(
                    self.nsg_1, self.nsg_2,
                    self.nsg_3, self.nsg_4,
                    NSButton.LEFT_THROTTLE, "LEFT_THROTTLE"),
                "left_trigger": NSSwitch(
                    self.nsg_1, self.nsg_2,
                    self.nsg_3, self.nsg_4,
                    NSButton.LEFT_TRIGGER, "LEFT_TRIGGER"),
                "right_throttle": NSSwitch(
                    self.nsg_1, self.nsg_2,
                    self.nsg_3, self.nsg_4,
                    NSButton.RIGHT_THROTTLE, "RIGHT_THROTTLE"),
                "right_trigger": NSSwitch(
                    self.nsg_1, self.nsg_2,
                    self.nsg_3, self.nsg_4,
                    NSButton.RIGHT_TRIGGER, "RIGHT_TRIGGER"),
                "left_stick": NSSwitch(
                    self.nsg_1, self.nsg_2,
                    self.nsg_3, self.nsg_4,
                    NSButton.LEFT_STICK, "LEFT_STICK"),
                "right_stick": NSSwitch(
                    self.nsg_1, self.nsg_2,
                    self.nsg_3, self.nsg_4,
                    NSButton.RIGHT_STICK, "RIGHT_STICK"),
            },
        )
        self.io.register_inputs(
            {
                "home": NSSwitch(
                    self.nsg_1, self.nsg_2,
                    self.nsg_3, self.nsg_4,
                    NSButton.HOME, "HOME"),
                "capture": NSSwitch(
                    self.nsg_1, self.nsg_2,
                    self.nsg_3, self.nsg_4,
                    NSButton.CAPTURE, "CAPTURE"),
            },
            admin=True,
        )

    async def on_finish(self):
        logging.info(f"Finish")
        self.io.disable_inputs()

        for seat in self.io._message_router.get_all_seats():
            self.io.send_score(
                score=1, seat=seat, seat_final_score=True,
            )
        self.io.send_score(score=1, final_score=True)

        self.nsg_1.releaseAll()
        self.nsg_2.releaseAll()
        self.nsg_3.releaseAll()
        self.nsg_4.releaseAll()

    async def on_prepare(self):
        await reset_trinket()
        await asyncio.sleep(2)

        self.nsg_1.releaseAll()
        self.nsg_2.releaseAll()
        self.nsg_3.releaseAll()
        self.nsg_4.releaseAll()

    async def on_exit(self, reason, exception):
        self.nsg_1.end()
        self.nsg_2.end()
        self.nsg_3.end()
        self.nsg_4.end()


if __name__ == "__main__":
    NinSwitchFourPlayers().run()
