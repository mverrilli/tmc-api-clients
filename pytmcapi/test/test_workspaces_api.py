# coding: utf-8

"""
    Talend Management Console Public API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.workspaces_api import WorkspacesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestWorkspacesApi(unittest.TestCase):
    """WorkspacesApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.workspaces_api.WorkspacesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_workspaces(self):
        """Test case for get_workspaces

        Get available Workspaces  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
