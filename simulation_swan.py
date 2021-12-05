import simpy

import os
import time
import loadfiles
import swan_controller

# This represents the G-Scale setup, without the actual network data. Max demand is for simulation purposes.
MAX_DEMAND = 80 # from the paper
NUM_DC = 12
NUM_LINKS = 19

flows = {}
datacenters = []
links = {}

def load_data():
    flow_int, flow_el, flow_bac = loadfiles.readFiles()
    flows['interactive'] = flow_int
    flows['elastic'] = flow_el
    flows['background'] = flow_bac

    links = loadfiles.readLinks()
    lenLinks = len(links)
    # For each link pair, if bidirectional, we add the return link to list, too.
    # This can be skipped if the processing takes into account the bidirectional links.
    for i in range(0,lenLinks):
        link = links[i]
        if link['Bidirectional'] == 'y':
            tmp = {
                'Ingress': link['Egress'],
                'Egress': link['Ingress'],
                'Bidirectional': 'y'
            }
            links.append(tmp)


if __name__ == "__main__":
    load_data()
