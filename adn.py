def obtener_complemento(base):
    """
     >>> obtener_complemento('G')
     'C'

    >>> obtener_complemento('T')
    'A'

    >>> obtener_complemento('K')
    'NO ES UNA BASE VALIDA'

    :param base:
    :return:
    """
    # retorna caracter
    if base =='C':
        return 'G'
    elif base =='G':
        return 'C'
    if base == 'T':
        return 'A'
    elif base == 'A':
        return 'T'
    if base!= 'A' or base != 'G' or base!='C'or base!='T':
        return "   NO ES UNA BASE VALIDA"


def generar_cadena_complementaria(adn):
    """
    >>> generar_cadena_complementaria('ATT')
    'TAA'

    >>> generar_cadena_complementaria('CCC')
    'GGG'

    >>> generar_cadena_complementaria('GGT')
    'CCA'

    :param adn:
    :return:
    """
    complement = ""
    for base in adn:
        complement += obtener_complemento(base)
    return complement



def calcular_correspondencia(adn1, adn2):
    # retorna num
    pass


def corresponden(adn1, adn2):
    # retorna Bool
    pass


def es_cadena_valida(adn):
    """
    >>> es_cadena_valida('CTTA')
    True

    >>> es_cadena_valida('CHAO')
    False

    >>> es_cadena_valida('TAC')
    True

    :param adn:
    :return:
    """
    for base in adn:
        if not es_base(base):
            return False
    return True


def es_base(caracter):
    """
    >>> es_base('K')
    False

    >>> es_base('G')
    True

    >>> es_base('C')
    True

    :param caracter:
    :return:
    """
    if len(caracter) != 1:
        raise ValueError(caracter, 'No es base')
    return caracter in 'CGTA'


def es_subcadena(adn1, adn2):
    """

    :param adn1:
    :param adn2:
    :return:
    """



def reparar_dano(adn, base):
    pass


def obtener_secciones(adn, n):
    pass


def obtener_complementos(lista_adn):
    pass


def unir_cadena(lista_adn):
    pass


def complementar_cadenas(lista_adn):
    pass

