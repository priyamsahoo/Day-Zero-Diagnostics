# -*- coding: utf-8 -*-

"""
    healthoslib.controllers.diseases_controller

    This file was automatically generated by APIMATIC BETA v2.0 on 02/18/2017
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.o_auth_2 import OAuth2

class DiseasesController(BaseController):

    """A Controller to access Endpoints in the healthoslib API."""
    

    def get_disease(self,
                    disease_id):
        """Does a GET request to /diseases/{disease_id}.

        TODO: Add Description

        Args:
            disease_id (string): TODO: type description here. Example: 

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
        _query_builder += '/diseases/{disease_id}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'disease_id': disease_id
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

    def get_all_diseases(self,
                         page,
                         size):
        """Does a GET request to /diseases.

        TODO: Add Description

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
        _query_builder += '/diseases'
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

    def search_diseases(self,
                        disease_query):
        """Does a GET request to /search/diseases/{disease_query}.

        TODO: Add Description

        Args:
            disease_query (string): TODO: type description here. Example: 

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
        _query_builder += '/search/diseases/{disease_query}'
        _query_builder = APIHelper.append_url_with_template_parameters(_query_builder, { 
            'disease_query': disease_query
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
