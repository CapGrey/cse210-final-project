class Location:
    """A distance from a relative origin (0, 0).

    The responsibility of Location is to hold and provide information about itself. Location has a few 
    convenience methods for adding, scaling, and comparing them.

    Attributes:
        _x (integer): The horizontal distance from the origin.
        _y (integer): The vertical distance from the origin.
    """
    
    def __init__(self, x, y):
        """Constructs a new Location using the specified x and y values.
        
        Args:
            x (int): The specified x value.
            y (int): The specified y value.
        """
        self._x = x
        self._y = y

    def add(self, other):
        """Gets a new point that is the sum of this and the given one.

        Args:
            other (Location): The Location to add.

        Returns:
            Location: A new Location that is the sum.
        """
        x = self._x + other.get_x()
        y = self._y + other.get_y()
        return Location(x, y)

    def equals(self, other):
        """Whether or not this Location is equal to the given one.

        Args:
            other (Location): The Location to compare.

        Returns: 
            boolean: True if both x and y are equal; false if otherwise.
        """
        return self._x == other.get_x() and self._y == other.get_y()

    def get_x(self):
        """Gets the horizontal distance.
        
        Returns:
            integer: The horizontal distance.
        """
        return self._x

    def get_y(self):
        """Gets the vertical distance.
        
        Returns:
            integer: The vertical distance.
        """
        return self._y

    def scale(self, factor):
        """
        Scales the point by the provided factor.

        Args:
            factor (int): The amount to scale.
            
        Returns:
            Location: A new Location that is scaled.
        """
        return Location(self._x * factor, self._y * factor)