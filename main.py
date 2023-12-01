import unittest
def fibo(elementos):
    ''' Esta funcion calcula una serie de elemntos de la serie de fibonacci
    :arg
    recibe como paratro el numero de elementos de la serie
    :return
    retorna una lista con los elementos generados
    '''
    lista = [0, 1]
    numero = 2
    if elementos < 3:
        return lista
    while numero <= elementos:
        lista.append(lista[numero - 2] + lista[numero - 1])
        numero = numero + 1
    return lista
'''
if __name__ == "__main__":
    cantidad = int(input("Dame el numero de elentos de la serie "))
    lista = fibo(cantidad)
    print("la serie es ", lista)
'''
class PruebasFunciones(unittest.TestCase):
    '''Clase definida para la operacion de comprobacion de los elemtos de la serie fibonacci'''
    def test_fibo(self):
        '''Metodo que llama a la funcion para la verificacion del elemto 5
        Tenemos que tener en cuenta que las listas retornadas comienzan a contar en el elemnto 0
        '''
        serie = fibo(10)
        self.assertEqual(serie[4], 3)

if __name__ == '__main__':
    '''Cuerpo principal de ejecucion de nuestro programa'''
    unittest.main()
