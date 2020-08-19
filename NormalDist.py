import plotly.figure_factory as ff
import csv
import statistics
import random
import pandas as pd 
import plotly.graph_objects as go

df = pd.read_csv('data2.csv')
data = df['temp'].tolist()
dataSet = []
#for i in range(0 , 100):
 #   randomIndex = random.randint(0 , len(data))
 #   value = data[randomIndex]
 #   dataSet.append(value)
#sampleMean = statistics.mean(dataSet)
#populationMean = statistics.mean(data)
#standaredDiviation = statistics.stdev(data)
#standaredDiviation2 = statistics.stdev(dataSet)
#print(populationMean , standaredDiviation)
#print(sampleMean , standaredDiviation2)

def randomSetOfMean(counter):
    dataSet2 = []
    for i in range(0 , counter):
      randomIndex = random.randint(0 , len(data) -1)
      value = data[randomIndex]
      dataSet2.append(value)
    mean = statistics.mean(dataSet2)
    return mean

def showFig(meanList):
    df = meanList
    fig = ff.create_distplot([df] , ['Temparature'] , show_hist = False)
    mean = statistics.mean(meanList)
    standDev = statistics.stdev(meanList)
    print(mean , standDev)
    fig.add_trace(go.Scatter(x = [mean , mean] , y = [0 , 1] , mode = 'lines' , name ='mean'))
    fig.show()

def setup():
    meanList = []
    for i in range(0 , 1000):
        SetOfMean = randomSetOfMean(200)
        meanList.append(SetOfMean)

    showFig(meanList)

setup()
