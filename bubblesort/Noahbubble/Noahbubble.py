import numpy as np


class BubbleSort:
    def __init__(self, smallestNum, largestNum, totalNum):

        while smallestNum >= largestNum:
            print("Invalid number entered. Largest number must be greater than smallest number.")
            largestNum = int(input("Enter largest number: "))
        # Generate random array based on user input
        array = np.random.randint(smallestNum, largestNum, totalNum)
        self._original = ", ".join(str(v) for v in array)
        # Traverse through all array arrays
        self._log = []
        for i in range(totalNum - 1):
            # Traverse the array from 0 to n-i-1
            for j in range(0, totalNum - i - 1):
                # Swap if the array found is greater
                # than the next array
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
                    self._log.append(str(array))
        self._bubblesort = ", ".join(str(v) for v in array)

    @property
    def original(self):
        return self._original

    @property
    def log(self):
        return self._log

    @property
    def bubblesort(self):
        return self._bubblesort
