
def ricercaBinaria(lista: list[int], x:int) -> bool:
    result: bool = False
    indice_min: int = 0
    indice_max: int = len(lista) - 1
    while result != True and indice_min <= indice_max:
        indice_medio = (indice_min + indice_max) // 2 
        if lista[indice_medio] == x:
            result = True
        elif lista[indice_medio] > x:
            indice_max = indice_medio - 1
        else:
            indice_min = indice_medio + 1
    return result

