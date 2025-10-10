from .api_requestor import APIRequestor
from .options import RequestOptions
from .dto import RequestOAuthAssessToken, RequestOAuthRefreshToken


class OAuth:
    @staticmethod
    def get_access_token(client_id: str, client_secret: str, code: str):
        options = RequestOptions(oauth_authorization=True, max_network_retries=2)
        params = RequestOAuthAssessToken(grant_type='authorization_code',
                                         client_id=client_id,
                                         client_secret=client_secret,
                                         code=code,
                                         )
        return APIRequestor._global_instance().request(
            bitrix_address=None,
            params=params,
            options=options,
        )

    @staticmethod
    def get_refresh_token(client_id: str,
                          client_secret: str,
                          refresh_token: str,
                          ):
        options = RequestOptions(oauth_authorization=True, max_network_retries=2)
        params = RequestOAuthRefreshToken(grant_type='refresh_token',
                                          client_id=client_id,
                                          client_secret=client_secret,
                                          refresh_token=refresh_token,
                                          )
        return APIRequestor._global_instance().request(
            bitrix_address=None,
            params=params,
            options=options,
        )
