from sqlalchemy.orm import Session
from models.settingModels import GlobalSettings
from config.database import session_users
import streamlit as st

@st.cache_data(ttl=30)
def get_chosen_table_value():
    chosen_table = session_users.query(GlobalSettings).filter_by(setting_name = 'chosen_table')
    if chosen_table:
        return chosen_table.first().setting_value

@st.cache_data
def update_global_setting(setting_name, setting_value):
    setting_to_update = session_users.query(GlobalSettings).filter_by(setting_name=setting_name).first()
    if setting_to_update:
        setting_to_update.setting_value = setting_value
        session_users.commit()
        return True    
    else:
        return False & print('No setting found with name: ' + setting_name)

@st.cache_data
def first_register_made():
    first_register_setting = session_users.query(GlobalSettings).filter_by(setting_name='first_admin_registered').first()
    if first_register_setting:
        return first_register_setting.setting_value == 'True'
    else:
        return False

@st.cache_data
def update_first_admin_registered(setting_value):
    first_admin_register = session_users.query(GlobalSettings).filter_by(setting_name='first_admin_registered').first()
    if first_admin_register:
        first_admin_register.setting_value = setting_value
        session_users.commit()
        return True
    else:
        return False