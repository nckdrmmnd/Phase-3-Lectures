import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Connect4 import *

if __name__ == "__main__":
  engine = create_engine('sqlite:///board_game.db')
  PlayingBoard.__table__.drop(engine)
  Base.metadata.create_all(engine)
  
  Session = sessionmaker(bind=engine)
  session = Session()
  
  for _ in range(6):
    board_row = PlayingBoard(col1="0",col2="0",col3="0",col4="0",col5="0",col6="0", col7="0")
    session.add(board_row)
    session.commit()
  print("refreshed the board")
  session.close()