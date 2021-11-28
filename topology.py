# coding=UTF-8
from mininet.net import Mininet
from mininet.node import CPULimitedHost # cpu Related settings
from mininet.node import OVSController
from mininet.link import TCLink # addLink Related settings
net = Mininet(link=TCLink,controller = OVSController)

c0 = net.addController() # SWAN controller
# Datacenter with switches and network agents etc.
h1 = net.addHost('h1')
h2 = net.addHost('h2')
h3 = net.addHost('h3')
h4 = net.addHost('h4')
h5 = net.addHost('h5')
s1 = net.addSwitch('s1') # service broker 1
s2 = net.addSwitch('s2') # service broker 2

# Creating links between nodes
net.addLink(h1, s1, bw=10, delay='5ms',max_queue_size=1000, loss=10, use_htb=True) #bandwidth bw,delayed delay Etc
net.addLink(h2, s1)
net.addLink(h3, s1, bw=10, delay='5ms',max_queue_size=1000, loss=10, use_htb=True) #bandwidth bw,delayed delay Etc
net.addLink(h4, s2)
net.addLink(h5, s2)
net.addLink(s1, c0)
net.addLink(s2, c0)

# Datacenter with inter-DC traffic omitted
dc1 = net.addHost('dc1')
dc2 = net.addHost('dc2')
dc3 = net.addHost('dc3')
dc4 = net.addHost('dc4')
dc5 = net.addHost('dc5')

# Creating links between nodes
net.addLink(dc1, c0)
net.addLink(dc2, c0)
net.addLink(dc3, c0)
net.addLink(dc4, c0)
net.addLink(dc5, c0)

# Configure all host ip
h1.setIP('10.0.0.1', 24)
h2.setIP('10.0.0.2', 24)
h3.setIP('10.0.0.3', 24)
h4.setIP('10.0.0.4', 24)
h5.setIP('10.0.0.5', 24)
dc1.setIP('10.0.0.6', 24)
dc2.setIP('10.0.0.7', 24)
dc3.setIP('10.0.0.8', 24)
dc4.setIP('10.0.0.9', 24)
dc5.setIP('10.0.0.10', 24)

net.start()
net.pingAll()
net.stop()