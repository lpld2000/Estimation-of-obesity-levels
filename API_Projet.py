# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 14:11:31 2022

@author: leopo
"""

import streamlit as st
import time
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import seaborn as sns
import statistics

st.title("Estimation of obesity levels")
st.write("""Réalisé par Mohammed Hormi et Léopold Dumenil""")
         
obesity=pd.read_csv("data_obesity.csv")

IMC=[]
for i in range (len(obesity["Height"])):
  imc=obesity["Weight"][i]/(obesity["Height"][i])**2
  IMC.append(imc)

obesity["IMC"]=IMC

obe_numeric=obesity.select_dtypes(include='number')


fig,axs=plt.subplots(3,3)
fig.set_size_inches(22,15)

sns.distplot(obe_numeric['Age'],bins=50,kde=True,ax=axs[0,0])
sns.distplot(obe_numeric['Weight'],bins=50,kde=True,ax=axs[0,1])
sns.distplot(obe_numeric['Height'],bins=50,kde=True,ax=axs[0,2])
sns.distplot(obe_numeric['IMC'],bins=50,kde=True,ax=axs[1,0])
sns.distplot(obe_numeric['FCVC'],bins=50,kde=True,ax=axs[1,1])
sns.distplot(obe_numeric['NCP'],bins=50,kde=True,ax=axs[1,2])
sns.distplot(obe_numeric['CH2O'],bins=50,kde=True,ax=axs[2,0])
sns.distplot(obe_numeric['FAF'],bins=50,kde=True,ax=axs[2,1])
sns.distplot(obe_numeric['TUE'],bins=50,kde=True,ax=axs[2,2])

st.pyplot(fig)

st.write("Visualisation des données numérique du dataset")

fig, axs = plt.subplots(3, 3)
fig.set_size_inches(22,15)

Male=obesity[obesity['Gender']=='Male']
Female=obesity[obesity['Gender']=='Female']
labels=['Male','Female']
gender = [Male,Female]
nb_gender = [len(x.index) for x in gender]
axs[0, 0].pie(nb_gender, labels=labels, autopct='%1.1f%%')

Yes=obesity[obesity['family_history_with_overweight']=='yes']
No=obesity[obesity['family_history_with_overweight']=='no']
labels= ['Family with overweight','Family without overweight']
Family = [Yes,No]
nb_Family = [len(x.index) for x in Family]
axs[0, 1].pie(nb_Family, labels=labels, autopct='%1.1f%%')

Yes =obesity[obesity['FAVC']=='yes']
No =obesity[obesity['FAVC']=='no']
labels = ['Eat high caloric food',"Don't eat high caloric food"]
Caloric = [Yes, No]
nb_Caloric = [len(x.index) for x in Caloric]
axs[0, 2].pie(nb_Caloric, labels=labels, autopct='%1.1f%%')

No=obesity[obesity['CAEC']=='no']
Sometimes=obesity[obesity['CAEC']=='Sometimes']
Frequently=obesity[obesity['CAEC']=='Frequently']
Always=obesity[obesity['CAEC']=='Always']
labels = ["Don't eat between meals", 'Sometimes eat between meals', 'Frequently eat between meals', 'Always eat between meals']
Meals = [No, Sometimes, Frequently, Always]
nb_Meals = [len(x.index) for x in Meals]
axs[1, 2].pie(nb_Meals, labels=labels, autopct='%1.1f%%')

No=obesity[obesity['SMOKE']=='no']
Yes=obesity[obesity['SMOKE']=='yes']
labels = ['Smoke', "Don't smoke"]
Smoke = [Yes, No]
nb_Smoke = [len(x.index) for x in Smoke]
axs[1, 1].pie(nb_Smoke, labels=labels, autopct='%1.1f%%')


Yes =obesity[obesity['SCC']=='yes']
No =obesity[obesity['SCC']=='no']
labels= ['Count Calories',"Don't count calories"]
Count = [Yes, No]
nb_Count = [len(x.index) for x in Count]
axs[1, 0].pie(nb_Count, labels=labels, autopct='%1.1f%%')


No=obesity[obesity['CALC']=='no']
Sometimes=obesity[obesity['CALC']=='Sometimes']
Frequently=obesity[obesity['CALC']=='Frequently']
Always=obesity[obesity['CALC']=='Always']
labels = ["DOn't drink alcool", 'Sometimes drink alcool', 'Frequently drink alcool', 'Always drink alcool']
Alcool = [No, Sometimes, Frequently, Always]
nb_Alcool = [len(x.index) for x in Alcool]
axs[2, 0].pie(nb_Alcool, labels=labels, autopct='%1.1f%%')

Public=obesity[obesity['MTRANS']=='Public_Transportation']
Walking=obesity[obesity['MTRANS']=='Walking']
Auto=obesity[obesity['MTRANS']=='Automobile']
Moto=obesity[obesity['MTRANS']=='Motorbike']
Bike=obesity[obesity['MTRANS']=='Bike']
labels=['public_transport','walking','auto','moto','bike']
Transport=[Public,Walking,Auto,Moto,Bike]
nb_transport=[len(x.index) for x in Transport]
axs[2,1].pie(nb_transport,labels=labels,autopct='%1.1f%%')

Insufficient=obesity[obesity['NObeyesdad']=='Insufficient_Weight']
Normal=obesity[obesity['NObeyesdad']=='Normal_Weight']
Over_I=obesity[obesity['NObeyesdad']=='Overweight_Level_I']
Over_II=obesity[obesity['NObeyesdad']=='Overweight_Level_II']
Obes_I=obesity[obesity['NObeyesdad']=='Obesity_Type_I']
Obes_II=obesity[obesity['NObeyesdad']=='Obesity_Type_II']
Obes_III=obesity[obesity['NObeyesdad']=='Obesity_Type_III']
labels=['Insufficient','Normal','over_I','over_II','obesity_I','obesity_II','obesity_III']
shape=[Insufficient,Normal,Over_I,Over_II,Obes_I,Obes_II,Obes_III]
nb_shape=[len(x.index) for x in shape]
axs[2,2].pie(nb_shape,labels=labels,autopct='%1.1f%%')


st.pyplot(fig)

st.write("Visualisation des données non-numériques")