import json
from utils import utils

class Features():
    def __init__(self, path):
        features_json = utils.get_json(path)
        self.path = path
        if len(features_json) == 0:
            {
                "ingredientes": {},
                "masas": {},
                "salsas": {},
                "tamanio": {},
                "bordes": {}
            }
        else:
            self.features_file = features_json

    def get_items_in_tipo(self,tipo):
        return self.features_file.get(tipo.capitalize())

    def get_features_tipos(self):
        return self.features_file.keys()

    def get_item_value_features_tipos(self, tipo, item):
        return self.features_file.get(tipo.capitalize()).get(item.capitalize()).capitalize()

    def get_feartures(self):
       return self.features_file

    def listar_items(self,tipo):
        return utils.get_clave_valor_text(self.features_file.get(tipo.capitalize()))

    def mostrar_configuracion(self,**kargs):
        return utils.get_clave_valor_text(self.features_file)

    def agregar_item(self, **kargs):
        self.features_file.get(kargs.get('tipo'))[len(self.features_file.get(kargs.get('tipo'))) + 1] = kargs.get('item').capitalize()
        return self.features_file.get(kargs.get('tipo'))


    def remover_item(self, tipo, item):
        if self.features_file.get(tipo.capitalize()) is None:
            print(f"{tipo} no es una tipo de elemento configurable")
            return None
        elif self.features_file.get(tipo.capitalize()).get(item) is None:
            print(f"{item} no es una item de tipo {tipo} configurable")
            return None
        else:
            new_features_items ={}
            n = 1
            for clave, valor in self.features_file.get(tipo).items():
                if clave != item:
                    new_features_items[str(n)] = valor
                    print(clave,valor,n)
                    print(new_features_items)
                    n=n+1
            self.features_file.pop(tipo)
            self.features_file[tipo] = new_features_items
            print('---------------',self.features_file.get(tipo))
            return self.features_file.get(tipo)

    def guardar_features(self):
        utils.update_json(self.path, self.features_file)

    def operar(self,funcion, **kargs):
        return self[funcion](**kargs)


    def existe_tipo(self, tipo):
        if self.features_file.get(tipo.capitalize()) is None:
            return False
        return True

    def existe_item(self, tipo, item):
        if self.features_file.get(tipo.capitalize()).get(item.capitalize()) is None:
            return False
        return True

    operaciones = {
            "1": mostrar_configuracion,
            "2": agregar_item,
            "3": remover_item
    }




