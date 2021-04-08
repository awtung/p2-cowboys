#class triangle:
#    def __init__(self, length, height ):
#        self.length = length
#        self.height = height
#def get_area(self):
#    return self.length * self.height

class Power3:
    """Initializer of class takes series parameter and returns Class Objectg"""
    def __init__(self, series):
        """Built in validation and exception"""
        if series < 3 or series > 100:
            raise ValueError("Series must be between 2 and 100")
        self._series = series
        self._list = []
        self._dict = {}
        self._dictID = 0
        # Duration timeElapsed;
        # Instant start = Instant.now();  // time capture -- start
        self.calc_series()
        # Instant end = Instant.now();    // time capture -- end
        # this.timeElapsed = Duration.between(start, end);

    """Algorithm for building Power2 sequence, this id called from __init__"""
    def calc_series(self):
        #multiplier = 1
        limit = self._series
        f = [3]  # Power2 starting array/list
        while limit > 0:
            self.set_data(f[0])
            f = [f[0] ** 3 ]
            limit -= 1
            #multiplier += 1

    """Method/Function to set Power2 data: list, dict, and dictID are instance variables of Class"""
    def set_data(self, num):
        self._list.append(num)
        self._dict[self._dictID] = self._list.copy()
        self._dictID += 1

    """Getters with decorator to allow . notation access"""
    @property
    def series(self):
        return self._series

    @property
    def list(self):
        return self._list

    @property
    def number(self):
        return self._list[self._dictID - 1]

    """Traditional Getter requires method access"""
    def get_sequence(self, nth):
        return self._dict[nth]


# Tester Code
if __name__ == "__main__":
    '''Value for testing'''
    n = 5
    '''Constructor of Class object'''
    power3 = Power3(n)

    '''Using getters to obtain data from object'''
    print(f"Power number for {n} = {Power3.number}")
    print(f"Power series for {n} = {Power3.list}")

    '''Using method to get data from object'''
    for i in range(n):
        print(f"Power sequence {i + 1} = {power3.get_sequence(i)}")

