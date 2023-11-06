from diagrams import Diagram, Cluster
from diagrams.oci.compute import BareMetal, BM
from diagrams.oci.connectivity import Backbone
from customs.rhel import LogoAnsible


with (Diagram("Openstack Cloud", show=False, direction="TB")):
    # Datacenter1
    backbone1 = Backbone("Backbone1")
    backbone2 = Backbone("Backbone2")
    server1: BM = BareMetal("CTR01")
    server2: BM = BareMetal("CTR02")
    logo_ansible = LogoAnsible()

    with Cluster("CONTROL GROUP"):
        ctrsrv = logo_ansible >> [server1, server2]

    with Cluster("CABINET1"):
        eor1 = backbone1 >> [
            # Sunucular
            server1,
            BareMetal("gbcpcpt02"),
            BareMetal("Sunucu3"),
            BareMetal("Sunucu4"),
            BareMetal("Sunucu5"),
            BareMetal("Sunucu6"),
            BareMetal("Sunucu7"),
            BareMetal("Sunucu8"),
            BareMetal("Sunucu9"),
            BareMetal("Sunucu10"),
        ]

    with Cluster("CABINET"):
        eor2 = backbone2 >> [
            # Sunucular
            server2,
            BareMetal("Sunucu12"),
            BareMetal("Sunucu13"),
            BareMetal("Sunucu14"),
            BareMetal("Sunucu15"),
            BareMetal("Sunucu16"),
            BareMetal("Sunucu17"),
            BareMetal("Sunucu18"),
            BareMetal("Sunucu19"),
            BareMetal("Sunucu20"),

        ]
