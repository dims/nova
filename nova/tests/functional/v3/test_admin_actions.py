# Copyright 2012 Nebula, Inc.
# Copyright 2013 IBM Corp.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from oslo_config import cfg

from nova.tests.functional.v3 import test_servers

CONF = cfg.CONF
CONF.import_opt('osapi_compute_extension',
                'nova.api.openstack.compute.legacy_v2.extensions')


class AdminActionsSamplesJsonTest(test_servers.ServersSampleBase):
    extension_name = "os-admin-actions"
    # TODO(gmann): Overriding '_api_version' till all functional tests
    # are merged between v2 and v2.1. After that base class variable
    # itself can be changed to 'v2'
    _api_version = 'v2'
    extra_extensions_to_load = ["os-access-ips"]

    def _get_flags(self):
        f = super(AdminActionsSamplesJsonTest, self)._get_flags()
        f['osapi_compute_extension'] = CONF.osapi_compute_extension[:]
        f['osapi_compute_extension'].append(
            'nova.api.openstack.compute.contrib.admin_actions.Admin_actions')
        return f

    def setUp(self):
        """setUp Method for AdminActions api samples extension

        This method creates the server that will be used in each tests
        """
        super(AdminActionsSamplesJsonTest, self).setUp()
        self.uuid = self._post_server()

    def test_post_reset_network(self):
        # Get api samples to reset server network request.
        response = self._do_post('servers/%s/action' % self.uuid,
                                 'admin-actions-reset-network', {})
        self.assertEqual(response.status_code, 202)

    def test_post_inject_network_info(self):
        # Get api samples to inject network info request.
        response = self._do_post('servers/%s/action' % self.uuid,
                                 'admin-actions-inject-network-info', {})
        self.assertEqual(response.status_code, 202)

    def test_post_reset_state(self):
        # get api samples to server reset state request.
        response = self._do_post('servers/%s/action' % self.uuid,
                                 'admin-actions-reset-server-state', {})
        self.assertEqual(response.status_code, 202)
