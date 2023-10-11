from diagrams import Diagram, Cluster
from diagrams.custom import Custom
from urllib.request import urlretrieve

with Diagram("Custom with remote icons", show=False, filename="custom_remote", direction="LR"):

  # download the icon image file
  diagrams_url = "https://github.com/mingrammer/diagrams/raw/master/assets/img/diagrams.png"
  diagrams_icon = "diagrams.png"
  urlretrieve(diagrams_url, diagrams_icon)

  diagrams = Custom("Diagrams", diagrams_icon)

  with Cluster("Some Providers"):
      openshift_url ="https://github.com/MRIDVANC/diagram-as-a-code/blob/master/Custom-Nodes/openshift-logo.png"
      openshift_icon ="openshift-logo.png"

      openshift = Custom("openshift", openshift_icon)


  diagrams >> openshift