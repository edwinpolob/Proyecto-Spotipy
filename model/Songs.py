import itertools
import TableIt
import webbrowser
import vlc
from operaciones import song_control

class Song:

    newid=itertools.count()
    
    def __init__(self, title, genre, singer, duration, year) -> None:
        self.id=next(Song.newid)
        self.title=title
        self.genre=genre
        self.singer=singer
        self.duration=duration
        self.year=year
        self.link=""
        self.file=""
        self.table=[]
        self.table.append(["ID","Title", "Genre","Singer","Duracion","Year"])
        self.table.append(self.Tabulate())

    def showAttributes(self):
        TableIt.printTable(self.table, useFieldNames=True)
    
    def playSong(self):
        #webbrowser.open(self.link)
        p = vlc.MediaPlayer(self.file)
        p.play()

    
    def Tabulate(self):
        d= self.__dict__
        lista=list(d.values())
        return lista 


class Playlist:
    def __init__(self,name,description):
        self.name=name
        self.description=description
        self.songs=[]
        self.table=[]
        self.table.append(["ID","Title", "Genre","Singer","Duracion","Year"])
        
    def showAttributes(self):
        print("Name: ", self.name)
        print("Description: ", self.description)
        print("The list of songs: ")
        print("")
        TableIt.printTable(self.table, useFieldNames=True)
       
    
    def Table(self):
        for i in self.songs:
            self.table.append(i.Tabulate())
        



        

        

        
        


