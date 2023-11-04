from diagrams import Cluster, Diagram, Edge
from diagrams.oci.connectivity import Backbone
from diagrams.onprem.compute import Server
from diagrams.onprem.monitoring import Grafana, Prometheus

with (Diagram(name="GBZ-SRV01 BAGLANTI", show=False)):
    metrics = Prometheus("metric")
    metrics << Edge(color="firebrick", style="dashed") << Grafana("monitoring")

    with Cluster("GBZ-NDC-SRV01"):
        grpcsvc = [Server("GBZ-SRV01")]

    with Cluster("NFVC vPC"):
        primary = Backbone("primary")
        primary - Edge(color="dark red", style="dashed") << Edge(label="collect") << metrics
        secondary = Backbone("secondary")
        grpcsvc >> Edge(color="dark red") >> primary
        grpcsvc >> Edge(color="dark reds") >> secondary

    with Cluster("NFVM LACP"):
        primary = Backbone("primary")
        primary - Edge(color="blue", style="dashed") << Edge(label="collect") << metrics
        secondary = Backbone("secondary")
        grpcsvc >> Edge(color="blue") >> primary
        grpcsvc >> Edge(color="blue") >> secondary
