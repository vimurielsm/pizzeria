from features.features import Features
from pedidos.pedidos import Pedidos
from utils import utils


menu_inicial = {
    "1": "Configuración",
    "2": "Agregar pedido",
    "3": "Cancelar"
}

menu_conf = {
    "1": "Mostrar configuracion",
    "2": "Agregar item configuracion",
    "3": "Remover item configuracion",
    "4": "Cancelar"
}



def menu_principal(features: Features):
    menu_text = utils.get_clave_valor_text(menu_inicial)
    opc = input('\n---- Menu principal. Digite la opción deseada ---- \n{0} -->'.format(menu_text))
    if opc in ['1', '2' ]:
    #if opc == '1' or opc == '2' or opc == '3':
        return  True, opc
    else: return False, opc



def menu_configuracion(features: Features):
    menu_text = utils.get_clave_valor_text(menu_conf)
    opc = input('\n---- Configuracion. Digite la opción deseada ---- \n{0} -->'.format(menu_text))
    if opc == '1':
        configurar[menu_conf.get(opc)](features)
        return True, 0
    elif opc in ['2','3']:
        tipo = input('\nSeleccione tipo:\n{0} -->'.format(features.get_features_tipos()))
        if  tipo =='':
            print("No se ingreso un tipo para configurar")
            return True, 0
        if not features.existe_tipo(tipo):
            print(f"El tipo {tipo} que ingreso, no es una tipo de elemento configurable")
            return True, 0
        if opc == '2':
            item = input(f'\nItems en {tipo.capitalize()}:\n{features.listar_items(tipo)} '
                         f'Ingrese nombre del nuevo item--> ')
        else:
            item = input(f'\nItems en {tipo.capitalize()}:\n{features.listar_items(tipo)} '
                         f'Ingrese número del {tipo} que desea remover--> ')
            if not features.existe_item(tipo, item):
                print(f"El item numero {item} no existe en la lista de {tipo}")
                return True, 0
        if item is None:
            print(f"No se ingreso un item de tipo {tipo} para configurar")
            return True, 0
        configurar[menu_conf.get(opc)](features, tipo=tipo.capitalize(), item=item.capitalize())
        return True, 0
    else:
        print(f'{opc} no es una opcion de configurarion')
        return True, opc


def mostrar_configuracion(feature: Features, **kargs):
     print('\n---- Configuracion ----\n',feature.mostrar_configuracion())


def agregar_item_configuracion(feature: Features, **kargs):
    if confirmar('agregar', 'tipo = {0}, item = {1}'.format(kargs.get('tipo'),kargs.get('item'))) == 'Y':
        feature.agregar_item(tipo=kargs.get('tipo'), item=kargs.get('item'))
        feature.guardar_features()


def remover_item_configuracion(feature: Features, **kargs):
    if confirmar('eliminar', 'tipo = {0}, item = {1}'.format(kargs.get('tipo'), kargs.get('item'))) == 'Y':
        feature.remover_item(tipo=kargs.get('tipo'), item=kargs.get('item'))
        feature.guardar_features()


def menu_agregar_pedido(feature: Features, pedidos: Pedidos):
    cantidad_pizzas = input('Cuantas pizzas desea ordenar: ')
    if cantidad_pizzas == '' or cantidad_pizzas == '0':
        print('No se digito una cantidad de pizzas. (Para cancelar digite 0)')
        return True, 0
    else:
        pedido = pedidos.nuevo_pedido()
        for p in range(0,int(cantidad_pizzas)):
            pizza = menu_crear_pizza(feature)
            if pizza is None:
                return True, 0
            pedido.get('items').append(pizza)
        pedidos.agregar_pedido(pedido)
        pedidos.guardar_pedidos()
        print(pedido)
    return True, 0


def ingresar_campo(campo, complemento='', mensaje = 'Ingrese el valor para'):
    dato = input(f'{mensaje} {campo} {complemento}')
    if dato =='':
        print(f'No se ingreso un valor para el campo {campo}')
        return None
    return dato


def menu_crear_pizza(feature: Features, **kargs):
    masa = ingresar_campo(campo='masa',complemento=f'\n{feature.listar_items("Masas")}')
    if masa is None: return None

    borde = ingresar_campo(campo='borde', complemento=f'\n{feature.listar_items("Bordes")}')
    if borde is None:  return None

    tamanio = ingresar_campo(campo='tamanio', complemento=f'\n{feature.listar_items("Tamanio")}')
    if tamanio is None:  return None

    ingredientes = ingresar_campo(campo='ingredientes', complemento=f'. (Digite el número de cada ingrediente'
                                   f' separado por comas). \n{feature.listar_items("Ingredientes")}')
    if ingredientes is None:  return None
    ing_no_validos = [i for i in ingredientes.split(',') if
                      i not in list(feature.get_items_in_tipo("Ingredientes").keys())]
    if len(ing_no_validos) > 0:
        print(f'\nLos ingredientes {ing_no_validos} no existen en la lista \n{feature.listar_items("Ingredientes")}')
        return None
    else:
        ing = []
        for i in ingredientes.split(','):
            ing.append(feature.get_item_value_features_tipos("Ingredientes", i))
        ingredientes = ing

    salsas = ingresar_campo(campo='salsas', complemento=f'. (Digite el número de cada salsa'
                                  f' separado por comas). \n{feature.listar_items("Salsas")}')
    if salsas is None:  return None
    salsas_no_validas = [i for i in salsas.split(',') if i not in list(feature.get_items_in_tipo("Salsas").keys())]
    if len(salsas_no_validas) > 0:
        print(f'\nLas salsas {salsas_no_validas} no existen en la lista \n{feature.listar_items("Salsas")}')
        return None
    else:
        salsas_2 =[]
        for s in salsas.split(','):
            salsas_2.append(feature.get_item_value_features_tipos("Salsas", s))
        salsas = salsas_2


    preparacion = ingresar_campo(campo='preparacion', complemento=f'\n{feature.listar_items("Preparacion")}')
    if preparacion is None:  return None


    pizza = {'masa': feature.get_item_value_features_tipos('Masas', masa),
             'borde': feature.get_item_value_features_tipos('Bordes', borde),
             'tamanio': feature.get_item_value_features_tipos('Tamanio', tamanio),
             'ingredients': ingredientes,
             'salsas': salsas,
             'preparacion': feature.get_item_value_features_tipos('Preparacion', preparacion)
             }
    return pizza


def confirmar(operacion, datos):
    return input('Confirma {}: {} Y/N?'.format(operacion, datos))


configurar = {
    "Mostrar configuracion": mostrar_configuracion,
    "Agregar item configuracion": agregar_item_configuracion,
    "Remover item configuracion": remover_item_configuracion
}

