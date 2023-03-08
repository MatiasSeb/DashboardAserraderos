from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from config.database import engine_users, session_users

Base = declarative_base()

class GlobalSettings(Base):
    __tablename__ = 'global_settings'
    
    setting_id = Column(Integer, primary_key=True, index=True)
    setting_name = Column(String(50), unique=True, nullable=False)
    setting_value = Column(String(15), nullable=False)
    
    def initialize_settings():
        settings = session_users.query(GlobalSettings).all()
        
        if not settings:
            #AQUI SE AGREGAN LAS CONFIGURACIONES DE USUARIO Y CONTENIDO
            default_settings = [
                GlobalSettings(setting_name='chosen_table', setting_value='camara1'),
                GlobalSettings(setting_name='first_admin_registered', setting_value='False')
            ]
            session_users.add_all(default_settings)
            session_users.commit()

Base.metadata.create_all(engine_users)
GlobalSettings.initialize_settings()