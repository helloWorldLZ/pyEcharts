import urllib.request as urllib2
from aip import AipNlp

APP_ID = '17276757'
API_KEY = client_id = 'VQOiCzu8sAdz8lyd4XGRVqGA'
SECRET_KEY = client_secret = 'cL44fG7S4M4hWwmuGSYXWceNcFCBTRMW'
access_token = '24.9df6ca84cea15e7c20193b5d495546d1.2592000.1571454361.282335-17276757'


def getNlpClient():
    return AipNlp(APP_ID, API_KEY, SECRET_KEY)


def getAccessToken():
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' \
           + client_id + '&client_secret=' + client_secret
    request = urllib2.Request(host)
    request.add_header('Content-Type', 'application/json; charset=UTF-8')
    response = urllib2.urlopen(request)
    content = response.read()
    if content:
        print(content)


# getAccessToken()
