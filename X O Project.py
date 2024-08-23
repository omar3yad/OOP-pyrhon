import os 

def cls() :
   os.system("cls")

class player :
  
  def __init__(self):
      self.__name = None
      self.__symbol = None   

  def get_name(self) :
    return self.__name 
  
  def set_name(self, name):
      self.__name = name

  def get_symbol(self) :
    return self.__symbol 

  def set_symbol(self, symbol):
      self.__symbol = symbol.upper()
      
  def choose_name(self) :
    while True:
      name = input("Enter Your Name (Letters) Only : ")
      if name.isalpha():
        self.set_name(name)
        break
      else:
        print("Invalid Name. Please (Use Letter) Onle :(")

  def choose_symbol(self) :
    f = False
    while not f:
      symbol = input("Enter Your symbol (X or O) Only: ")
      if symbol.upper() == 'X' or symbol.upper() == 'O':
        self.set_symbol(symbol)
        break
      else:
        print("Invalid Symbol. Please Enter (X or O) Only :(")

##########################

class menu :

  def __init__(self) -> None:
    pass
  
  def check_1or2(self) :
    while True:
      choice = input("Please Enter Your Choice (1 Or 2): ")
      if choice.isdigit() :
        if int(choice) == 1 or int(choice) ==  2 :
          cls()
          return int(choice)
      
  def display_main_menu(self) : 
    print("Welcom To My X O Game ❤")
    print("1: Start Gmae ")
    print("2: Quik Game")
    return self.check_1or2()
      
  def display_end_menu(self) :
    print("Game Over :|")
    print("1: Restart Gmae ")
    print("2: Quik Game")
    return self.check_1or2()

##########################

class board :

  def __init__(self) -> None:
    self.list = [1,2,3,4,5,6,7,8,9]
  
  def display_board(self) :
    cls()
    print("---------------")
    for i in range(0, 9, 3):
        row = "| " + " || ".join(str(self.list[j]) for j in range(i, i+3)) + " |"
        print(row)
        print("---------------")

  def get_choice(self) :
    while True :
      choice = input("Enter Number (1..9) : ")
      if not choice.isdigit():
          print("Bad choice: Not a number")
      else:
          choice = int(choice)
          if choice < 1 or choice > 9:
              print("Bad choice: Out of range")    
          elif self.list.count(choice) == 0:
              print("Bad choice: Number is used")
          else:
              return choice
          
  def updat_board(self, s) :
    choice = self.get_choice()
    self.list[choice-1] = s

  def reset_board(self):
      self.list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

##########################

class game :

  def __init__(self):
      self.board = board()
      self.players = [player(), player()]
      self.menu =  menu()
      self.curant_player = False # 1

  def setup_players(self) : 
    print("Setting up Player 1")
    self.players[0].choose_name()
    self.players[0].choose_symbol()
    symbol1 = self.players[0].get_symbol()
    symbol2 = 'O' if symbol1 == 'X' else 'X'
    cls()
    print("Setting up Player 2")
    self.players[1].choose_name()
    self.players[1].set_symbol(symbol2)
    cls()

  def quit_game(SELF) :
    print ("Thank you for game :) ")

  def check_win(self ,s) :
    b = self.board.list
    for i in range(0, 9, 3): # Check rows
      if b[i] == b[i + 1] == b[i + 2] == s:
          return True
    for i in range(3): # Check columns
      if b[i] == b[i + 3] == b[i + 6] == s:
          return True
    if b[0] == b[4] == b[8] == s:
      return True
    if b[2] == b[4] == b[6] == s:
      return True
    return False
  
  def check_draw(self):
      if all(type(x) == str for x in self.board.list):
          return not any(self.check_win(symbol) for symbol in ['X', 'O'])
      return False

  def restart_game(self):
    self.board.reset_board()
    self.curant_player = False # 1
    self.play_game()

  def show_end_menu(self):
    choice = self.menu.display_end_menu()
    if choice ==1 :
      self.board.reset_board()
      self.restart_game()
    else :
      self.quit_game()

  def play_game(self) :
     while True :
      self.board.display_board()
      p = self.players[self.curant_player]
      print(f"{p.get_name()}'s turm '{p.get_symbol()}'")
      self.board.updat_board(p.get_symbol())
      self.curant_player = not self.curant_player
      if self.check_win(p.get_symbol()) :
        cls()
        self.board.display_board()
        print(f"{p.get_name()} is wins! 🎆")
        self.show_end_menu()
        break
      if self.check_draw():
        print("Drow")
        self.show_end_menu()
        break
         
  def start_game(self) :
    choice = self.menu.display_main_menu()
    if choice == 1 :
      self.setup_players()
      self.play_game()
    else :
       self.quit_game()

##########################

g = game()
g.start_game()