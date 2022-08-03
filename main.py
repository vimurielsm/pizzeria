from features.features import Features
from pedidos.pedidos import Pedidos
from menu import menu


if __name__ == '__main__':
    features = Features("./resources/features.json")
    pedidos = Pedidos("./resources/pedidos.json")
    continue_loop = True
    while continue_loop:
        continue_loop, opcion = menu.menu_principal(features)
        if opcion == '1':
            continue_loop, opcion = menu.menu_configuracion(features)
        if opcion == '2':
            continue_loop, opcion =menu.menu_agregar_pedido(features,pedidos)


