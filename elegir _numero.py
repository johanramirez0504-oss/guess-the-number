import random
continuar=True
puntaje_total=0

while continuar:
    print("="*39)
    print("=JUEGO PARA ADIVINAR EL NÚMERO RANDOM=")
    print("="*39)
    mn=int(input("Elija un número mínimo: "))
    mx=int(input("Elija un número máximo: "))
    if mn >= mx:
        print("El número mínimo debe ser menor que el máximo.")
        continue
    int_max=int(input("Elija un número máximo de intentos: "))
    if int_max <= 0:
        print("Los intentos deben ser mayores que 0.")
        continue
    numero=random.randint(mn,mx)
    intentos=0
    volver=True
    gano=False
    while continuar and intentos<int_max and volver:
        intentos+=1

        print(f"Intento: {intentos}.")
        try:
           
            ran_num=int(input(f"Introduzca un número del {mn} al {mx}: "))
            if ran_num<mn or ran_num>mx:
                print(f"El número {ran_num} no está dentro del rango de {mn} a {mx}.")
                intentos-=1
                continue
            else:
                if ran_num==numero:
                    rango=mx-mn+1
                    puntaje_por_intentos=max(10,int(rango/int_max)*10)
                    intentos_sobrantes=int_max-intentos+1
                    puntaje_partida=puntaje_por_intentos*intentos_sobrantes
                    if intentos==1:
                        bonus_intento=50*int(rango/(int_max))
                        print(f"BONUS POR PRIMER INTENTO: {bonus_intento}")
                        puntaje_partida+=bonus_intento
                    if rango>=100:
                        puntaje_partida+=200
                        print("BONUS POR PARTIDA GRANDE: +200 pts.")
                    puntaje_total+=puntaje_partida
                    print(f"\nGANASTE. El número era {numero}. Lo lograste con {intentos} intentos.")
                    print(f"Puntaje de esta partida: {puntaje_partida} pts.")
                    print(f"Puntaje total acumulado: {puntaje_total} pts.")
                    gano=True
                    while continuar:
                        back=input("¿Volver a intentar con otros números? S/N: ").upper().strip()
                        if back=="S":
                            volver=False
                            break
                        elif back=="N":
                            print("Gracias por jugar. Hasta luego. _OuO/")
                            continuar=False
                            break
                        else:
                            print("Respuesta incorrecta.")
                elif ran_num<numero:
                    print(f"El número que tienes que adivinar es mayor que {ran_num}.")
                elif ran_num>numero:
                    print(f"El número que tienes que adivinar es menor que {ran_num}.")
                else:
                    print("No disponible.")
        except ValueError:
            print("Opción no disponible.")
            continue
    if volver==False:
        continue
    if not gano:
        print(f"\n¡Perdiste! Alcanzaste los intentos máximos. El número era {numero}.")
        print(f"Puntaje final de la sesión: {puntaje_total} pts.")
    break

