#Esse código foi feito em uma coding session em conjunto com Caio (https://github.com/CaioPaula) e Gabi (https://github.com/Gabrielle-Cartaxo)
from mod import *

bot = Robozinho()

loader = yaspin() 

def choicer():
    options = [
        inquirer.List(name="escolha" ,message="Escolha o comando", choices=["conectar", "desconectar", "mover", "home", "mostrar posição atual", "toogle tool", "sair"])
    ]

    prompt = inquirer.prompt(options) #variavel que recebe os prompts das escolhas
    print(prompt)

    escolha = prompt["escolha"] #salva o valor da escolha do cli na variavel

    print(escolha)

    return escolha #retorna o valor escolhido no cli

def main():
        loop:bool = True #indica o loop quando deve parar ou não

        while loop == True:
            match choicer():
                case "conectar":
                    bot.connect()

                case "desconectar":
                    bot.desconnect()

                case "mover":
                    x = float(input("X: "))
                    y = float(input("Y: "))
                    z = float(input("Z: "))
                    r = float(input("R: "))
                    bot.move_arm(x, y, z, r)

                case "home":
                    bot.home()

                case "mostrar posição atual":
                    bot.posicao_atual()


                case "toogle tool":
                    tool = inquirer.prompt(
                        [inquirer.List("tool", message="Ecolha ferramente utilizada no momento", choices=["sucker", "griper"])]
                    )["tool"]
                    status = inquirer.prompt(
                        [inquirer.List("status", message="Escolha o modo da ferramenta Ligado=True | Desligado=False", choices=["Ligado", "Desligado"])]
                    )["status"]
                    print(status)
                    bot.toogle_tool(tool=tool, status=status)

                case "sair":
                    loop = False
                    exit()

if __name__ == "__main__":
    
    main()