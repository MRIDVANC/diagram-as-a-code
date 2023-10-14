from diagrams.custom import Custom
from urllib.request import urlretrieve


class Ansible(Custom):
  def __init__(self):
    _url = "https://raw.githubusercontent.com/MRIDVANC/diagram-as-a-code/master/Custom-Nodes/ansible.png"
    _icon = "ansible.png"
    _label = "Ansible"
    urlretrieve(_url, _icon)
    super().__init__(_label, _icon)

class Ansible_Tower(Custom):
  def __init__(self):
    _url = "https://raw.githubusercontent.com/MRIDVANC/diagram-as-a-code/master/Custom-Nodes/ansible_tower.png"
    _icon = "ansible_tower.png"
    _label = "Ansible Tower"
    urlretrieve(_url, _icon)
    super().__init__(_label, _icon)

    class Ansible_Playbook(Custom):
      def __init__(self):
        _url = "https://raw.githubusercontent.com/MRIDVANC/diagram-as-a-code/master/Custom-Nodes/ansible_playbook.png"
        _icon = "ansible_playbook.png"
        _label = "Ansible Playbook"
        urlretrieve(_url, _icon)
        super().__init__(_label, _icon)