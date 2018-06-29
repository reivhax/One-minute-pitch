import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY=os.getenv('SECRET_KEY')
    DATABASE_PASSWORD=os.getenv('DATABASE_PASS')
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://xv:{}@localhost/pomodoro'.format(DATABASE_PASSWORD)
    SQLALCHEMY_TRACK_MODIFICATIONS=True

class ProdConfig(Config):
    '''
    Pruduction configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass

class TestConfig(Config):
    '''
    Testing configuration child class

    Args:
        Config: The parent configuration class with General configuration settings 
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class
    
    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}