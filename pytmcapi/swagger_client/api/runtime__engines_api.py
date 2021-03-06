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


class RuntimeEnginesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_remote_engine(self, body, **kwargs):  # noqa: E501
        """Create new Remote Engine  # noqa: E501

        Create new Remote Engine  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_remote_engine(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EngineRequest body: remote engine (required)
        :return: Engine
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_remote_engine_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_remote_engine_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_remote_engine_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create new Remote Engine  # noqa: E501

        Create new Remote Engine  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_remote_engine_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EngineRequest body: remote engine (required)
        :return: Engine
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
                    " to method create_remote_engine" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_remote_engine`")  # noqa: E501

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

        # Authentication setting
        auth_settings = ['Access Token', 'Basic Authentication']  # noqa: E501

        return self.api_client.call_api(
            '/runtimes/remote-engines', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Engine',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_remote_engine(self, id, **kwargs):  # noqa: E501
        """Delete Remote Engine by id  # noqa: E501

        Delete Remote Engine by id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_remote_engine(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: remote engine id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_remote_engine_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_remote_engine_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def delete_remote_engine_with_http_info(self, id, **kwargs):  # noqa: E501
        """Delete Remote Engine by id  # noqa: E501

        Delete Remote Engine by id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_remote_engine_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: remote engine id (required)
        :return: None
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
                    " to method delete_remote_engine" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_remote_engine`")  # noqa: E501

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
            '/runtimes/remote-engines/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_remote_engine(self, id, **kwargs):  # noqa: E501
        """Get Remote Engine by id  # noqa: E501

        Get Remote Engine by id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_remote_engine(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: remote engine id (required)
        :return: Engine
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_remote_engine_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_remote_engine_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_remote_engine_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get Remote Engine by id  # noqa: E501

        Get Remote Engine by id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_remote_engine_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: remote engine id (required)
        :return: Engine
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
                    " to method get_remote_engine" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_remote_engine`")  # noqa: E501

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
            '/runtimes/remote-engines/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Engine',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_remote_engines(self, **kwargs):  # noqa: E501
        """Get all (available) Remote Engines  # noqa: E501

        Get all (available) Remote Engines  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_remote_engines(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str query: search query (FIQL format), e.g. \"environmentId==5cb47ca4b1b5247f6006529e\",\"status==PAIRED\"
        :return: Engine
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_remote_engines_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_remote_engines_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_remote_engines_with_http_info(self, **kwargs):  # noqa: E501
        """Get all (available) Remote Engines  # noqa: E501

        Get all (available) Remote Engines  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_remote_engines_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str query: search query (FIQL format), e.g. \"environmentId==5cb47ca4b1b5247f6006529e\",\"status==PAIRED\"
        :return: Engine
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_remote_engines" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'query' in params:
            query_params.append(('query', params['query']))  # noqa: E501

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
            '/runtimes/remote-engines', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Engine',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def unpair_remote_engine(self, id, **kwargs):  # noqa: E501
        """Unpair Remote Engine  # noqa: E501

        Unpair Remote Engine  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.unpair_remote_engine(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: remote engine id (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.unpair_remote_engine_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.unpair_remote_engine_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def unpair_remote_engine_with_http_info(self, id, **kwargs):  # noqa: E501
        """Unpair Remote Engine  # noqa: E501

        Unpair Remote Engine  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.unpair_remote_engine_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: remote engine id (required)
        :return: str
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
                    " to method unpair_remote_engine" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `unpair_remote_engine`")  # noqa: E501

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
            ['text/plain'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Access Token', 'Basic Authentication']  # noqa: E501

        return self.api_client.call_api(
            '/runtimes/remote-engines/{id}/pairing', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
