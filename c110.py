import plotly.figure_factory as ff
import pandas as pd
import statistics
import random
import plotly.graph_objects as go

df = pd.read_csv("newData.csv")

data = df["average"].tolist()

#mean = statistics.mean(data)
#print(mean)

std_dev = statistics.stdev(data)
print(std_dev)

#fig = ff.create_distplot([data],["average"],show_hist=False)

#fig.show()
"""
dataset = []

for i in range(0,100):
    random_index = random.randint(0,len(data))
    value = data[random_index]
    dataset.append(value)
sample_mean = statistics.mean(dataset)
sample_stdev = statistics.stdev(dataset)

print("sample_mean: ",sample_mean)
print("sample_stdev: ",sample_stdev)
"""
def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([df],["average"],show_hist=False)
    fig.add_trace(go.Scatter(x = [mean,mean],y = [0,1],mode = "lines",name = "mean"))
    fig.show()

def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_mean = random_set_of_mean(100)
        mean_list.append(set_of_mean)

    show_fig(mean_list)
    mean = statistics.mean(mean_list)
    print("sample mean is ",mean)
setup()
mean = statistics.mean(data)
print("population mean is ",mean)
def standerd_deviation():
    mean_list = []
    for i in range(0,1000):
        set_of_mean = random_set_of_mean(100)
        mean_list.append(set_of_mean)

    std_dev = statistics.stdev(mean_list)
    print("standered deviation of sample is ",std_dev)

standerd_deviation()












