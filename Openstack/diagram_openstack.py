from diagrams import Diagram
from diagrams.openstack.compute import Nova
from diagrams.openstack.networking import Neutron
from diagrams.openstack.storage import Cinder
from diagrams.oci.compute import VirtualMachine
from diagrams.oci.network import RouteTable
with Diagram("Openstack Test1", show=False, direction="TB"):
    Neutron("OS Switch") >> [Nova("Sunucu"),
                  Cinder("CEPH"),
                  VirtualMachine("DGW"),
                  RouteTable("RT"),
                  Nova("Sunucu2")] >> VirtualMachine('DGW1')