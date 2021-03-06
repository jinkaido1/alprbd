"""
Declaration of the Segment class
"""


class Segment:
    """
    Single segment of plate number
    """

    def __init__(self, serial, image, plate):
        self._serial = serial   # segment id
        self._image = image     # segment image
        self._plate = plate     # plate
        self.guess = []         # list of (prediction, probability), in descending order

    @property
    def serial(self):
        """id of the segment"""
        return self._serial

    @property
    def image(self):
        """segment image"""
        return self._image

    @property
    def plate(self):
        """get the plate which this segment belongs to"""
        return self._plate

    @property
    def value(self):
        """returns the top predicted value"""
        if len(self.guess) == 0:
            return None
        return self.guess[0][0]

# end class
