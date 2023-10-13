from diagrams import Diagram, Cluster
from diagrams.custom import Custom
from urllib.request import urlretrieve

from customs.ansible import Ansible

with Diagram("Custom with remote icons", show=False, filename="custom_remote", direction="LR"):
  ansible = Ansible()
  with Cluster("Some Providers"):

    openstack_url = "https://github.com/mingrammer/diagrams/raw/master/resources/openstack/openstack.png"
    openstack_icon = "openstack.png"
    urlretrieve(openstack_url, openstack_icon)

    openstack = Custom("OpenStack", openstack_icon)

    elastic_url = "https://github.com/mingrammer/diagrams/raw/master/resources/elastic/saas/elastic.png"
    elastic_icon = "elastic.png"
    urlretrieve(elastic_url, elastic_icon)

    elastic = Custom("Elastic", elastic_icon)

  diagrams >> openstack
  diagrams >> elastic