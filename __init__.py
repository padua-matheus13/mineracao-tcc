from selenium import webdriver
import pymysql

# inicializando MySQL
db = pymysql.connect("localhost", "root", "endgame123", "base_tcc")


def postToDatabase(id, item):
    cursor = db.cursor()

    sql = "INSERT INTO medicamentos (id, nome_descricao) VALUES (%s, %s)"
    cursor.connection.ping()
    with cursor.connection as cursor:
        cursor.execute(sql, (int(id), item))
    db.close()


def main():
    chrome = webdriver.Chrome()
    chrome.get('https://interacoesmedicamentosas.com.br/interacoes.php')

    drugList = chrome.find_element_by_id("lista")
    items = drugList.find_elements_by_tag_name("li")

    id = 0

    for item in items:
        drug = item.text
        id += 1
        print(id, drug)
        postToDatabase(id, drug)


main()
