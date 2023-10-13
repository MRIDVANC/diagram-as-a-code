from diagrams.custom import Custom
from urllib.request import urlretrieve


class Ansible(Custom):
  def __init__(self):
    _url = "https://raw.githubusercontent.com/MRIDVANC/diagram-as-a-code/master/Custom-Nodes/ansible-logo.png"
    _icon = "ansible.png"
    _label = "Ansible"
    urlretrieve(_url, _icon)
    super().__init__(_label, _icon)

class Ansible_Tower(Custom):
  def __init__(self):
    _url = "https://raw.githubusercontent.com/MRIDVANC/diagram-as-a-code/master/Custom-Nodes/ansible-logo.png"
    _icon = "ansible.png"
    _label = "Ansible"
    urlretrieve(_url, _icon)
    super().__init__(_label, _icon)