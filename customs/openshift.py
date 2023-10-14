from diagrams.custom import Custom
from urllib.request import urlretrieve


class Openshift(Custom):
  def __init__(self):
    _url = "https://raw.githubusercontent.com/MRIDVANC/diagram-as-a-code/master/Custom-Nodes/openshift.png"
    _icon = "openshift.png"
    _label = "Openshift"
    urlretrieve(_url, _icon)
    super().__init__(_label, _icon)
