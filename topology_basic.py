# coding=UTF-8
from mininet.net import Mininet
from mininet.node import CPULimitedHost  # cpu Related settings
from mininet.node import OVSController
from mininet.link import TCLink  # addLink Related settings

net = Mininet(link=TCLink, controller=OVSController)

c0 = net.addController()  # SWAN controller
# Datacenter with switches and network agents etc.
h1 = net.addHost('h1')
h2 = net.addHost('h2')
h3 = net.addHost('h3')
h4 = net.addHost('h4')

net.addlink(h1, h2, bw=10)
net.addlink(h2, h3, bw=10)
net.addlink(h3, h4, bw=10)
net.addlink(h1, h4, bw=10)
net.addlink(h2, h4, bw=10)

h1.setIP('10.0.0.1', 24)
h2.setIP('10.0.0.2', 24)
h3.setIP('10.0.0.3', 24)
h4.setIP('10.0.0.4', 24)

net.start()
net.pingAll()
net.stop()
