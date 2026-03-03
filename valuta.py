import requests
import os
from dotenv import load_dotenv, set_key
import sys

ENV_FILE = '.env'

if '--key' in sys.argv:
    key_index = sys.argv.index('--key') + 1
    api_key = sys.argv[key_index]
    set_key(ENV_FILE, 'API_KEY', api_key)
    print('API key saved!')

load_dotenv()
key = os.getenv('API_KEY')

if not key:
    print('Ingen api nøgle fundet. Kør: python3 valuta.py --key DIN_API_NØGLE')
    sys.exit(1)


print('Indtast første valuta')
firstValuta = input()

print('Indtast anden valuta')
secondValuta = input()

print('Indtast hvor meget du vil konvertere')
amount = input()


URL = f'https://v6.exchangerate-api.com/v6/{key}/pair/{firstValuta}/{secondValuta}/{amount}'

res = requests.get(URL)

data = res.json()




if str(data['result']) == 'error':
    if str(data['error-type']) == 'invalid-key':
        print('Forkert api nøgle')
        print('Kør programmet igen med python3 valuta.py --key DEN_RIGTIGE_NØGLE')
        sys.exit(1)
    else:
        print('Der skete en fejl')
        print('Sikre dig at du indtaster rigtige valutaer')
        print('Fx: euro = eur og dollars = usd')
        sys.exit()

print('Konverterings rate: ' + str(data['conversion_rate']))
print('Din konvertering bliver: ' + str(data['conversion_result']) + ' ' + str(data['target_code']))


