# -*- coding: utf-8 -*-
import logging
import urlparse

import requests

logger = logging.getLogger(__name__)


class API(object):

    API_URL = 'https://api.voximplant.com/platform_api/'

    def __init__(self, account, password):
        # TODO use api key and session
        if isinstance(account, int):
            acc_key = 'account_id'
        elif '@' in account:
            acc_key = 'account_email'
        else:
            acc_key = 'account_name'

        self._client = requests.Session()
        self._client.params = {acc_key: account,
                               'account_password': password}

    def log_errors(self, response):
        json = response.json()
        if 'error' in json:
            error = json['error']
            logger.error(u'%s %s', error['code'], error['msg'])

    def _api_request(self, METHOD, **kwargs):
        response = self._client.get(urlparse.urljoin(self.API_URL, METHOD),
                                    params=kwargs)
        self.log_errors(response)
        return response.json()

    def _get_user_key(self, user):
        if isinstance(user, int):
            userkey = 'user_id'
        else:
            userkey = 'user_name'
        return userkey

    def user_add(self, user_name, user_display_name, user_password,
                       parent_accounting=False,
                       two_factor_auth_required=False,
                       mobile_phone=None,
                       user_active=True,
                       user_custom_data=''):

        if len(user_name) < 6:
             raise Exception('User name too short')

        if len(user_password) < 7:
             raise Exception('User password too short')

        params = {'user_name': user_name,
                  'user_display_name': user_display_name,
                  'user_password': user_password
                 }
        if mobile_phone:
            params['mobile_phone'] = mobile_phone
        if user_custom_data:
            params['user_custom_data'] = user_custom_data

        return self._api_request('AddUser', **params)['user_id']

    def user_del(self, user):
        return self._api_request('DelUser', **{self._get_user_key(user): user})

    def user_bind(self, user, application):

        params = {self._get_user_key(user): user,
                  'application': application,
                  'bind': 1,
                 }
        return self._api_request('BindUser', **params)

    def user_unbind(self, user, application):
        params = {self._get_user_key(user): user,
                  'application': application,
                  'bind': 0,
                 }
        return self._api_request('BindUser', **params)
