from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine, Column, Integer, String

BaseModel = declarative_base()

class Users(BaseModel):
    __tablename__ = 'user'  # Название таблицы

    # Колонки создаются через Column
    id = Column(Integer, primary_key=True)  # Главный ключ
    user_id = Column(Integer)  # Строка длиной 100 символов
    rol = Column(String(100))  # Число

# Настраиваем подключение к БД (файл указывается при запуске