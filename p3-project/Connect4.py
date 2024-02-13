import sqlite3
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import Session, sessionmaker, relationship, declarative_base, validates #imports a database session
from sqlalchemy.exc import IntegrityError # importing errors
#Define declarative_base() 
# connection = sqlite3.connect("board_game.db")                                 
# cursor = connection.cursor()
Base = declarative_base() #maps our classes to an obj which makes the "meta data"

class PlayingBoard(Base):
  __tablename__ = 'Playing_Board'
  
  id = Column(Integer, primary_key=True)
  col1 = Column(Integer, nullable= True)
  col2 = Column(Integer, nullable= True)
  col3 = Column(Integer, nullable= True)
  col4 = Column(Integer, nullable= True)
  col5 = Column(Integer, nullable= True)
  col6 = Column(Integer, nullable= True)
  col7 = Column(Integer, nullable= True)
  
  players = relationship("Player", back_populates="playing_board")

class Player(Base):
  __tablename__ = "Players"
  id = Column(Integer, primary_key=True)
  symbol = Column(String, nullable=False)
  wins = Column(Integer, nullable=True)
  
  playing_board = relationship("PlayingBoard", back_populates="players")
  playing_board_id = Column(Integer, ForeignKey("Playing_Board.id"))
  
  
  
if __name__ =="__main__":
  engine = create_engine('sqlite:///board_game.db')
  PlayingBoard.__table__.drop(engine)
  Player.__table__.drop(engine)
  
  Base.metadata.create_all(engine)
  Session = sessionmaker(bind=engine)
  session = Session()
  player1 = Player(id=1,symbol="X",wins= 0)
  player2 = Player(id=2,symbol="O",wins= 0)
  session.add_all([player1, player2])
  session.commit()
  
  
  
  while True:
    
    print("Welcome to Connect 4")
    print("1: New Game")
    print("2: Player Options")
    print("0: Exit")
    
    user_input = input("Enter your choice: ")
    if user_input == '1':
      #refresh the playing board first
      for _ in range(6):
        board_row = PlayingBoard(col1="0",col2="0",col3="0",col4="0",col5="0",col6="0", col7="0")
        session.add(board_row)
        session.commit()
      print("refreshed the board")
      session.close()
      #go through the turns for the plays until game ends
      
      
      
      game_over = False
      turn = 0 
      
      while game_over == False:
        
        turn = turn % 2
        if turn == 0:
          print("Player 1 choose a # for which slot to place a piece")
          print("| 1 | 2 | 3 | 4 | 5 | 6 | 7 |")
          print("0: exit")
          col_choice = input("Dropping piece: ")
          try:
            col_choice = int(col_choice)
          except ValueError:
            print("invalid input")
            continue
          
          if 1 <= col_choice <= 7:
            print("Hello")
            sql_command = f'''
            UPDATE Playing_Board SET col1 = {player1.symbol} WHERE id = 6
            '''
            cursor.execute(sql_command)
            turn = turn + 1
            print(turn)
          elif col_choice == 0:
            print("Exiting game")
            game_over = True
          else:
            print("Invalid syntax (1-7)")
        else:
          print("Player 2 choose a # for which slot to place a piece")
          print("| 1 | 2 | 3 | 4 | 5 | 6 | 7 |")
          print("0: exit")
          col_choice = input("Dropping piece: ")
          try:
            col_choice = int(col_choice)
          except ValueError:
            print("invalid input")
            continue
          if 1 <= col_choice <= 7:
            print("Hello")
            
            turn = turn + 1
            print(turn)
          elif col_choice == 0:
            print("Exiting game")
            game_over = True
          else:
            print("Invalid syntax (1-7)")
        
    
    elif user_input == '2':
      #edit player symbol
      while True:
        opt = input("Player to Edit (1-2): ")
        if opt == '1':
          new_symbol = input("Enter a symbol to represent Player 1: ")
          player_to_update = session.query(Player).filter_by(id=1).first()
          player_to_update.symbol = new_symbol
          session.commit()
          print(f"Symbol for Player 1 has been updated to {player_to_update.symbol}")
          
        elif opt == '2':
          new_symbol = input("Enter a symbol to represent Player 2: ")
          player_to_update = session.query(Player).filter_by(id=2).first()
          player_to_update.symbol = new_symbol
          session.commit()
          print(f"Symbol for Player 2 has been updated to {player_to_update.symbol}")
          
        else:
          print("Please enter a valid option.")
          
      
    #exit
    elif user_input == '0':
      print("cya later aligator")
      break
    else:
      print("invalid syntax")