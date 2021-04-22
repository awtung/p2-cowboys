"""Factorial algorithm contained within a class """


class NoahBubbleSort:
    """Initializer of class takes series parameter and returns Class Objectg"""
    def __init__(self, series, arr):
        self._series = series
        self._list = []
        self._dict = {}
        self._dictID = 0
        # Duration timeElapsed;
        # Instant start = Instant.now();  // time capture -- start
        self.calc_series(arr)
        # Instant end = Instant.now();    // time capture -- end
        # this.timeElapsed = Duration.between(start, end);

    """Algorithm for building Factorial sequence, this id called from __init__"""
    def calc_series(self, arr):
        n = len(arr)

        # Traverse through all array elements
        for i in range(n):

            # Last i elements are already in place
            for j in range(0, n-i-1):

                # traverse the array from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                if arr[j] > arr[j+1] :
                    arr[j], arr[j+1] = arr[j+1], arr[j]
    arr = [64, 34, 25, 12, 22, 11, 90]

    calc_series(arr)

    print ("Sorted array is:")
    for i in range(len(arr)):
        print ("%d" %arr[i]),

    """Method/Function to set Factorial data: list, dict, and dictID are instance variables of Class"""
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
    n = 0
    '''Constructor of Class object'''
    noahbubblesort = NoahBubbleSort(n)

    '''Using getters to obtain data from object'''
    print(f"Factorial number for {n} = {noahbubblesort.number}")
    print(f"Factorial series for {n} = {noahbubblesort.list}")

    '''Using method to get data from object'''
    for i in range(n):
        print(f"Factorial sequence {i + 1} = {noahbubblesort.get_sequence(i)}")