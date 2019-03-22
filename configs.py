from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker


class EmailConfig:
    HOST = 'smtp.gmail.com'
    PORT = 587
    USE_TLS = True
    HOST_USER = ''
    HOST_PASSWORD = ''

    @staticmethod
    def make_config():
        smtp = {
            'host': EmailConfig.HOST,
            'port': EmailConfig.PORT,
            'tls': EmailConfig.USE_TLS,
            'user': EmailConfig.HOST_USER,
            'password': EmailConfig.HOST_PASSWORD
        }
        return smtp


class SQLAlchemyConfig:
    DRIVER = 'postgresql+psycopg2'
    USERNAME = 'sadmonad'
    PASSWORD = '12345'
    HOST = 'localhost'
    PORT = 5432
    DATABASE_NAME = 'rest_mandarin'

    @staticmethod
    def make_config():
        url = URL(SQLAlchemyConfig.DRIVER,
                  username=SQLAlchemyConfig.USERNAME,
                  password=SQLAlchemyConfig.PASSWORD,
                  host=SQLAlchemyConfig.HOST,
                  port=SQLAlchemyConfig.PORT,
                  database=SQLAlchemyConfig.DATABASE_NAME)
        SQLAlchemyConfig.ENGINE = create_engine(url)
        Session = sessionmaker(bind=SQLAlchemyConfig.ENGINE, autocommit=True)
        SQLAlchemyConfig.SESSION = Session()
