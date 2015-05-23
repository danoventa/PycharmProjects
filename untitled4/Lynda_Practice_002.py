__author__ = 'Executor'

class inclusive_range:
    def __init__(self, *args):
        numargs = len(args)
        if numargs < 1: raise TypeError('requires lest 1')
        elif numargs == 1:
            self.stop = args[0]
            self.start = 0
            self.step = 1
        elif numargs == 2:
            (self.start, self.stop) = args
            self.step = 1
        elif numargs == 3:
            (self.start, self.stop, self.step) = args
        else: raise TypeError('we expect moar! Only give {}'. format(numargs))

    def __iter__(self):
        i = self.start
        while i <= self.stop:
            yield i
            i += self.step

def main():
    o = range(5, 25)
    for i in o: print(i, end = ' ')

    oi = inclusive_range(5, 25, 7)
    for i in oi: print(i, end = ' ')

if __name__ == "__main__" :
    main()