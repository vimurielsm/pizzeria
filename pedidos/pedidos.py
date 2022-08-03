import json
from utils import utils
class Pedidos():
    def __init__(self, path):
        pedidos_json = utils.get_json(path)
        self.path = path
        if len(pedidos_json) == 0:
            {
                "pedidos": [ ]
            }

        else:
            self.pedidos_file = pedidos_json

    def agregar_pedido(self, pedido):
        self.pedidos_file.get('pedidos').append(pedido)

    def nuevo_pedido(self):
        codigo =len(self.pedidos_file.get('pedidos'))+1
        nuevo_pedido = {'codigo':codigo,'items':[]}
        return nuevo_pedido

    def guardar_pedidos(self):
        utils.update_json(self.path, self.pedidos_file)