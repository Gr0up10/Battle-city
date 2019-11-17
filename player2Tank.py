import tank


class Player2Tank(tank.Tank):
    def keyEventDown(self, key):
        if key == 275:
            self._go_right()
        elif key == 276:
            self._go_left()
        elif key == 273:
            self._go_up()
        elif key == 274:
            self._go_down()

    def keyEventUp(self, key):
        if key == 275:
            self._stop_moving_right()
        if key == 276:
            self._stop_moving_left()
        if key == 273:
            self._stop_moving_up()
        if key == 274:
            self._stop_moving_down()
