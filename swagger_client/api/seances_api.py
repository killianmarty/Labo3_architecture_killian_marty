# coding: utf-8

"""
    API de Cours

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class SeancesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def cours_id_seances_id_seance_delete(self, id, id_seance, **kwargs):  # noqa: E501
        """Supprime une séance  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cours_id_seances_id_seance_delete(id, id_seance, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: (required)
        :param int id_seance: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.cours_id_seances_id_seance_delete_with_http_info(id, id_seance, **kwargs)  # noqa: E501
        else:
            (data) = self.cours_id_seances_id_seance_delete_with_http_info(id, id_seance, **kwargs)  # noqa: E501
            return data

    def cours_id_seances_id_seance_delete_with_http_info(self, id, id_seance, **kwargs):  # noqa: E501
        """Supprime une séance  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cours_id_seances_id_seance_delete_with_http_info(id, id_seance, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: (required)
        :param int id_seance: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'id_seance']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cours_id_seances_id_seance_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `cours_id_seances_id_seance_delete`")  # noqa: E501
        # verify the required parameter 'id_seance' is set
        if ('id_seance' not in params or
                params['id_seance'] is None):
            raise ValueError("Missing the required parameter `id_seance` when calling `cours_id_seances_id_seance_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'id_seance' in params:
            path_params['idSeance'] = params['id_seance']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/cours/{id}/seances/{idSeance}', 'DELETE',
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

    def cours_id_seances_id_seance_get(self, id, id_seance, **kwargs):  # noqa: E501
        """Retourne les infos sur la séance  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cours_id_seances_id_seance_get(id, id_seance, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: (required)
        :param int id_seance: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.cours_id_seances_id_seance_get_with_http_info(id, id_seance, **kwargs)  # noqa: E501
        else:
            (data) = self.cours_id_seances_id_seance_get_with_http_info(id, id_seance, **kwargs)  # noqa: E501
            return data

    def cours_id_seances_id_seance_get_with_http_info(self, id, id_seance, **kwargs):  # noqa: E501
        """Retourne les infos sur la séance  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cours_id_seances_id_seance_get_with_http_info(id, id_seance, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: (required)
        :param int id_seance: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'id_seance']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cours_id_seances_id_seance_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `cours_id_seances_id_seance_get`")  # noqa: E501
        # verify the required parameter 'id_seance' is set
        if ('id_seance' not in params or
                params['id_seance'] is None):
            raise ValueError("Missing the required parameter `id_seance` when calling `cours_id_seances_id_seance_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'id_seance' in params:
            path_params['idSeance'] = params['id_seance']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/cours/{id}/seances/{idSeance}', 'GET',
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

    def cours_id_seances_id_seance_post(self, id, id_seance, **kwargs):  # noqa: E501
        """Crée une nouvelle séance  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cours_id_seances_id_seance_post(id, id_seance, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: (required)
        :param int id_seance: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.cours_id_seances_id_seance_post_with_http_info(id, id_seance, **kwargs)  # noqa: E501
        else:
            (data) = self.cours_id_seances_id_seance_post_with_http_info(id, id_seance, **kwargs)  # noqa: E501
            return data

    def cours_id_seances_id_seance_post_with_http_info(self, id, id_seance, **kwargs):  # noqa: E501
        """Crée une nouvelle séance  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cours_id_seances_id_seance_post_with_http_info(id, id_seance, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: (required)
        :param int id_seance: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'id_seance']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cours_id_seances_id_seance_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `cours_id_seances_id_seance_post`")  # noqa: E501
        # verify the required parameter 'id_seance' is set
        if ('id_seance' not in params or
                params['id_seance'] is None):
            raise ValueError("Missing the required parameter `id_seance` when calling `cours_id_seances_id_seance_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'id_seance' in params:
            path_params['idSeance'] = params['id_seance']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/cours/{id}/seances/{idSeance}', 'POST',
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
