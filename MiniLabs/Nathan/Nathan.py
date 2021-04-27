"""Square Root algorithm contained within a class """
import math


class Sqrt:
    """Initializer of class takes series parameter and returns Class Object"""

    def __init__(self, series):
        """Built in validation and exception"""
        if series < 4 or series > 1000000:
            raise ValueError("Series must be between 4 and 100")
        self._series = series
        self._list = []
        self._dict = {}
        self._dictID = 0
        # Duration timeElapsed;
        # Instant start = Instant.now();  // time capture -- start
        self.calc_series()
        # Instant end = Instant.now();    // time capture -- end
        # this.timeElapsed = Duration.between(start, end);

    """Algorithm for building Square Root sequence, this id called from __init__"""

    def calc_series(self):
        limit = self._series
        f = [1000000]  # Square Root starting array/list
        while limit > 0:
            self.set_data(f[0])
            f = [math.sqrt(f[0])]
            limit -= 1

    """Method/Function to set Square Root data: list, dict, and dictID are instance variables of Class"""

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
    n = 6
    '''Constructor of Class object'''
    sqrt = Sqrt(n)

    '''Using getters to obtain data from object'''
    print(f"Square Root number for {n} = {sqrt.number}")
    print(f"Sqaure Root series for {n} = {sqrt.list}")

    '''Using method to get data from object'''
    for i in range(n):
        print(f"Square Root sequence {i + 1} = {sqrt.get_sequence(i)}")
