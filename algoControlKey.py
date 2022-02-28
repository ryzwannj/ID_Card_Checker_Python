def algo_controlKey(code : str):
    resultat = 0
    facteur = (7, 3, 1)

    for (position, car) in enumerate(code):
        if car == "<":
            valeur = 0
        elif "0" <= car <= "9":
            valeur = int(car)
        elif "A" <= car <= "Z":
            valeur = ord(car)-55
        else:
            print("Caractère hors bornes")
            break
            
        resultat += valeur * facteur[position % 3]
        final_resultat = str(resultat % 10)
    return final_resultat