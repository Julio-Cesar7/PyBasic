def elim_elementos(lis, val_1, val_2):
    eliminar_elementos=0
    new_list = []
    for elemento in lista:
        if elemento != val_1 and elemento != val_2:
            new_list.append(elemento)
        else:
            eliminar_elementos +=1
    if eliminar_elementos < 2:
        print("No se eliminaron")
    return new_list

lista=['Mecánica Quántica II', 'Espectroscopía Mossbaüer', 'Física del Estado Sólido II', 'Óptica Física', 'E.Rayos X', 'Cristalografía']
lista.append("Física Computacional II")
lista.append("Electricidad y Magnetismo I")
lista.append("Electricidad y Magnetismo II")
lista.append("Electromagnetismo I y II")

eliminar_1='Mecánica Quántica II'
eliminar_2='Espectroscopía Mossbaüer'
result= elim_elementos(lista,eliminar_1,eliminar_2)
result.reverse()
for revers in result:
    print(revers)
