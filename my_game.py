from random import randint as rdn, seed as s

def check_machine_move(posiciones,machine):
    while True:
        if posiciones[machine]=="x" or posiciones[machine]=="o":  
            machine=rdn(0,8)
        else:
            break
    return machine

def check_human_move(posiciones,human):  
    while True:
        if human not in range(0,9):
            human=int(input("Dime una posición válida:"))
        elif posiciones[human]=="x" or posiciones[human]=="o": 
            human=int(input("Dime una posición libre: "))
        else:
            break
    return human
            
def machine_move(posiciones,move): 
    control=True
    while control:
        for i in range(len(posiciones)):
            if posiciones[i]=="x" or posiciones[i]=="o":
                pass 
            elif posiciones[i]==move:
                posiciones[i]="o"
                control=False
                return posiciones 
           
def human_move(human_move,posiciones): 
    for i in range(len(posiciones)):
        if posiciones[i]==human_move: 
            posiciones[i]="x"
    return posiciones

def board(to_print):
    print(
        """ 
                                                  ____________________ 
                                                 |      |      |      |
                                                 |  {}   |  {}   |  {}   |
                                                 |______|______|______|                                                  
                                                 |      |      |      |
                                                 |  {}   |  {}   |  {}   |
                                                 |______|______|______|                                                 
                                                 |      |      |      |
                                                 |  {}   |  {}   |  {}   |
                                                 |______|______|______| """.format(to_print[0],
         to_print[1],to_print[2],to_print[3],
         to_print[4],to_print[5],to_print[6],
         to_print[7],to_print[8]
         ))

def human_wins(posición):
    for x in posición:
        if posición[0]=="x" and  posición[1]=="x" and posición[2]=="x":
            print("Se acabó el juego gana el humano")
            return True               
        elif posición[3]=="x" and  posición[4]=="x" and posición[5]=="x" :
                print("Se acabó el juego gana el humano")
                return True    
        elif posición[6]=="x" and  posición[7]=="x" and posición[8]=="x" :
                print("Se acabó el juego gana el humano")
                return True   
        elif posición[0]=="x" and  posición[3]=="x" and posición[6]=="x" :
                print("Se acabó el juego gana el humano")
                return True   
        elif posición[1]=="x" and  posición[4]=="x" and posición[7]=="x" :
                print("Se acabó el juego gana el humano")
                return True   
        elif posición[2]=="x" and  posición[5]=="x" and posición[8]=="x" :
                print("Se acabó el juego gana el humano")
                return True   
        elif posición[0]=="x" and  posición[4]=="x" and posición[8]=="x" :
                print("Se acabó el juego gana el humano")
                return True  
        elif posición[2]=="x" and  posición[4]=="x" and posición[6]=="x":
                print("Se acabó el juego gana el humano")
                return True   
        else:
            return False    

def machine_wins(posición):
    for x in posición:
        if posición[0]=="o" and  posición[1]=="o" and posición[2]=="o":
            print("Se acabó el juego gana la máquina ")
            return True               
        elif posición[3]=="o" and  posición[4]=="o" and posición[5]=="o" :
                print("Se acabó el juego gana la máquina")
                return True    
        elif posición[6]=="o" and  posición[7]=="o" and posición[8]=="o" :
                print("Se acabó el juego gana la máquina")
                return True   
        elif posición[0]=="o" and  posición[3]=="o" and posición[6]=="o" :
                print("Se acabó el juego gana la máquina")
                return True   
        elif posición[1]=="o" and  posición[4]=="o" and posición[7]=="o" :
                print("Se acabó el juego gana la máquina")
                return True   
        elif posición[2]=="o" and  posición[5]=="o" and posición[8]=="o" :
                print("Se acabó el juego gana la máquina")
                return True   
        elif posición[0]=="o" and  posición[4]=="o" and posición[8]=="o" :
                print("Se acabó el juego gana la máquina")
                return True  
        elif posición[2]=="o" and  posición[4]=="o" and posición[6]=="o":
                print("Se acabó el juego gana la máquina")
                return True   
        else:
            return False

def run():
    posiciones=[x for x in range(0,9)]
    jugadas=[x for x in range(1,10)]
    board(posiciones)   
    for i in jugadas:
                if i % 2 != 0:
                    movimiento_humano=int(input("Dime una posición: "))
                    valido=check_human_move(posiciones,movimiento_humano)
                    human_move_to_print=human_move(valido,posiciones)
                    board(human_move_to_print)
                    if human_wins(human_move_to_print):
                        break
                else:
                    machine=rdn(0,8)
                    if machine == movimiento_humano:
                        machine=rdn(0,8)
                    movimiento_machine=check_machine_move(human_move_to_print,machine)
                    machine_move_to_print=machine_move(human_move_to_print , movimiento_machine)
                    board(machine_move_to_print)
                    if machine_wins(machine_move_to_print):
                        break

if __name__=="__main__":
    run()