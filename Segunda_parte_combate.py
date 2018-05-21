pokemon_elegido = input("¿Contra que pokemon quieres conmbatir? (Agua / Fuego / Hoja):")

vida_pikachu = 100
vida_enemigo = 0
ataque_pokemon = 0
if pokemon_elegido == "Agua":
    vida_enemigo = 90
    nonbre_pokemon = "Agua"
    ataque_pokemon = 8

elif pokemon_elegido == "Fuego":
    vida_enemigo = 80
    nonbre_pokemon = "Fuego"
    ataque_pokemon = 7

elif pokemon_elegido == "Hoja":
    vida_enemigo = 100
    nonbre_pokemon = "Hoja"
    ataque_pokemon = 10



while vida_pikachu > 0 and vida_enemigo > 0:
    ataque_elegido = input("¿Que ataque vammos a usar? )Chispazo / Bola voltio ")

    if ataque_elegido == "Chispazo":
        vida_enemigo  -= 10
        print("Le quitas 10 de vida al enemigo")
    elif ataque_elegido == "Bola voltio":
        vida_enemigo -= 12
        print("Le quitas 12 de vida al enemigo")

    print("La vida del {} ahora es de {}".format(nonbre_pokemon ,vida_enemigo))

    print("{} te hace un ataque de {} de daño".format(nonbre_pokemon, ataque_pokemon))
    vida_pikachu -= ataque_pokemon

    print("La vida de Pikachu es de {}".format(vida_pikachu))

if vida_enemigo <= 0:
    print("¡Pikachu a ganado!")
if vida_pikachu <= 0:
    print("¡Has perdido!")

print("El combate ha termiando")