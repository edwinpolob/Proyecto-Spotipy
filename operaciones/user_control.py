from operaciones import song_control
from model import Person
from model.Person import User
import os
import time

usuarios=[]
user1=User("Edwin","Polo","","edpo77","123","edwin.com","")
user1.typeofUser="User"
user2=User("Laura","","","laura77","123","","")
usuarios.append(user1)
usuarios.append(user2)


def menuUser ():
    print ("******Bienvenidos a SPOTIPY*****************")
    print ("* 1.Crear un playlist")
    print ("* 2.Escuchar una cancion")
    print ("* 3.Mostrar la informacion de las canciones")
    print ("* 4. MOstrar listas de reproduccion por usuario")
    print ("* 5.Exit/Quit")
    print("*********************************************")
    

def OptionUser():
    while True:
        menuUser()
        opcion=input("Que te gustaria hacer? \n")
        if opcion=="1":
            song_control.createPlaylist()            
        elif opcion=="2":
            song_control.playSongs()                               
        elif opcion=="3":
            song_control.showSongs()             
        elif opcion=="4":
            showPlaylistbyUser()
        elif opcion=="5":
            print("\n Goodbye")
            time.sleep(5)
            os.system("cls")
            break
        elif opcion !="":
            print("\n Not Valid Choice Try again")


def OptionAdmin():
    while True:
        menuAdmin()
        opcion=input("Que te gustaria hacer? \n")
        if opcion=="1":
            song_control.CreateSongs()
        elif opcion=="2":
            song_control.showSongs()                    
        elif opcion=="3":
            print("\n Goodbye")
            time.sleep(5)
            os.system("cls")
            break
        elif opcion !="":
            print("\n Not Valid Choice Try again")


def menuAdmin ():
    print ("******Bienvenidos a SPOTIPY*****************")
    print ("* 1.Crear Canciones")
    print ("* 2.Mostrar la información de las canciones")
    print("* 3.Exit/Quit")
    print("*********************************************")


def showPlaylistbyUser():
    print ("The playlist of the User: ", usuarios[Person.UserId].name, " ", usuarios[Person.UserId].apellido, " are: ")
    print("")
    for user in usuarios[Person.UserId].playlists:
        user.showAttributes()


def IntroToSystem():
    while True:
        print ("******Bienvenidos a SPOTIPY*****************")
        opcion=int(input("Seleccione Opcion: 1. Login, 2. Register  3. Salir"))
        for i in usuarios:
            i.showAttributes()
        if opcion == 1:
            intentos=1
            salir=False
            while intentos <=3:
                print ("Este es su intento No {}".format(intentos))
                usuario=input("Digite su  usuario: ")
                password=input("Digite su clave: ")
                for i in usuarios:
                    i.loginUser(usuario,password)
                    if i.login==True:
                        salir=True
                        break
                if salir==True:
                    break
                intentos+=1
        elif opcion==2:
            print ("Bienvenido, vamos al registro en el sistema: ")
            user=User("","","","","","","")
            user.RegisterUser()
            usuarios.append(user)
            print("Usuario registrado con exito")
            time.sleep(3)
            os.system("cls")
        elif opcion==3:
            print("\n Goodbye")
            time.sleep(5)
            os.system("cls")
            break
        elif opcion !="":
            print("\n Not Valid Choice Try again")