# -*- coding: utf-8 -*-

"""
    healthoslib.controllers.generics_controller

    This file was automatically generated by APIMATIC BETA v2.0 on 02/18/2017
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.o_auth_2 import OAuth2

class GenericsController(BaseController):

    """A Controller to access Endpoints in the healthoslib API."""
    

    def get_generic(self,
                    generic_id):
        """Does a GET request to /medicines/generics/{generic_id}.

        Get a generic by id

        Args:
            generic_id (string): TODO: type description here. Example: 

        Returns:
            mixed: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri.format(Configuration.host)
        _query_builder += '/medicines/generics/{generic_id}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'generic_id': generic_id
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        OAuth2.apply(_request)
        _context = self.execute_request(_request)        
        self.validate_response(_context)    

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def get_medicines_by_generic(self,
                                 page,
                                 size,
                                 exclusive,
                                 generic_id):
        """Does a GET request to /medicines/generics/{generic_id}/medicines.

        Get medicines containing the generic

        Args:
            page (int): TODO: type description here. Example: 
            size (int): TODO: type description here. Example: 
            exclusive (bool): TODO: type description here. Example: 
            generic_id (string): TODO: type description here. Example: 

        Returns:
            mixed: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri.format(Configuration.host)
        _query_builder += '/medicines/generics/{generic_id}/medicines'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'generic_id': generic_id
        })
        _query_url = APIHelper.clean_url(_query_builder)
        _query_parameters = {
            'page': page,
            'size': size,
            'exclusive': exclusive
        }

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers, query_parameters=_query_parameters)
        OAuth2.apply(_request)
        _context = self.execute_request(_request)        
        self.validate_response(_context)    

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def get_all_generics(self,
                         page,
                         size):
        """Does a GET request to /medicines/generics.

        All generics

        Args:
            page (int): TODO: type description here. Example: 
            size (int): TODO: type description here. Example: 

        Returns:
            mixed: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri.format(Configuration.host)
        _query_builder += '/medicines/generics'
        _query_url = APIHelper.clean_url(_query_builder)
        _query_parameters = {
            'page': page,
            'size': size
        }

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers, query_parameters=_query_parameters)
        OAuth2.apply(_request)
        _context = self.execute_request(_request)        
        self.validate_response(_context)    

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)

    def search_generics(self,
                        generic_query):
        """Does a GET request to /search/medicines/generics/{generic_query}.

        Search a generic by name

        Args:
            generic_query (string): TODO: type description here. Example: 

        Returns:
            mixed: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri.format(Configuration.host)
        _query_builder += '/search/medicines/generics/{generic_query}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'generic_query': generic_query
        })
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers)
        OAuth2.apply(_request)
        _context = self.execute_request(_request)        
        self.validate_response(_context)    

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body)
