
import matplotlib.pyplot as plt
import operator
from frequency import *


def plotFrequencyBar(freqDict):
    print(freqDict)
    lists = sorted(freqDict.items(), key=operator.itemgetter(1), reverse=True)[0:10]
    print("lol")
    terms, counts = zip(*lists)

    r = range(len(terms))

    plt.xticks(r, terms)

    plt.bar(r, counts, align='center')

    plt.show()


#if __name__ == '__main__':
    #plotFrequencyBar(sys.argv[1])
