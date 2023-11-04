from urllib.request import urlretrieve
from diagrams.custom import Custom
from constants.constant import ANSIBLE_LOGO, OPENSHIFT_LOGO


class Rhel(Custom):
    def __init__(self):
        _url = "https://raw.githubusercontent.com/MRIDVANC/diagram-as-a-code/master/custom_icons/rhel/rhel.png"
        _icon = "rhel.png"
        _label = "Red Hat"
        urlretrieve(_url, _icon)
        super().__init__(_label, _icon)


class LogoAnsible(Custom):
    def __init__(self):
        _url = ANSIBLE_LOGO
        _icon = "ansible.png"
        _label = "Ansible"
        urlretrieve(_url, _icon)
        super().__init__(_label, _icon)


class TowerAnsible(Custom):
    def __init__(self):
        _url = ("https://raw.githubusercontent.com/MRIDVANC/diagram-as-a-code/master/custom_icons/ansible"
                "/ansible_tower.png")
        _icon = "ansible_tower.png"
        _label = "Ansible Tower"
        urlretrieve(_url, _icon)
        super().__init__(_label, _icon)


class PlaybookAnsible(Custom):
    def __init__(self):
        _url = ("https://raw.githubusercontent.com/MRIDVANC/diagram-as-a-code/master/custom_icons/ansible"
                "/ansible_playbook.png")
        _icon = "ansible_playbook.png"
        _label = "Ansible Playbook"
        urlretrieve(_url, _icon)
        super().__init__(_label, _icon)


class Openshift(Custom):
    def __init__(self, label):
        _url = OPENSHIFT_LOGO
        _icon = "openshift.png"
        _label = label
        urlretrieve(_url, _icon)
        super().__init__(_label, _icon)
