# Microsoft SD-WAN computing allocations over a set of tunnels
# Author: Sevval Simsek - Boston University
import math
import sys
from dataclasses import dataclass

@dataclass
class Flow:
    type: str
    demand: float
    allocation: float

class Tunnel:
    ingress: str
    egress: str

# Global parameters
priorities = {'interactive', 'elastic', 'background'}
scratch = {'interactive': 0.05, 'elastic': 0.05, 'background': 0.05}
MAX_INT = sys.maxint
tunnels = []  # todo: populate these two
links = []
I_matrix = [[0 for i in range(len(links))] for j in range(len(tunnels))]

flows = [] # todo: call readFiles and load flows
numFlows = len(flows)

capacity_links = [5, 5, 5, 10, 5, 5]  # 5 links total, links not determined here
rem_c = capacity_links.copy()


# End - initializations

def swan_allocation():
    for pri in priorities:
        tunnels.append(throughput_max(pri, rem_c))
    return tunnels


def throughput_max(priority, rem_c):
    return MCF(priority, rem_c, 0, MAX_INT, None)

def getmaxDemand():
    max_d = 0
    for f in flows:
        if f.demand > max_d:
            max_d = f.demand
    return max_d

def getDemandList():
    demands = []
    for f in flows:
        demands.append(f.demand)
    return demands

def appx_maxmin(alpha, U, pri, rem_c):
    F = [] # todo: learn what this is
    d_max = getmaxDemand()
    T = math.ceil(math.log(d_max / U, alpha))
    f_list = []
    for k in range(1, T):
        list_b = MCF(pri, rem_c, math.pow(alpha, k - 1) * U, math.pow(alpha, k) * U, F)
        for i in range(len(list_b)):
            if i not in F and list_b[i] < min([k], math.pow(alpha,k)*U):
                F.append(i)
                f_list.append(list_b[i])
    return f_list

# Multi-commodity flow problem
def MCF(priority: str, rem_c, b_low: float, b_high: float, F):
    list_b = []
    for i in range(numFlows):
        if i in F:
            b_i = F[i]
            list_b[i] = b_i
        else:
            max_b = min(b_high, flows[i].demand)
            min_b = b_low
            # constraint: min_b < b < max_b
            b_i = math.floor((min_b + max_b) / 2)  # average approach, todo: make sure this is true

            # another constraint, for each link, allocation sum must be less than remaining capacity
            for l in range(len(links)):
                s_cap = scratch.get(priority)
                min_capacity = min(rem_c[l], (1-s_cap)*capacity_links[l])


            list_b[i] = b_i
    return list_b

if __name__ == '__main__':
    allocation_map = swan_allocation()
