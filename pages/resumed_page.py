import streamlit as st
import controllers.dataController as dc
import controllers.userController as uc
import controllers.settingsController as settings
import time
import pandas as pd
from controllers.dataController import *


@st.cache_data(ttl=10)
def load_data_chosen_by_adm():
    if settings.get_chosen_table_value():
        return dc.get_table_data(settings.get_chosen_table_value())

st.dataframe(load_data_chosen_by_adm())

