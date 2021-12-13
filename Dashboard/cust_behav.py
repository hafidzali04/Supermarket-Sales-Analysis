# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 22:34:16 2021

@author: Ali
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def app():
    data = pd.read_csv('https://github.com/fahmimnalfrzki/ds-masterclass-h8-vol2/blob/284ec2784a61b03c60bd37b25d69863cf92629af/data/supermarket_sales%20-%20Sheet1.csv?raw=true')
    
    def func(pct, allvalues):
        absolute = int(pct / 100.*np.sum(allvalues))
        return "{:.1f}%\n({:d})".format(pct, absolute)
    
    #st.set_page_config(page_title='Customer Behavior',layout='wide')
    st.title("Customer Behavior")
    
    #------------ Sidebar --------------
    #st.sidebar.subheader("Customer Gender")
    option = st.sidebar.selectbox('Select Customer Gender:',list(data['Gender'].unique()))
    warna = st.sidebar.color_picker("Pilih Warna","#0000FF")
    
    
    baris_dat,baris_col,baris_pendapatan = st.columns(3)
    baris_dat.metric('Transaction Total {}'.format(option), len(data[data['Gender']==option]))
    baris_col.metric('Rating Store Base on {}'.format(option), round(data[data['Gender']==option]['Rating'].mean(),1))
    baris_pendapatan.metric('Total Income Base on {}'.format(option), round(data[data['Gender']==option]['Total'].sum()))
    genderclass_dat = data[data['Gender']==option] 
    #------------ Baris 1 --------------
    ## -- Plot 1 --
    baris1_col1,baris1_col2,baris1_col3 = st.columns((3,3,1))
    
    fig1,ax1 = plt.subplots()
    explode = (0.1, 0, 0, 0, 0, 0)
    
    tc = genderclass_dat['Product line'].value_counts()
    label=tc.index
    ax1.pie(tc,explode=explode, labels=label, autopct = lambda pct: func(pct, tc), startangle=90)
    
    baris1_col1.write('Transaction Customer {}'.format(option))
    baris1_col1.pyplot(fig1)
    ## -- end Plot 1 --
    
    
    ## --Plot 2
    fig2,ax2 = plt.subplots()
    explode = (0.1, 0, 0, 0, 0, 0)
    spend = genderclass_dat.groupby('Product line').sum()['Total'].sort_values(ascending=False)
    label=spend.index
    ax2.pie(spend,explode=explode, labels=label, autopct = lambda pct: func(pct, spend), startangle=90)
    
    baris1_col2.write('Customers Spend across Product Line')
    baris1_col2.pyplot(fig2)
    ## --end Plot 2
    
    
    #-------------- Baris 2 -------------
    
    #baris2_col1,baris2_col2= st.columns((5,5))
    st.write('Highest Spend Product Line by Customer')
    #fig3, ax3 = plt.subplots()
   # genderclass_dat.groupby('Product line').max()['Total'].sort_values(ascending=True).plot(kind='barh',ax=ax3, color=warna)
    st.bar_chart(genderclass_dat.groupby('Product line').max()['Total'].sort_values(ascending=False))
    
    
    st.write('Payment Method by Customer')
    #fig4, ax4 = plt.subplots()
    #genderclass_dat['Payment'].value_counts().sort_values(ascending=True).plot(kind='barh',ax=ax4, color=warna)
    st.bar_chart(genderclass_dat['Payment'].value_counts().sort_values(ascending=True))

