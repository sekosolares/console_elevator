# Analizador lexico


class Error(Exception):
    pass


class BadLevelRangeException(Error):
    pass

class Ascensor():
    nivel = 0
    estado = 'inicio'
    max_level = 5

    def print_instrucciones(self, piso_act):
        print("\n\nIndique a que nivel se dirige (ingrese [0] para ir a PB):")

        if piso_act == 0:
            piso_act = "PB"
            
        for level in range( (self.max_level * -1), 1):
            level = level * -1 if level < 0 else "PB"
            print(f"[ {level} ] <-- Esta aqui" if level == piso_act else f"[ {level} ]")


    def ascensor(self):
        try:
            self.print_instrucciones(self.nivel)
            level = int(input(" >_ "))
            if level > self.max_level or level < 0:
                raise BadLevelRangeException 

            self.estado = 'inicio'
            print("\n\nDetalle de estados:")
            while not self.estado == 'detenido':
                print(self.estado)

                if level == self.nivel:
                    self.estado = 'detenido'
                    print(self.estado)

                if level > self.nivel:
                    self.estado = 'subiendo'
                    self.nivel += 1

                if level < self.nivel:
                    self.estado = 'bajando'
                    self.nivel -= 1

            self.print_instrucciones(self.nivel)
        except ValueError as valerr:
            print("\nSe ha ingresado un valor no permitido!")
        except BadLevelRangeException as bad_level_err:
            print("\nSe ha ingresado un valor fuera del rango permitido!")


    


def main():
    off = False
    ascensor = Ascensor()
    while not off:
        ascensor.ascensor()
        resp = input("\nSalir del ascensor? (s/n) >_ ")
        off = resp.upper() == 'S'

if __name__ == '__main__':
    main()
