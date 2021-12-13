# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 14:53:18 2021

@author: Ali
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def app():
    data = pd.read_csv('https://github.com/fahmimnalfrzki/ds-masterclass-h8-vol2/blob/284ec2784a61b03c60bd37b25d69863cf92629af/data/supermarket_sales%20-%20Sheet1.csv?raw=true')
    data['Date'] = data.Date.astype('datetime64[ns]') #Mengubah tipe data Date
    data['Hour'] = pd.DatetimeIndex(data['Time']).hour
    data['Day'] = pd.DatetimeIndex(data['Date']).day
    #st.set_page_config(page_title='Store Review',layout='wide')
    st.title("Store Review")
        
        #------------ Sidebar --------------
    #st.sidebar.subheader("Pilih Kota")
    option = st.sidebar.selectbox('Store City:',list(data['City'].unique()))
    warna = st.sidebar.color_picker("Pilih Warna","#0000FF")
    
    
    city = data['City'].value_counts()
    labels = city.index 
    
    baris_dat,baris_col,baris_pendapatan,baris_gross = st.columns(4)
    baris_dat.metric('Total Transaksi {}'.format(option), len(data[data['City']==option]))
    baris_col.metric('Rating Store {}'.format(option), round(data[data['City']==option]['Rating'].mean(),1))
    baris_pendapatan.metric('Total Pendapatan Store {}'.format(option), round(data[data['City']==option]['Total'].sum()))
    baris_gross.metric('Gross Income Store {}'.format(option),round(data[data['City']==option]['gross income'].sum()))
    plt.style.use('default')    
        #------------ Baris 1 --------------
    baris1_col1,baris1_col2,__ = st.columns((3,3,1))
        ## -- Plot 1 --
    baris1_col1.write('Penjualan selama 1 bulan di store {}'.format(option))
    #Filter Rating
    baris1_col1.bar_chart(data[data['City'] == option].groupby(['Day'])['Quantity'].sum().reset_index(),width=0, height=0)
    ## -- end Plot 1 --    
    
        ## --Plot 2
    #option = baris1_col1.selectbox('Pilih Kota',data['City'].unique())
    baris1_col2.write('Metode Pembayaran yang digunakan di kota {}'.format(option))
    baris1_col2.bar_chart(data[data['City']==option]['Payment'].value_counts().sort_values(ascending=False))
    ## --end Plot 2
        #------------ Baris 2 --------------
    st.header('Total Pendapatan Store Berdasarkan Product line {}'.format(option))
    fig3, ax3 = plt.subplots(figsize=(15,5))
    data[data['City']==option].groupby('Product line').sum()['Total'].sort_values(ascending=True).plot(kind='barh',ax=ax3, color=warna)
    st.pyplot(fig3)
    
    
        
    #-------------- Baris 3 -------------
    
    x=data.groupby(['City']).Gender.value_counts()
    male = [x.values[0], x.values[3], x.values[4]]
    female = [x.values[1],x.values[2],x.values[5]]
        
    x = np.arange(len(labels))
    width = 0.175  # the width of the bars
    st.header('Jumlah Pengunjung berdasarkan Gender')
    fig5, ax5 = plt.subplots(figsize=(15,5))
    rects1 = ax5.bar(x - width/2, male, width, label='Male')
    rects2 = ax5.bar(x + width/2, female, width, label='Female')
    ax5.set_ylabel('Banyak Pengunjung')
    ax5.set_xticks(x)
    ax5.set_xticklabels(labels)
    ax5.legend()
    st.pyplot(fig5)
    
      
    
    
    
    
    #st.header('Tabel Data')
    #st.dataframe(data) 