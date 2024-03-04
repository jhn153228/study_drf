import requests
'''강의와 버전이 달라서 어쩌다보니 JWT 대신 Bearer 토큰을 사용...?

 장고 4.0 이상부터 JWT대신 Bearer토큰 사용을 권장한다고 함
 rest_framework_simplejwt
'''

Bearer_TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNj' \
               'ZXNzIiwiZXhwIjoxNzA5NDQxMTQ1LCJpYXQiOjE3MDk0NDA4NDUsImp0aSI6I' \
               'jZiNDU3ZTRjM2IyYTQ4ZjFhYTczZmYyYjQ1MjkyNTVlIiwidXNlcl9pZCI6Mn0' \
               '.Pnds8DSY460pqMdAq6P3A14E86UDhMBK3YLOs7oWZrE'

headers = {
    'Authorization': f'Bearer {Bearer_TOKEN}'
}

res = requests.get('http://localhost:8000/post/1/', headers= headers)
print(res.json())