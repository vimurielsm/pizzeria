import json


def get_clave_valor_text(diccionario):
    text = ''
    for clave, valor in diccionario.items():
        text ='{0} {1} --> {2}\n'.format(text,clave, valor)
    return text


def get_json(json_path):
    with open(json_path, 'r') as json_file:
        return json.load(json_file)


def update_json(json_path, json_data):
    with open(json_path, 'w') as json_file:
        json.dump(json_data, json_file)