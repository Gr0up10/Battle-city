from block import Block


class Brick(Block):
    def __init__(self, screen):
        super().__init__('sprites/blocks/4.png', screen)
        self.is_wall = True
