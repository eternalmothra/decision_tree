import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

RG = nx.Graph()

rd = 'RD'
prob = 'Problem'

print "For all COSTS enter a negative number. For all GAINS enter a positive number"

lose = float(raw_input("How much revenue will you LOSE if you DON'T do this research? (negative) "))

gain = float(raw_input("How much revenue will you GAIN if you DO this research? "))

b_cost = float(raw_input("How much will it cost you to do this research? (negative) " ))

p_minor = float(raw_input("Predict how likely you are to have a MINOR problem (number between 0 and 1): "))
minor_cost = float(raw_input("How much will it cost to have a MINOR problem? (negative) "))

p_major = float(raw_input("Predict how likely you are to have a MAJOR problem (number between 0 and 1): "))
major_cost = float(raw_input("How much will it cost to have a MAJOR problem? (negative) "))

p_none = 1.0 -(p_minor+p_major)

def utility(r ='yes', problem_cost = 0):
    if r =='no':
        return lose
    else:
        u = gain+b_cost+problem_cost
        return u
        
def exp_value(r='yes'):
    val = p_minor*utility(problem_cost = minor_cost)+p_major*utility(problem_cost = major_cost)+p_none*utility()
    if r == 'no':
        return lose
    else:
        return val      
    
print "Should you do this research?"
print "Your value if you DON'T ",
print exp_value(r='no')
print "Your value if you DO ",
print exp_value()

if exp_value()>exp_value(r='no'):
    print "YES"
else:
    print "NO"    
    
RG.add_nodes_from([0,1,2,3,4,5])
pos = {0: np.array([0.4, 1.0]), 1: np.array([0.6, 0.6]), 2: np.array([0.0, 0.6]), 3: np.array([0.2, 0.0]), 4:np.array([0.6, 0.0]), 5:np.array([1.0, 0.0])}


nx.draw_networkx_nodes(RG, pos, nodelist=[0], node_shape = 's', node_size =1000) #rd
nx.draw_networkx_nodes(RG, pos, nodelist=[1], node_shape = 'o', node_size =1000) #problem
nx.draw_networkx_nodes(RG, pos, nodelist=[2,3,4,5], node_shape = 'd', node_size =1000) #utilities

                   
                   

nx.draw_networkx_edges(RG,pos, edgelist=[(0,1), (0,2), (1,3), (1,4), (1,5)], width=8,alpha=0.5,edge_color='r')

labels={}
labels[0] = rd
labels[1] = prob
labels[2] = int(utility(r='no'))
labels[3] = int(utility(problem_cost = minor_cost))
labels[4] = int(utility())
labels[5] = int(utility(problem_cost = major_cost))

e_label = {}
e_label[(0,1)] = 'yes'
e_label[(0,2)] = 'no'
e_label[(1,3)] = 'minor (p ='+str(p_minor)+')'
e_label[(1,4)] = 'none (p ='+str(p_none)+')'
e_label[(1,5)] = 'major (p ='+str(p_major)+')'

nx.draw_networkx_labels(RG,pos,labels,font_size=16)
nx.draw_networkx_edge_labels(RG, pos, edge_labels=e_label)


plt.show()