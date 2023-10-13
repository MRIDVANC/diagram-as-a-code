from diagrams import Diagram
from diagrams.openstack.compute import Nova
from diagrams.openstack.networking import Neutron
from diagrams.openstack.storage import Cinder
from diagrams.oci.compute import BareMetal
from diagrams.oci.connectivity import Backbone
from customs.ansible import



with Diagram("Openstack Cloud", show=False, direction="TB"):
    # Datacenter1
    backbone1 = Backbone("Backbone1")
    backbone2 = Backbone("Backbone2")
    backbone3 = Backbone("Backbone3")
    backbone4 = Backbone("Backbone4")
    backbone5 = Backbone("Backbone5")
    backbone6 = Backbone("Backbone6")
    backbone7 = Backbone("Backbone7")
    backbone8 = Backbone("Backbone8")
    backbone9 = Backbone("Backbone9")
    backbone10 = Backbone("Backbone10")
    backbone11 = Backbone("Backbone11")


    backbone1 >> [
        # Sunucular
        BareMetal("Sunucu1"),
        BareMetal("Sunucu2"),
        BareMetal("Sunucu3"),
        BareMetal("Sunucu4"),
        BareMetal("Sunucu5"),
        BareMetal("Sunucu6"),
        BareMetal("Sunucu7"),
        BareMetal("Sunucu8"),
        BareMetal("Sunucu9"),
        BareMetal("Sunucu10"),
    ] >> backbone2
    backbone2 >> [
        # Ceph1
        Cinder("Ceph1"),
        Cinder("Ceph2"),
        Cinder("Ceph3"),
    ]

    # Datacenter2
    backbone3 = Backbone("Backbone3")
    backbone3 >> [
        # Sunucular
        BareMetal("Sunucu11"),
        BareMetal("Sunucu12"),
        BareMetal("Sunucu13"),
        BareMetal("Sunucu14"),
        BareMetal("Sunucu15"),
        BareMetal("Sunucu16"),
        BareMetal("Sunucu17"),
        BareMetal("Sunucu18"),
        BareMetal("Sunucu19"),
        BareMetal("Sunucu20"),
    ] >> backbone4
    backbone4 >> [
        # Ceph4
        Cinder("Ceph4"),
        Cinder("Ceph5"),
        Cinder("Ceph6"),
    ]

    # ...

    # Datacenter10
    backbone10 = Backbone("Backbone10")
    backbone10 >> [
        # Sunucular
        BareMetal("Sunucu101"),
        BareMetal("Sunucu102"),
        BareMetal("Sunucu103"),
        BareMetal("Sunucu104"),
        BareMetal("Sunucu105"),
        BareMetal("Sunucu106"),
        BareMetal("Sunucu107"),
        BareMetal("Sunucu108"),
        BareMetal("Sunucu109"),
        BareMetal("Sunucu110"),
    ] >> backbone11
    backbone11 >> [
        # Ceph10
        Cinder("Ceph10"),
        Cinder("Ceph11"),
        Cinder("Ceph12"),
    ]

    # Backboneler
    backbone1 >> backbone2
    backbone3 >> backbone4
    ...
    backbone9 >> backbone10