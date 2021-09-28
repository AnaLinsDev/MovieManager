from model.Person import Person
from view.MainView import MainView
from view.UserView import UserView

class Main():

    def __init__(self, user=""):
        self._user = Person("","")

        self._main_view = MainView()
        self._user_view = UserView()
        

    def get_user(self):  
        return self._user
    def set_user(self, newUser):  
        self._user = newUser

    def get_main_controller(self):  
        return self._main_controller

    def get_user_controller(self):  
        return self._user_controller

    def get_manager_controller(self):  
        return self._manager_controller

    def menu(self):

        if self._user.get_name() == "" :
            return input(" 1 - Login \n 2 - Register \n 3 - Sair \n Digite sua opção: ")
 
        elif self._user.get_name().startswith("admin"):
            return input(" 1 - Listar Filmes \n 2 - Adicionar Filme \n 3 - Remover Filme \n 4 - Editar Filme \n 5 - Logout \n 6 - Sair \n Digite sua opção: ")

        else:
            return input(" 1 - Listar Filmes \n 2 - Listar Filmes favoritos \n 3 - Adicionar Filme na Lista de favoritos \n 4 - Remover Filme da lista de favoritos \n 5 - Logout \n 6 - Sair \n Digite sua opção: ")
        
main = Main()
answer = main.menu() 

while answer != 3 and main._user.get_name() == "":

    if main._user.get_name() == "" :

        if answer == '1' :
            res = main._main_view.login()
            if res != None:
                main.set_user(res)
                print (" Logado ")
            else : 
                print (" Ocorreu um problema ")

        if answer == '2' :
            res = main._main_view.register()
            if res != None:
                main.set_user(res)
                print (" Logado ")
            else : 
                print (" Ocorreu um problema ")

        if answer == '3' :
            print (" Volte sempre ! ^^ \n\n")
            break

    answer = main.menu()
# and  not main._user.get_name().startswith("admin")
while answer != 6 and main._user.get_name() != "" :

    if answer == '1' :
        print ("\nFILMES: ")
        movies = main._user_view.get_movies()
        for m in movies :
            print ( m.get_key() , " )  " , m.get_name() , " - " , m.get_year() )
        print ("\n")

    if answer == '2' :
        print ("\nFavoritos:  ")
        movies  = main._user_view.get_favorite_movies(main._user)
        for m in movies :
            print ( m.get_key() , " )  " , m.get_name() , " - " , m.get_year() )
        print ("\n")

    if answer == '3' :

        print ("\nFILMES: ")
        movies = main._user_view.get_movies()
        for m in movies :
            print ( m.get_key() , " )  " , m.get_name() , " - " , m.get_year() )
        print ("\n")

        res = main._user_view.add_favorite_movies(main._user)
        if res != None:
            print ("\nAdicionando Filme Favorito  ")
            main.set_user(res)
        else:
            print("Ocorreu um problema")
        print ("\n")

    if answer == '4' :
                
        print ("\nFavoritos:  ")
        movies  = main._user_view.get_favorite_movies(main._user)
        for m in movies :
            print ( m.get_key() , " )  " , m.get_name() , " - " , m.get_year() )
        print ("\n")

        res = main._user_view.rem_favorite_movies(main._user)
        if res != None:
            print ("\nRemovendo Filme Favorito  ")
            main.set_user(res)
        else:
            print("Ocorreu um problema")
        print ("\n")

    if answer == '5' :
        print (" Volte sempre ! ^^ \n\n")
        main.set_user(Person("",""))
        
    if answer == '6' :
        print (" Volte sempre ! ^^ \n\n")
        break 
        
    answer = main.menu()








 
     