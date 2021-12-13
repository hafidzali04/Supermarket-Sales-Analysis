# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 14:19:41 2021

@author: Ali
"""

import store_review, cust_behav, hypotesis
import streamlit as st

st.set_page_config(page_title='Supermarket Sales',layout='wide')
PAGES = {
    'Store Review': store_review,
    'Customer Behavior': cust_behav,
    'Hypothesis Testing': hypotesis,
       }

#st.title('Supermarket Sales')

st.sidebar.title('Supermarket Sales Review')
selection = st.sidebar.selectbox("Pages ", list(PAGES.keys()))
page = PAGES[selection]

page.app()

  