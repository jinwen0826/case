#!/usr/bin/env python
# coding: utf-8

# ## Case 2 results using SQL Sever
# Jinwen Li
# ### 1.asked information
# SQL query codes can be found using the link:https://github.com/jinwen0826/case_study0409

# In[144]:


result=pd.DataFrame({'Year':['2017','2016','2015'],
                     'Trev_curr':['31417495.03','25730943.59','29036749.19'],
                     'Newcust_rev':['21769213.01','17206366.90','N/A'],
                     'Ecu_growth':['1123705.33','N/A','N/A'],
                     'Revlost_att':['16146518.63','20551216.15','N/A'],
                     'Ecu_revcurr':['9648282.02','8524576.69','N/A'],  
                     'Ec_revp':['8524576.69','N/A','N/A'],
                     'Totalc_curr':['249987','204646','231294'],
                     'Totalc_p':['204646','231294','N/A'],
                     'Number_new_cus':['173449','136891','N/A'],
                     'Number_lost_cus':['128108','163539','N/A']                    
                     
                    })
print(result)


# ### Notes:  
# 1.Trev_curr: Total revenue for the current year  
# 2.Newcust_rev: New Customer Revenue   
# 3.Ecu_growth: Existing Customer Growth  
# 4.Revlost_att:Revenue lost from attrition
# 5.Ecu_revcurr:Existing Customer Revenue Current Year  
# 6.Ec_revp:Existing Customer Revenue Prior Year  
# 7.Totalc_curr:Total Customers Current Year  
# 8.Totalc_p: Total Customers Previous Year  
# 9.Number_new_cus:New Customers  
# 10.Number_lost_cus:Lost Customers  

# #### 1.Total revenue for the current year
# --The total revenue for the current year(2017) is 31417495.0300001  
# --The total revenue for the current year(2016) is 25730943.5900001  
# --The total revenue for the current year(2015) is 29036749.19  
# 
# #### 2.New Customer Revenue 
# --New Customer Revenue for 2017 is 21769213.01, for 2016 is 17206366.9.  
# 
# #### 3.Existing Customer Growth
# -- Existing Customer Growth for year 2017 is 9648282.02000003-8524576.68999998= 1123705.33000005  
# -- For here, we can only calculate the Existing Customer Growth for year 2017 because we don't know the  
# -- existing revenue in year 2015, so we cannot get the Existing Customer Growth for 2016.  
# 
# #### 4. Revenue lost from attrition
# -- Here, we define the  Revenue lost from attrition is the customers who bought goods last year but don't buy  
# -- goods current year, and the lost is the value of goods they bought last year.  
# 
# --The revenue lost from attrition in 2017 is 16146518.63, in 2016 is 20551216.15.  
# 
# #### 5.Existing Customer Revenue Current Year
# -- The existing customer revenue for year 2017 is 9648282.02000002, and for year 2016 is 8524576.69.  
# 
# #### 6.Existing Customer Revenue Prior Year
# -- For year 2017, the prior year is 2016, and the 2016 existing customer revenue is 8524576.69.  
# 
# #### 7.Total Customers Current Year
#  --The total customers for current year 2017 is 249987，for year 2016 is 204646, for year 2015 is 231294.  
# 
# ####  8.Total Customers Previous Year
#  --For year 2017, the previous year is 2016, the total customers is 204646.  
#  -- for year 2016, the previous year is 2015, the total customers is 231294.  
# 

# #### 9.New Customers list
# for year 2017:  
# -- The total number of new customers for 2017 is 173449 and the top 10 of new customers is below.  
# 
# fuyjaexmoh@gmail.com  
# qvjfterwnk@gmail.com   
# uxilnjipqh@gmail.com  
# bcxekwoaor@gmail.com  
# zhlvymbfwx@gmail.com  
# fdkiioqtli@gmail.com  
# vcihdhamko@gmail.com  
# mqptqupwfa@gmail.com  
# zxdpwkylvf@gmail.com  
# vpsfdhgrfo@gmail.com   
# 
# for year 2016:
# -- The total number of new customers for 2016 is 136891 and the top 10 of new customers is below.  
# mwrossuukz@gmail.com  
# gkwsoupawk@gmail.com  
# vlyigtgfzs@gmail.com  
# yfirychuhk@gmail.com  
# trnzgqinuu@gmail.com  
# hhxxpwlakg@gmail.com  
# xshhioxkjs@gmail.com  
# xypcivocfw@gmail.com  
# hoyilazseb@gmail.com  
# dkbsemibna@gmail.com  
# 

# #### 10.Lost Customers list
# for year 2017:  
# -- for year 2017, the number of lost customers is 128108, and the top 10 of the lost customers is below.  
# 
# gkwsoupawk@gmail.com  
# trnzgqinuu@gmail.com  
# hhxxpwlakg@gmail.com  
# lfeafnigbu@gmail.com  
# cemerinvsn@gmail.com  
# wkgndosxgd@gmail.com  
# xshhioxkjs@gmail.com  
# ujelzbtqer@gmail.com  
# gmsayrrlrm@gmail.com  
# whnnmusxsc@gmail.com  
# 
# for year 2016:  
# -- for year 2016, the number of lost customers is 163539, and the top 10 of the lost customers is below.  
# 
# sxabypbfhj@gmail.com  
# cyksxkrbby@gmail.com  
# fosfxhsnqg@gmail.com  
# yuozotbyus@gmail.com  
# lrafxvxavj@gmail.com    
# zufomelpjp@gmail.com  
# ihvfzxfjyd@gmail.com  
# nhknapwsbx@gmail.com  
# irvstayzjd@gmail.com  
# jawkygcvwx@gmail.com  
# 
# 
# 

# ### 2.import data using python

# In[36]:


import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


# In[37]:


customers = pd.read_csv('casestudy.csv') #customers


# In[38]:


customers.head(10)


# ### Form 1
# From the form below，there is an interesting observation.We can see the mean of three years net revenue are all around 125, the minimum are all 1.0, the maximum of three years net revenue are all 250.
# 

# In[87]:


customers.groupby('year').net_revenue.agg(['sum', 'min', 'mean', 'max','median'])


# ### Plots 1
# From the plots below, we can see the distributions of net_revenue in three years are all very even. Thus, we can see  
# customers don't have any perferance about each price points.

# In[91]:


net_revenue2015=customers[customers.year==2015]['net_revenue']
plt.hist(net_revenue2015)
plt.title('2015 net revenue')


# In[92]:


net_revenue2016=customers[customers.year==2016]['net_revenue']
plt.hist(net_revenue2016)
plt.title('2016 net revenue')


# In[93]:


net_revenue2017=customers[customers.year==2017]['net_revenue']
plt.hist(net_revenue2017)
plt.title('2017 net revenue')


# ### Plots 2
# From the plots below,we can see the total net revenue and total customers of 2015-2017 , and we can see there is a tendency to go down and then up both on the total net revenue and total number of customers. 
# 
# From the second plot below, we can see there is a coincide on the plot, this is a very interesting thing.So each customer contributes the same amount of sales growth, as long as there is a customer increase, there will be a unit of sales growth.

# In[138]:


result['Trev_curr'] = result['Trev_curr'].astype(float, errors = 'raise')
total_revenue=result['Trev_curr']
result['Totalc_curr'] = result['Totalc_curr'].astype(float, errors = 'raise')
total_customers=result['Totalc_curr']
x=['2015','2016','2017']
y1=[total_revenue[2],total_revenue[1],total_revenue[0]]
plt.plot(x,y1,label='total revenue',color='b')
y2=[total_customers[2],total_customers[1],total_customers[0]]
plt.plot(x,y2,label ='total customers',color='r')
fig,ax1=plt.subplots()
ax2=ax1.twinx()
ax1.plot(x,y1,'b',linewidth='5',linestyle='--')
ax2.plot(x,y2,'r',linewidth='2')
ax1.set_ylabel('total revenue')
ax2.set_ylabel('total customers')
plt.title('2015-2017 total net revenue v.s. total customers')


# ### Plot 3
# From the plot below, we can see the new customer revenue is also increasing.

# In[142]:


x=['2016','2017']
y=[17206366.90,21769213.01]
plt.plot(x,y)
plt.title('2016-2017 new customer revenue')


# ### Plots 4
# From the plots below, the organe line represents the number of new customers, the blue one represents the number of lost customers. We can know, in 2016, the number of lost customers is bigger than the number of new customers, which is a bad thing. However, in 2017, the number of new customers is larger than the number of lost customers which is a good thing for the company.

# In[143]:


x=['2016','2017']
y1=[136891,173449]
plt.plot(x,y1,label='number of new_customers',color='orange')
y2=[163539,128108]
plt.plot(x,y2,label ='number of lost_customers',color='b')
fig,ax1=plt.subplots()
ax2=ax1.twinx()
ax1.plot(x,y1,'orange',linewidth='5',linestyle='--')
ax2.plot(x,y2,'b',linewidth='2')
ax1.set_ylabel('number of new_customers')
ax2.set_ylabel('number of lost_customers')
plt.title('2016-2017 number of new customers v.s. number of lost customers')


# In[ ]:




