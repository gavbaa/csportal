# If things have stopped working:
#   Go to https://developer.intuit.com/app/developer/playground (the OAuth2 playground)


# from intuitlib.client import AuthClient
# from intuitlib.enums import Scopes
import base64
import requests

# Sandbox settings
g_client_id = 'ABhngJDN74XASgpApbxaMi0mkG3T2AXF2b42SNGFsi822QIrjb'
g_client_secret = 'aUfHVI7ak11TPmkDHzvhMI28IPS5bGdAgv3Ahy5N'
g_access_token = 'eyJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..Ro1qz3gmEer7fqHmh_hx-A.4je54FsIyamnIvEmlDENffpKTifrMlQ7JwJedhf-xUJ-GF_jh-rhQoYJZ2pXeN6y7lD-IsCE8tsWTS0SHKPvBebUUgcgcY_zyMAEsynmoYQ3Rg-XOkDl8U_rLv9e5wEfYhv39y5CfXtuOfweM7jtDH4hgx-RrFBL-EG-grOegM6JQIOKFYfV7u5LyK80kpX9XFq6wcWWza9xOTCYoUFD_hwGQW2THxIWGjcGKZ-CNa3c_B4KCyMPf941oPchfeJNSoyDRdaOLV_CpTSQGNT7cv3wks7-C_N7kmft-dglpQXui2NORb8aObzdFnu7nDP5EfBdg_aToq3diTgMD-HPJAXSA_uXPVkSv-AkweafXf2c5S_ZTGnuFHuIKStZv7NSmpJUPKTlDVjWY3_D3oVX3_vKjeBIj73kE6qp9Kl4x-1atCFu2EyfQMQO4XHjZhOIwbs7nJ80s0uqp4Q2TAWsyQ8QA8x1aKdqlwauz5gBa4Djq0lrTsqp3tTSI4GplIpkeEjEADYdT89IFgKdx4VpYauU42-whO5MVmzn9d-plorBQH8HuClmR8o0i5wjDOqz2Oj9B5lXd2nT5HfswIA8e-FqldV6JRfhrNWxZ1oPHlKU3Jamh17kZHOYGqMmkHXjq2HIpDhRGUV0Ywk-B29nPob1glQ4pcS1tAWCaD4ptvVZOTSc-tBllN_D_WkCH-I18q5e8HBQnj1eCgIguq8ZSy8xVyTLlipk5rQraZifkNxVBDSJNFQsYh8kFqVa1BiV.HOMrZiDRvQa-57Ct7EDhAg'
g_refresh_token = 'AB11605033209okVOooMnixoVUPhXxImwm1gBJpR90Zw2kILmk'
# Production Base URL: https://quickbooks.api.intuit.com
# Sandbox Base URL: https://sandbox-quickbooks.api.intuit.com
g_url_prefix = 'https://sandbox-quickbooks.api.intuit.com'

# qbo_env = 'sandbox' # 'sandbox' or 'production'

# //Instantiate client
# auth_client = AuthClient(
#     client_id,
#     client_secret,
#     'https://developer.intuit.com/v2/OAuth2Playground/RedirectUrl',
#     qbo_env,
# )

# // Prepare scopes
# scopes = [
#     Scopes.ACCOUNTING,
# ]

# // Get authorization URL
# auth_url = auth_client.get_authorization_url(scopes)


def get_access_token_from_auth_code(client_id, client_secret):
    """
     HOW TO GET THE ACCESS TOKEN:
     Go to https://developer.intuit.com/app/developer/playground (the OAuth2 playground)
     Do step 1
     Put the auth code here
     This generates the access token
     The auth code is only good ONCE!
    """
    auth_code = 'AB115963069662ZwxAN9VpPHiyFWZQtYJ5T3zQbxoTkmVNud0R'
    redirect_uri = 'https://developer.intuit.com/v2/OAuth2Playground/RedirectUrl'
    # refresh_token = 'AB11605031453TlkILCcrXnOmplWMWZjMwwM9KMapv92GZtFee'
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Basic ' + base64.b64encode((client_id + ':' + client_secret).encode('ascii')).decode('ascii')
    }

    auth_res = requests.post('https://oauth.platform.intuit.com/oauth2/v1/tokens/bearer',
                             data={
                                 'grant_type': 'authorization_code',
                                 'code': auth_code,
                                 'redirect_uri': redirect_uri
                             },
                             headers=headers)
    print(auth_res.text)


def get_access_token_from_refresh_token(client_id, client_secret, refresh_token):
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Basic ' + base64.b64encode((client_id + ':' + client_secret).encode('ascii')).decode('ascii')
    }

    refresh_res = requests.post('https://oauth.platform.intuit.com/oauth2/v1/tokens/bearer',
                                data={
                                    'grant_type': 'refresh_token',
                                    'refresh_token': refresh_token,
                                },
                                headers=headers)
    return refresh_res.json()


refresh_bits = get_access_token_from_refresh_token(g_client_id, g_client_secret, g_refresh_token)
g_access_token = refresh_bits['access_token']
print('access_token', g_access_token)


def qbo_api_test(url_prefix, access_token):
    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + access_token,
    }
    res = requests.get(
        url_prefix + '/v3/company/4620816365081117300/companyinfo/4620816365081117300',
        headers=headers,
    )
    print(res.text)


qbo_api_test(g_url_prefix, g_access_token)
