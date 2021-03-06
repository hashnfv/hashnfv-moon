# Copyright 2015 Open Platform for NFV Project, Inc. and its contributors
# This software is distributed under the terms and conditions of the 'Apache-2.0'
# license which can be found in the file 'LICENSE' in this package distribution
# or at 'http://www.apache.org/licenses/LICENSE-2.0'.
"""
Assignments allow to connect data with elements of perimeter

"""

from flask import request
from flask_restful import Resource
# from oslo_config import cfg
from oslo_log import log as logging
# from moon_interface.tools import check_auth

__version__ = "0.1.0"

LOG = logging.getLogger(__name__)
# CONF = cfg.CONF


class Messenger(Resource):
    """
    Endpoint for messenger requests
    """

    __urls__ = (
        "/configuration/messenger",
    )

    def __init__(self, *args, **kwargs):
        self.conf = kwargs.get('conf', {})

    # @check_auth
    def get(self):
        """Retrieve messenger configuration

        :return: {
            "messenger": {
                "hostname": "hostname for the messenger server",
                "port": "port for the main messenger server",
                "user": "user for the main messenger server",
                "password": "password for the main messenger server",
                "protocol": "protocol to use (eg. rabbit)"
            }
        }
        """
        url = self.conf.TRANSPORT_URL
        hostname = url.split("@")[-1].split(":")[0].split("/")[0]
        try:
            port = int(url.split("@")[-1].split(":")[1].split("/")[0])
        except ValueError:
            port = None
        user = url.split("//")[1].split(":")[0]
        # TODO: password must be encrypted
        password = url.split(":")[2].split("@")[0]
        protocol = url.split(":")[0]
        return {
            "messenger": {
                "hostname": hostname,
                "port": port,
                "user": user,
                "password": password,
                "protocol": protocol,
            }
        }

