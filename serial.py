class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """Create a serial number generator from start number"""
        self.start_num = start
        self.incrementer = start

    def generate(self):
        """Generate a new serial number"""
        self.incrementer += 1
        return self.incrementer - 1
        # if self.start_num == self.incrementer:
        #     self.incrementer = 0
        #     return self.start_num
        # else:
        #     self.incrementer += 1
        #     return self.incrementer + self.start_num

    def reset(self):
        """Reset serial number"""
        self.incrementer = self.start_num
