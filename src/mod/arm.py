import pydobot
from serial.tools import list_ports
from yaspin import yaspin
from time import sleep

class Robozinho(pydobot.Dobot):
    def __init__(self) -> None:
        
        self.loader = yaspin("carregando..seja paciente") #loader


    def connect(self):
        self.loader.start()
        try:
            porta_disponivel = list_ports.comports()
            
            for port in porta_disponivel:
                print(port)

            porta = porta_disponivel[0].device
            self.device_ = pydobot.Dobot(port=porta, verbose=False) #Variavel global pq tem self.
            self.loader.ok("Conectado com sucesso")
        except:
            self.loader.fail("Dispositivo não encontrado")
        sleep(2)


    def desconnect(self):
        self.device_.close() #desconectar o braço


    def move_arm(self, x:float, y:float, z:float, r:float):
        try:
            self.device_.move_to(x, y, z, r, wait=True)
        except:
            self.connect()


    def home(self):
        self.move_arm(240, 0, 150, 0)

    def posicao_atual(self): #Mário me ajudou a criar essa função
        posicao = self.device_.pose()
        print(f"A posição atual é: {posicao}")
    

    def toogle_tool(self, tool:str, status):
        match status:
            case "Ligado":
                status=True
        
            case "Desligado": 
                status=False
        
        self.loader.start()
        try:
            match tool:
                case "griper":
                    self.device_.grip(status)

                case "sucker":
                    self.device_.suck(status)
            self.loader.ok("Ferramente executada com sucesso")

        except:
            self.loader.fail("Nenhum dispositivo encontrado")
            self.connect()

        sleep(2)
                

                 
