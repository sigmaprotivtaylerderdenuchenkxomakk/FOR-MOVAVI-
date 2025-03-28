from config import *
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine, Column, Integer, String
from db_create import *


class User():
    def __init__(self, user_id, rol):
        self.user_id = user_id
        self.rol = rol

    @staticmethod
    def get_user_by_id(id: int)-> str:
        """Возращает роль по id user 
        если его нет в базе данных то
        говорит об этом

        Args:
            id (int): 
        """
        engine = create_engine("sqlite:///" + db_name)
        Session = sessionmaker(bind=engine)
        session = Session()
        user: str
        try:
            user = session.query(Users).filter_by(user_id=id).first().rol
        except:
            user = 'Пользователь не найден'
        session.close()
        return user

    @staticmethod
    def save_user(id:int, rol:str)->None:
        """Сохраняет id и роль в базу данных
        Args:
            id (int): 
            rol (str):
        """
        engine = create_engine("sqlite:///" + db_name)
        Session = sessionmaker(bind=engine)
        session = Session()
        new_user = Users(user_id=id, rol=rol)
        session.add(new_user)
        session.commit()
        session.close()
