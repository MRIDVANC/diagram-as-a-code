from diagrams.custom import Custom
from urllib.request import urlretrieve


class RHEL(Custom):
  def __init__(self):
    _url = "https://raw.githubusercontent.com/MRIDVANC/diagram-as-a-code/master/Custom-Nodes/rhel.png"
    _icon = "rhel.png"
    _label = "Red Hat"
    urlretrieve(_url, _icon)
    super().__init__(_label, _icon)
