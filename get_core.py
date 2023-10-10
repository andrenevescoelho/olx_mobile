import requests,re,time
from bs4 import BeautifulSoup
import lxml
import mysql_connect

url = 'https://www.olx.com.br/celulares/estado-df/'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',}
response = requests.get(url, headers=headers)
code = response.text

padrao_url = r'https?://df.olx.com.br[^\s"]+'

urls_encontradas = re.findall(padrao_url, code)

if response.status_code == 200:
    for urls in urls_encontradas:
        print(urls)
        webpage = requests.get(urls, headers=headers)

        soup = BeautifulSoup(webpage.content, "html.parser")

        dom = lxml.etree.HTML(str(soup))

        try:
            padrao_item_id = r'"item_id":(\d+)'
            correspondencia_item_id  = re.search(padrao_item_id, webpage.text)
            item_id = correspondencia_item_id.group(1)
        except:
            item_id = 'nda'

        if not item_id == 'nda':    
            #obtendo o modelo
            try:
                Modelo = (dom.xpath('//*[@id="content"]/div[2]/div/div[2]/div[1]/div[29]/div/div/div[2]/div[3]/div[2]/span')[0].text)
            except:
                padrao_item_name = r'"item_name":"(.*?)"'
                correspondencia_item_name = re.search(padrao_item_name, webpage.text)
                Modelo = correspondencia_item_name.group(1)

            if Modelo == 'OUTROS':
                padrao_item_name = r'"item_name":"(.*?)"'
                correspondencia_item_name = re.search(padrao_item_name, webpage.text)
                Modelo = correspondencia_item_name.group(1)

            #obtendo a saude da bateria
            try:
                Saude_da_bateria = (dom.xpath('//*[@id="content"]/div[2]/div/div[2]/div[1]/div[29]/div/div/div[2]/div[7]/div[2]/span')[0].text)  
            except:
                Saude_da_bateria = 'nda'

            #obtendo a Marca
            try:
                Marca = (dom.xpath('//*[@id="content"]/div[2]/div/div[2]/div[1]/div[29]/div/div/div[2]/div[2]/div[2]/span')[0].text)
            except:
                Marca = 'nda'

            #obetendo a condicao
            try:
                Condicao = (dom.xpath('//*[@id="content"]/div[2]/div/div[2]/div[1]/div[29]/div/div/div[2]/div[4]/div[2]/span')[0].text)
            except:
                Condicao = 'nda'

            #obtendo a memoria interna
            try:
                Memoria_interna = (dom.xpath('//*[@id="content"]/div[2]/div/div[2]/div[1]/div[29]/div/div/div[2]/div[5]/div[2]/span')[0].text) 
            except:
                Memoria_interna = ''

            #obtendo a cor
            try: 
                cor = (dom.xpath('//*[@id="content"]/div[2]/div/div[2]/div[1]/div[29]/div/div/div[2]/div[6]/div[2]/span')[0].text)  
            except:
                cor = 'nda'

            try:
                padrao_price = r'"price":"(.*?)"'
                correspondencia_price  = re.search(padrao_price, webpage.text)
                valor = correspondencia_price.group(1)
            except:
                valor = (dom.xpath('//*[@id="content"]/div[2]/div/div[2]/div[1]/div[16]/div/div/div/div/div[1]/div/div[1]/span')[0].text)

            item_id_existe_na_base = mysql_connect.select('select item_id from data_mobile where item_id = '+item_id+'')

            if not item_id_existe_na_base:
                print('item_id '+ item_id)
                print('Modelo '+ Modelo)
                print('Marca ' + Marca)
                print('Condicao '+Condicao)
                print('Memoria_interna '+Memoria_interna)
                print('cor '+cor)
                print('Saude_da_bateria '+Saude_da_bateria)
                print('valor '+str(valor))
                insert = ('insert into data_mobile (item_id,Modelo,Marca,Condicao,Memoria_interna,cor,Saude_da_bateria,valor,url,last_update_date) values ("'+item_id+'","'+Modelo+'","'+Marca+'","'+Condicao+'","'+Memoria_interna+'","'+cor+'","'+Saude_da_bateria+'","'+valor+'","'+urls+'",now())')  
                print(insert)
                mysql_connect.insert(insert)        
                print('')
                
            else:
                print('ja cadastrado')
        
        
else:
    print(f'Request failed with status code: {response.status_code}')



