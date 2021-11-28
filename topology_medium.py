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
h5 = net.addHost('h5')
h6 = net.addHost('h6')
h7 = net.addHost('h7')

net.addlink(h1, h2, bw=10)
net.addlink(h2, h3, bw=10)
net.addlink(h3, h4, bw=10)
net.addlink(h4, h5, bw=10)
net.addlink(h5, h6, bw=10)
net.addlink(h6, h7, bw=10)
net.addlink(h1, h7, bw=10)
net.addlink(h2, h6, bw=10)

h1.setIP('10.0.0.1', 24)
h2.setIP('10.0.0.2', 24)
h3.setIP('10.0.0.3', 24)
h4.setIP('10.0.0.4', 24)
h5.setIP('10.0.0.5', 24)
h6.setIP('10.0.0.6', 24)
h7.setIP('10.0.0.7', 24)

net.start()
net.pingAll()
net.stop()
