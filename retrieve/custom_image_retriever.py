import diagrams.custom

from urllib.request import urlretrieve

from diagrams import Diagram


class Ansible:
    def __init__(self):
        _url = "https://raw.githubusercontent.com/MRIDVANC/diagram-as-a-code/master/Custom-Nodes/ansible-logo.png"
        _icon = "ansible.png"
        _label = "Ansible"
        urlretrieve(_url, _icon)
        self.custom = diagrams.Custom(_label, _icon)

    def get_custom(self):
        return self.custom


with Diagram("Custom with remote icons", show=False, filename="abc", direction="LR"):
    ansible = diagrams.custom.Custom(Ansible().get_custom())



