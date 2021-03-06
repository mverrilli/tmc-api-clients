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
from swagger_client.api.tasks_api import TasksApi  # noqa: E501
from swagger_client.rest import ApiException


class TestTasksApi(unittest.TestCase):
    """TasksApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.tasks_api.TasksApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_configure_task_execution(self):
        """Test case for configure_task_execution

        Configure Task execution  # noqa: E501
        """
        pass

    def test_create_task(self):
        """Test case for create_task

        Create Task  # noqa: E501
        """
        pass

    def test_get_available_tasks(self):
        """Test case for get_available_tasks

        Get available Tasks  # noqa: E501
        """
        pass

    def test_get_task(self):
        """Test case for get_task

        Get Task by id  # noqa: E501
        """
        pass

    def test_get_task_configuration(self):
        """Test case for get_task_configuration

        Get Task configuration  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
