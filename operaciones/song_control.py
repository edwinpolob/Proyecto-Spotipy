import os
from model import Songs
from model.Songs import Playlist, Song
from operaciones import user_control
from model import Person
from model.Person import User
import time
import TableIt



Songs=[]
listSongsPlaylist=[]
listSongsPlaylist.append(["ID","Title", "Genre","Singer","Duracion","Year"])
listSong=[]
listSong.append(["ID","Title", "Genre","Singer","Duracion","Year"])
song1=Song("I am the best","Pop","2NE1","240","2011")
song1.link="https://www.youtube.com/watch?v=j7_lSP8Vc3o"
song1.file="/MP3/I am the best.mp3"
song2=Song("Dancing Queen","Rock","ABBA","190","1976")
song2.file="/MP3/Dancing Queen.mp3"
song3=Song("Beautiful","Pop Rock","Cristina Aguilar","300","2002")
song4=Song("Rose Garden","Soul","Lynn Anderson","189","1970")
song5=Song("Hero","Pop","Mariah Carey","245","1993")
Songs.append(song1)
Songs.append(song2)
Songs.append(song3)
Songs.append(song4)
Songs.append(song5)

for i in Songs:
    listSong.append(i.Tabulate())


def showSongs ():
    print("**Songs List**")
    TableIt.printTable(listSong, useFieldNames=True)
              
    print("")

def CreateSongs ():
    
    song=Song("","","","","")
    print(" Con esta opción usted podrá agregar una nueva cancion")

    """Ingreso titulo de la cancion"""
    song.title=input("Indique el titulo de la cancion: \n")    

    """Ingreso del Genero de la canción"""    
    song.genre=input("Indique el genero de la cancion: \n")    

    """Ingreso del cantante de la cancion"""
    song.singer=input("Indique el cantante de la cancion: \n")

    """Ingreso la duración de la cancion en segundos"""
    song.duration=int(input("Indique la duración de la canción en segundos: \n"))

    """Ingreso del año de la cancion"""
    song.year=input("Indique el año de la cancion: \n")
    Songs.append(song)

    time.sleep(5)
    os.system("cls")    

    print ("La información de la canción cuyo titulo es ", song.title, " es: ")
    a=song.Tabulate()
    listSong.append(a)    
    song.showAttributes()
    
    


def createPlaylist():
    play1=Playlist("","")
    print ("Vamos a crear un playlist")
    play1.name=input("Cual será el nombre del playlist? ")
    play1.description=input("De una breve descripcion del playlist: ")
    print("Ahora vamos a agregar las canciones del playlist: ")

    TableIt.printTable(listSong, useFieldNames=True)
    while True:
        selected=int(input("Digite el ID de la cancion: "))
        for song in Songs:
            if selected==song.id:
                play1.songs.append(song)
                
        option=int(input("Desea agregar una nueva canción: 1. SI    2.NO "))
        if option==1:
            continue
        else:
            break

    play1.Table()

    print ("La informacion del playlist de nombre: ", play1.name, " es: ")
    play1.showAttributes()
    user_control.usuarios[Person.UserId].addplayListUser(play1)



def playSongs():
    print ("Here you can select your song: ")
    showSongs()
    selected=int(input("Digite el ID de la cancion: "))
    for song in Songs:
        if selected==song.id:
            song.playSong()
    

    

       




    
  



    








