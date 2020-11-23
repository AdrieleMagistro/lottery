import random
import math
import copy
import matplotlib.pyplot as plt
import pandas as pd
import statistics as st

#passare questi numeri come parametri da terminale
M = 10
N = 5
tickets = [i for i in range(M)]
tickets_sold = []
people = [i for i in range(N)]

lottery = {}
history = {}
stat= {}
m = M
n = N

# Selling tickets
for p in people:
    #nr_tickets_max = math.ceil(m/n)
    nr_tickets_max = random.randint(1, math.ceil(m/n))
    myTickets = []
    for i in range(nr_tickets_max):
        ticket = random.choice(tickets)
        tickets.remove(ticket)
        tickets_sold.append(ticket)
        m -= 1
        myTickets.append(ticket)
    lottery[p] = myTickets 
    history[p] = 0
    stat[p] = []
    n -= 1

# Fill missing values
while tickets:
    p = random.choice(people)
    ticket = random.choice(tickets)
    tickets.remove(ticket)
    tickets_sold.append(ticket)
    lottery[p].append(ticket) 

def plot(data):
    data['mean'].plot(
            kind='bar',
            yerr = data['std'] * 1.96)
    plt.show()

def game(lot, his, sta):
    nr_tests = 0
    tot_tests = 30
    while nr_tests < tot_tests:
        h = copy.copy(his)
        i = 0
        tot = 1000
        while(i < tot):
            winner = random.choice(tickets_sold)
            for (k,v) in lot.items():
                if winner in v:
                    h[k] += 1
            i += 1

        for (p,r) in h.items():
            nr_w = (r/tot)*100
            sta[p].append(round(nr_w, 2))
        nr_tests += 1
    print("Standard Deviation")
    for p in h.keys():
        print(str(p)+": "+str(st.stdev(sta[p])))
    print(sta) 

    temp_dict = {}
    for k in sta.keys():
        temp_dict[k] = [st.mean(sta[k]), st.stdev(sta[k])] 

    print(temp_dict)

    df = pd.DataFrame.from_dict(temp_dict, orient='index', columns=['mean', 'std'])

    plot(df)
    return df

def fake_game(lot, his, sta):
    nr_tests = 0
    tot_tests = 30
    while nr_tests < tot_tests:
        h = copy.copy(his)
        i = 0
        tot = 1000
        while(i < tot):
            winner = random.choice(people)
            h[winner] += 1
            i += 1

        for (p,r) in h.items():
            nr_w = (r/tot)*100
            sta[p].append(round(nr_w, 2))
        nr_tests += 1
    print("Standard Deviation")
    for p in h.keys():
        print(str(p)+": "+str(st.stdev(sta[p])))
    print(sta) 

    temp_dict = {}
    for k in sta.keys():
        temp_dict[k] = [st.mean(sta[k]), st.stdev(sta[k])] 

    print(temp_dict)

    df = pd.DataFrame.from_dict(temp_dict, orient='index', columns=['mean', 'std'])

    plot(df)
    return df

df = game(lottery, history, stat)