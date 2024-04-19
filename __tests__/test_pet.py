#1- bibliotecas
import json          # leitor e escritor de arquivos json
import pytest        # motor/ framework de teste de unidade
import requests      # framework de teste de API



#2- classe (opcional no python, em muitos casos)

#2.1 - atributos ou variáveis
# consulta e resultado esperado
pet_id = 114564801         # código do animal
pet_name = "Snoopy"        # nome do animal
pet_category_id = 1        # código da categoria do animal
pet_category_name = "dog"  # título da categoria
pet_tag_id = 1             # código do rótulo
pet_tag_name = "vacinado"  # titulo do rótulo


# informações em comum(global)
url = "https://petstore.swagger.io/v2/pet"            # endereço
headers = { "Content-Type": "application/json" }        # formato dos dados trafegados

#2.2- funções/método

def test_post_pet():
    # configura
    # dados de entrada estão no arquivo json
    pet = open("./fixtures/json/pet1.json")    # abre o arquivo json
    data = json.loads(pet.read())             # ler o conteúdo e carregar como json em uma variável data
    # dados de saída / resultado esperado estão nos atributos acima das funções
    
    #executa
    response = requests.post(           # executa o método post com as informações a seguir
        url = url,                      # endereço
        headers = headers,              # cabeçalho / informações extras da mensagem
        data = json.dumps(data),        # a mensagem = json
        timeout = 5                     # tempo limite da transmissão, em segundos
    )
    
    #valida
    response_body = response.json()      # cria uma variável e carrega a resposta em formato json
    
    assert response.status_code == 200
    assert response_body["id"] == pet_id
    assert response_body["name"] == pet_name
    assert response_body["category"]["name"] == pet_category_name
    assert response_body["tags"][0]["name"] == pet_tag_name
    
def test_get_pet():
    # Configura
    # Dados de Entrada e Saída/Resultado Esperado estão na seção de atributos antes das funções
    
    # Executa
    response = requests.get(
        url = f"{url}/{pet_id}",  # chama o endereço do get/consulta passando o código do animal 
        headers = headers
        # não tem corpo de mensagem / body
    )
    
    # Valida
    response_body = response.json()
    
    assert response.status_code == 200
    assert response_body["name"] == pet_name
    assert response_body["category"]["id"] == pet_category_id
    assert response_body["tags"][0]["id"] == pet_tag_id
    assert response_body["status"] == "available"
    
    
def test_put_pet():
    # Configura
    # Dados de entrada vem de um arquivo json
    pet = open("./fixtures/json/pet2.json")
    data = json.loads(pet.read())
    # Dados de Saída/resultado esperado vem dos atributos descritos antes das funções
    
    # Executa
    response = requests.put(
        url = url,
        headers = headers,
        data = json.dumps(data),
        timeout = 5
    )
    
    # Valida
    response_body = response.json()
    
    assert response.status_code == 200
    assert response_body["id"] == pet_id
    assert response_body["name"] == pet_name
    assert response_body["category"]["name"] == pet_category_name
    assert response_body["tags"][0]["name"] == pet_tag_name
    assert response_body["tags"][0]["id"] == pet_tag_id
    assert response_body["status"] == "sold"
    
def test_delete_pet():
    # Configura
    # Dados de entrada e saída virão dos atributos
    # Executa
    response = requests.delete(
        url = f"{url}/{pet_id}",
        headers = headers
    )
    
    # Valida
    response_body = response.json()
    
    assert response.status_code == 200   #se o pedido veio
    assert response_body["code"] == 200  #se o pedido veio certo
    assert response_body["type"] == "unknown"
    assert response_body["message"] == str(pet_id)
    
    