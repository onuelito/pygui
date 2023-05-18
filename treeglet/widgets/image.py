import pyglet
from pyglet.sprite import Sprite
from pyglet.graphics import OrderedGroup

from treeglet.widget import Widget

class Image(Widget):
    """
    Texture display class
    """
    
    _resize_image = True #Variable to force resize or not

    def __init__(self, texture, x=0, y=0, z=0, group=None, batch=None):

        super().__init__(x=x, y=y, z=z, width=texture.width, height=texture.height)
        self._group = OrderedGroup(z, parent=group)
        self._sprite = Sprite(texture, x, y, group=self._group, batch=batch)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def z(self):
        return self._z

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height
     
    @property
    def visible(self):
        return self._visible

    @x.setter
    def x(self, value):
        self._x = value
        self._sprite.x = value + self.__anchor_x_offset__()

    @y.setter
    def y(self, value):
        self._y = value
        self._sprite.y = value + self.__anchor_y_offset__()

    @z.setter
    def z(self, value):
        self._z = value
        self._group = OrderedGroup(value, parent=self._group.parent)

    @width.setter
    def width(self, value):
        scale_x = value/self._width
        self._sprite.scale_x *= scale_x
        self._width = value

    @height.setter
    def height(self, value):
        scale_y = value/self._height
        self._sprite.scale_y *= scale_y
        self._height = value

    @visible.setter
    def visible(self, value):
        self._group.visible = value

    """
    Group & Batch
    """
    def set_group(self, value):
        visible = self._group.visible
        self._group = OrderedGroup(self.z, parent=value)
        self._group.visible = visible
        self._sprite.group = self._group

    def set_batch(self, value):
        self._batch = value
        self._sprite.batch = value

    """
    Image methods
    """

    @property
    def image(self):
        return self._sprite.image

    @image.setter
    def image(self, value):
        """
        Reseting width and height for scaling purpose
        """
        if self._resize_image:
            width, height               = self._width, self._height
            self._width, self._height   = value.width, value.height
            self._sprite.scale_x        = 1
            self._sprite.scale_y        = 1
            self._sprite.image          = value
            self.width, self.height     = width, height
        else:
            self._sprite.image          = value
            self._width                 = self._sprite.width
            self._height                = self._sprite.height