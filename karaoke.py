########################      A        ######################

# creation de la classe Player
class Player:
    # creation des options de la classe
    def __init__(self, surnom, nbrpoints):  
        self.__pseudo = surnom
        self.__scores = nbrpoints
        
    # creation d'une fonction qui envoie le score d'une musique     
    def EnvoieScore(self, chanson):
            print(self.__scores[chanson])        

    #creation d'une fonction qui ajoute un score a la musique
    def NouveauScore(self, newscore, nomChanson):                   
        self.nouveauscore = newscore
        self.songname = nomChanson
        # conditions qui verifie que le nouveau score est superieur à l'ancien
        if self.nouveauscore >= self.__scores[self.songname]:         
            self.__scores[self.songname] = newscore
            print("ton nouveau score est de", self.__scores[self.songname])
        else:
            print("Tu n'a pas battu ton record!")
     
     
    #fonction renvoyant le score moyen
#    def MoyScore(self)
    #fonction renvoyant le score le plus haut
#    def BestSong(self)
    #fonction renvoyant le score le plus bas
#    def WorstSong(self)
    
    #fonction renvoyant le score total
    def TotalScore(self):                   
        ScoreMaximum = 0
        #parcours le tableau ScoreChanson en entier
        for i in self.__scores:                      
            ScoreMaximum += self.__scores[i]            
        print (self.__pseudo,"ton score total est de", ScoreMaximum)                       
    
    
    
    
#creation d'un tableau avec les musiques et les scores            
ScoreChanson={0:50, 1:95, 2:85, 3:55, 4:68}        

Jean = Player("Jean",ScoreChanson)
Jean.EnvoieScore(2)
Jean.NouveauScore(55,0)
#Jean.MoyScore()
#Jean.BestSong()
#Jean.WorstSong()
Jean.TotalScore()


########################      B        ######################

class Karaoke:
    
    def __init__(self, chanson, nbrPlayer):
        self.__nchanson = chanson
        self.__nPlayer = nbrPlayer