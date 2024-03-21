import requests
import time

#url de exemplo
url = "https://camo.githubusercontent.com/1817b38e81e8ac757188d0c9fc095551af4c33276905ff3aa931eb85a61aec2c/68747470733a2f2f70726f66696c652d636f756e7465722e676c697463682e6d652f7b477265636f50657265737d2f636f756e742e737667"
num_atualizacoes = 10000

for i in range(num_atualizacoes):
    r = requests.get(url)
    if r.status_code == 200:
        print(f'Página atualizada com sucesso - {i+1}')
    else:
        print('Falha ao acessar a página:', r.status_code)
    time.sleep(0.01)
''
print('Obrigado por usar o bot do Tavera')
