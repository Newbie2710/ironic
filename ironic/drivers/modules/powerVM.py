from ironic.openstack.common import log as logging

LOG = logging.getLogger(__name__)
class DummyUtility(object):

  def validate(self, task, node):
    pass
  
  def prepare(self, task, node):
    pass
  
  def deploy(self, task, node):
    LOG.info(_(‘PowerVM driver has been implemented!!!’))
