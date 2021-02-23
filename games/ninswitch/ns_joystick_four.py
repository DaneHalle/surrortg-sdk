from surrortg.inputs import Joystick, Directions

DIRECTION_TO_JOYSTICK_VALS = {
    Directions.TOP: (128, 0),
    Directions.BOTTOM: (128, 255),
    Directions.LEFT: (0, 128),
    Directions.RIGHT: (255, 128),
    Directions.TOP_LEFT: (0, 0),
    Directions.TOP_RIGHT: (255, 0),
    Directions.BOTTOM_LEFT: (0, 255),
    Directions.BOTTOM_RIGHT: (255, 255),
    Directions.MIDDLE: (128, 128),
}


class NSJoystick(Joystick):
    def __init__(self, side,
                    x_axis1, y_axis1,
                    x_axis2, y_axis2,
                    x_axis3, y_axis3,
                    x_axis4, y_axis4):
        super().__init__()
        self.side = side
        self.x_axis1 = x_axis1
        self.y_axis1 = y_axis1
        self.x_axis2 = x_axis2
        self.y_axis2 = y_axis2
        self.x_axis3 = x_axis3
        self.y_axis3 = y_axis3
        self.x_axis4 = x_axis4
        self.y_axis4 = y_axis4

    async def handle_coordinates(self, x, y, seat=0):
        direction = self.get_direction_8(x, y)
        x, y = DIRECTION_TO_JOYSTICK_VALS[direction]
        if seat == 0:
            self.x_axis1(x)
            self.y_axis1(y)
        elif seat == 1:
            self.x_axis2(x)
            self.y_axis2(y)
        elif seat == 2:
            self.x_axis3(x)
            self.y_axis3(y)
        elif seat == 3:
            self.x_axis4(x)
            self.y_axis4(y)

    async def reset(self, seat=0):
        if seat == 0:
            self.x_axis1(128)
            self.y_axis1(128)
        elif seat == 1:
            self.x_axis2(128)
            self.y_axis2(128)
        elif seat == 2:
            self.x_axis3(128)
            self.y_axis3(128)
        elif seat == 3:
            self.x_axis4(128)
            self.y_axis4(128)
