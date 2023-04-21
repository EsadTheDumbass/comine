import tkinter

class Cindy():
    def __init__(self):
        self.leeftijd = 15
        self.school = "Coder Minds"
        self.fav_docent = "Meester Salih"

    def vraag(self, vraagje:str):
        v = input(vraagje)
    def zeg(self, woorden: str):
        print("Cindy zegt: " + woorden)
    def maak_dialogue(self,woordjes: str):
        print("Cindy: " + woordjes)
    def zeg_hallo(self):
        print('Cindy: Hallo!')

class Bob():
    def __init__(self):
        self.leeftijd = 15
        self.school = "Coder Minds"
        self.fav_docent = "Meester Esat"

    def vraag(self, vraagje:str):
        v = input(vraagje)
    def zeg(self, woorden: str):
        print("Bob zegt: " + woorden)
    def maak_dialogue(self,woordjes: str):
        print("Bob: " + woordjes)
    def zeg_hallo(self):
        print('Bob: Hallo!')

bob = Bob()
cindy = Cindy()
bob.zeg("lekker?")