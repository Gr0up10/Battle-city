import tank


class PlayerTank(tank.Tank):
    def keyEventDown(self, key):
        if chr(key) == 'd':
            self._go_right()
        elif chr(key) == 'a':
            self._go_left()
        elif chr(key) == 'w':
            self._go_up()
        elif chr(key) == 's':
            self._go_down()

    def keyEventUp(self, key):
        if chr(key) == 'd':
            self._stop_moving_right()
        if chr(key) == 'a':
            self._stop_moving_left()
        if chr(key) == 'w':
            self._stop_moving_up()
        if chr(key) == 's':
            self._stop_moving_down()