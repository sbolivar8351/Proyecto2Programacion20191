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
    """
    >>> calcular_correspondencia('CATG','GTAC')
    100.0

    >>> calcular_correspondencia('CAT','GAA')
    66.66666666

    >>> calcular_correspondencia('TTT','GGG')
    0.0

    :param adn1:
    :param adn2:
    :return:
    """
    if generar_cadena_complementaria(adn1)==adn2:
        return 100.0

def corresponden(adn1, adn2):
    '''
    >>> corresponden('ATTT','TAAA')
    True
    >>> corresponden('TATATATAT','GAGAGAGA')
    False

    :param adn1:
    :param adn2:
    :return:
    '''
    return generar_cadena_complementaria(adn1) == adn2


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
    >>> es_base('KK')
    Traceback (most recent call last):
    ..
    ValueError: ('KK', 'No es base')
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
    >>> es_subcadena('GGATA','ATA')
    True

    >>> es_subcadena('TTTAAA','GCGC')
    False

    :param adn1:
    :param adn2:
    :return:
    """
    if es_cadena_valida(adn1) and es_cadena_valida(adn2):
        return adn2 in adn1
    raise ValueError(adn2, 'No es subcadena')

def reparar_dano(adn, base):
    """
    >>> reparar_dano('TA','CC')
    :param adn:
    :param base:
    :return:
    """

    if not corresponden(adn, base):
        base = generar_cadena_complementaria(adn)

    return "La base fue reparada " + base

def obtener_secciones(adn, n):
    """

    :param adn:
    :param n:
    :return:
    """
    pass


def obtener_complementos(lista_adn):
    pass


def unir_cadena(lista_adn):
    pass


def complementar_cadenas(lista_adn):
    pass

