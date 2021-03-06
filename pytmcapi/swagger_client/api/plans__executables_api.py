# coding: utf-8

"""
    Talend Management Console Public API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class PlansExecutablesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def configure_plan_execution(self, id, **kwargs):  # noqa: E501
        """Configure Plan execution  # noqa: E501

        Configure Plan execution  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.configure_plan_execution(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Plan id (required)
        :param RunConfig body: RunConfig
        :return: RunConfig
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.configure_plan_execution_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.configure_plan_execution_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def configure_plan_execution_with_http_info(self, id, **kwargs):  # noqa: E501
        """Configure Plan execution  # noqa: E501

        Configure Plan execution  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.configure_plan_execution_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Plan id (required)
        :param RunConfig body: RunConfig
        :return: RunConfig
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method configure_plan_execution" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `configure_plan_execution`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Access Token', 'Basic Authentication']  # noqa: E501

        return self.api_client.call_api(
            '/executables/plans/{id}/run-config', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RunConfig',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_plan(self, body, **kwargs):  # noqa: E501
        """Create Plan  # noqa: E501

        Create Plan  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_plan(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PlanRequest body: Execution plan (required)
        :return: Plan
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_plan_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_plan_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_plan_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create Plan  # noqa: E501

        Create Plan  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_plan_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PlanRequest body: Execution plan (required)
        :return: Plan
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_plan" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_plan`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Access Token', 'Basic Authentication']  # noqa: E501

        return self.api_client.call_api(
            '/executables/plans', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Plan',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_available_plans(self, **kwargs):  # noqa: E501
        """Get available Plans  # noqa: E501

        Get available Plans  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_available_plans(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: plan name filter
        :param str environment_id: environment id
        :param str workspace_id: workspace id
        :param int limit: limit
        :param int offset: offset
        :return: Page
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_available_plans_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_available_plans_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_available_plans_with_http_info(self, **kwargs):  # noqa: E501
        """Get available Plans  # noqa: E501

        Get available Plans  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_available_plans_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: plan name filter
        :param str environment_id: environment id
        :param str workspace_id: workspace id
        :param int limit: limit
        :param int offset: offset
        :return: Page
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'environment_id', 'workspace_id', 'limit', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_available_plans" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'environment_id' in params:
            query_params.append(('environmentId', params['environment_id']))  # noqa: E501
        if 'workspace_id' in params:
            query_params.append(('workspaceId', params['workspace_id']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Access Token', 'Basic Authentication']  # noqa: E501

        return self.api_client.call_api(
            '/executables/plans', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Page',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_executable_details(self, id, **kwargs):  # noqa: E501
        """Get Plan details  # noqa: E501

        Get Plan details  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_executable_details(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: executable ID (required)
        :return: PlanExecutableDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_executable_details_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_executable_details_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_executable_details_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get Plan details  # noqa: E501

        Get Plan details  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_executable_details_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: executable ID (required)
        :return: PlanExecutableDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_executable_details" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_executable_details`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Access Token', 'Basic Authentication']  # noqa: E501

        return self.api_client.call_api(
            '/executables/plans/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PlanExecutableDetails',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_plan_configuration(self, id, **kwargs):  # noqa: E501
        """Get Plan configuration  # noqa: E501

        Get Plan configuration  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_plan_configuration(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: plan id (required)
        :return: RunConfig
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_plan_configuration_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_plan_configuration_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_plan_configuration_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get Plan configuration  # noqa: E501

        Get Plan configuration  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_plan_configuration_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: plan id (required)
        :return: RunConfig
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_plan_configuration" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_plan_configuration`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Access Token', 'Basic Authentication']  # noqa: E501

        return self.api_client.call_api(
            '/executables/plans/{id}/run-config', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RunConfig',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
