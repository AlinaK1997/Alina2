from random import choice

class PassegiataALeatoria:
    """Una classa che genera la passegiata"""

    def __init__(self, passi = 1000):
        self.passi = passi

        self.x = [0]
        self.y = [0]

    def fare_passegiata(self):
        """Calcolare tutti i punti durante la passegiata aleatoria"""

        while len(self.x) < self.passi:
            
            x_direzione = choice([-1, 1])
            x_distanza = choice([0, 1, 2, 3, 4])
            x_passo = x_direzione * x_distanza

            y_direzione = choice([-1, 1])
            y_distanza = choice([0, 1, 2, 3, 4])
            y_passo = y_direzione * y_distanza

            #Movimenti di [o, 0] non sono accetati


            if x_passo == 0 and y_passo == 0:
                continue

            x_attuale = self.x[-1] + x_passo
            y_attuale = self.y[-1] + y_passo

            self.x.append(x_attuale)
            self.y.append(y_attuale)





