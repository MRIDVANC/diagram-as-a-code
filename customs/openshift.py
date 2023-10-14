from diagrams.custom import Custom
from urllib.request import urlretrieve

from constants.constant import OPENSHIFT_LOGO


class Openshift(Custom):

  def __init__(self):
    _url = OPENSHIFT_LOGO
    _icon = "openshift.png"
    _label = "openshit"
    urlretrieve(_url, _icon)
    super().__init__(_label, _icon)

