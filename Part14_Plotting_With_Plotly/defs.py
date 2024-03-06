API_KEY = "ea2b655f011530d06c2c333174b28f8d-c0da41f98d38aa72ba8932e9f2d8d1b0"
ACCOUNT_ID = "101-001-26558478-001"
OANDA_URL = 'https://api-fxpractice.oanda.com/v3'

SECURE_HEADER = {
    'Authorization': f'Bearer {API_KEY}'
}

if __name__ == "__main__":
    print(f'{ACCOUNT_ID}')