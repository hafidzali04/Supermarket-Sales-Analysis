# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 14:25:35 2021

@author: Ali
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy import stats

def app():
    data = pd.read_csv('https://github.com/fahmimnalfrzki/ds-masterclass-h8-vol2/blob/284ec2784a61b03c60bd37b25d69863cf92629af/data/supermarket_sales%20-%20Sheet1.csv?raw=true')
    city1 = data[data['City']=='Yangon']
    city2 = data[data['City']=='Mandalay']
    city3 = data[data['City']=='Naypyitaw']
    data['Date'] = data.Date.astype('datetime64[ns]') #Mengubah tipe data Date
    st.subheader('Hypothesis Testing')
    st.write("Apakah daily average of sales of two store are significantly different or not H0: μ_Yangon= μ_Naypyitaw H1: μ_Yangon != μ_Naypyitaw")
    baris_dat,baris_col = st.columns(2)
    daily_yangon = city1[['Date','Total']].groupby('Date').sum().sample(80)
    daily_nay = city3[['Date','Total']].groupby('Date').sum().sample(80)
    
    baris_dat.metric('Average sales of Yangon a day: ',np.round(daily_yangon.Total.mean()))
    baris_col.metric('Average sales of Naypyitaw a day: ',np.round(daily_nay.Total.mean()))
    baris2_dat,baris2_col = st.columns(2)
    t_stat, p_val = stats.ttest_ind(daily_yangon,daily_nay)
    baris2_dat.metric('P-value:',p_val[0]) #the p-value isn't divided by 2 since the output is two-sided p-value
    baris2_col.metric('t-statistics:',t_stat[0])
    yangon_pop = np.random.normal(daily_yangon.Total.mean(),daily_yangon.Total.std(),300)
    nay_pop = np.random.normal(daily_nay.Total.mean(),daily_nay.Total.std(),300)

    ci = stats.norm.interval(0.90, daily_yangon.Total.mean(),daily_yangon.Total.std())
    fig, ax = plt.subplots(figsize=(15,5))
    
    sns.distplot(yangon_pop, label='Yangon Average Sales a Day *Pop',color='blue')
    sns.distplot(nay_pop, label='Naypyitaw Average Sales a Day *Pop',color='red')

    plt.axvline(daily_yangon.Total.mean(), color='blue', linewidth=2, label='Yangon mean')
    plt.axvline(daily_nay.Total.mean(), color='red',  linewidth=2, label='Naypyitaw mean')
    
    plt.axvline(ci[1], color='green', linestyle='dashed', linewidth=2, label='confidence threshold of 95%')
    plt.axvline(ci[0], color='green', linestyle='dashed', linewidth=2)

    plt.axvline(yangon_pop.mean()+t_stat[0]*yangon_pop.std(), color='black', linestyle='dashed', linewidth=2, label = 'Alternative Hypothesis')
    plt.axvline(nay_pop.mean()-t_stat[0]*nay_pop.std(), color='black', linestyle='dashed', linewidth=2)
    
    st.pyplot(fig)
    st.write("Berdasarkan nilai P_value yang dihasilkan  kita bisa terima hipotesis 0 bahwa penjualan di kota yangon tidak terlalu berbeda dari kota Naypyitaw")