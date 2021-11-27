# Microsoft SD-WAN computing allocations over a set of tunnels
# Author: Sevval Simsek - Boston University
import math
import sys
from dataclasses import dataclass
@dataclass
class Flow:
    name: str
    type: str
    demand: float

# Beginning - initializations
temp = Flow('Fa', 'interactive', 15)
temp1 = Flow('Fb', 'elastic', 10)
temp2 = Flow('Fc', 'background', 5)
flows = [temp, temp1, temp2]  # should be a number or maybe list of flows?
numflows = len(flows)
priorities = {'interactive', 'elastic', 'background'}
MAX_INT = sys.maxint
capacity_links = [5, 5, 5, 10, 5, 5] # 5 links total, links not determined here1
rem_c = capacity_links.copy()
demands = [] #demands for each source destination pair
tunnels = {}

# End - initializations

def swan_allocation():
    for pri in priorities:
        tunnels.add(throughput_max(pri, rem_c))
    return tunnels


def throughput_max(priority, rem_c):
    return MCF(priority, rem_c, 0, MAX_INT, None)

def getmaxDemand():
    max_d = 0
    for f in flows:
        if f.demand > max_d:
            max_d = f.demand
    return max_d

def appx_maxmin(alpha, U, pri,rem_c):
    F = {}
    d_max = getmaxDemand()
    T = math.ceil(math.log(d_max/U,alpha))
    for k in range(1,T):
        list_b = MCF(pri, rem_c, math.pow(alpha,k-1)*U,math.pow(alpha,k)*U,F)
        for b_i in list_b:
            if b_i not in F and b_i < min(demands[k]):  #not sure, it must be i
                pass


def MCF(priority, rem_c, b_low, b_high: float, F):
    for i in range(numflows):
        if i in F:
            b_i = F[i]
        else:
            min_b = min(b_high, flows[i].demand)


if __name__ == '__main__':
    allocation_map = swan_allocation()
