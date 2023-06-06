import numpy as np

class Tal:
    def __init__(self, Threshold, Array):
        self.Threshold = Threshold
        self.Array = Array

    def Run(self):
        try:
            mean = np.mean(self.Array)
            print(mean)
        except Exception as e:
            print(e)

array = [
    [1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 20, 30], [40, 50, 60], [70, 80, 90]
]


A = Tal(Threshold=0.001, Array=np.array(array))
A.Run()

# TODO:Syncronize GIT with IDE.