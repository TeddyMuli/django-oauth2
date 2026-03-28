import requests

client_id = 'k7s513gwNdNA8n7pMaBv7VS4cleig5i9WmNH39Hv'
client_secret = '7Az44wy5M9QT5lYYgFtQruw5kJn6XvuTiOvEAfBy3FRopMpXM0aHgdyBK3kvSZuDclT75IAj6DbHqensjJ6EVle25V6koVRoYrIWhGREA5zbD1uh0EEn3d6Y2tztBDnv'

# Token endpoint
token_url = 'http://127.0.0.1:8000/o/token/'

data = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret,
    'scope': 'read',
}

response = requests.post(token_url, data=data)
if response.status_code != 200:
    print("Token request failed:", response.status_code)
    print("Response text:", response.text)
    exit(1)

try:
    token = response.json().get('access_token')
except Exception as e:
    print("Failed to parse token response as JSON:", e)
    print("Response text:", response.text)
    exit(1)

headers = {'Authorization': f'Bearer {token}'}
api_url = 'http://127.0.0.1:8000/api/rooms/'
api_response = requests.get(api_url, headers=headers)

try:
    print(api_response.json())
except Exception as e:
    print("Failed to parse API response as JSON:", e)
    print("Response text:", api_response.text)
