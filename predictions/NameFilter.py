
# coding: utf-8

# In[1]:



import pandas as pd
import numpy as np


def clean_names():
# In[2]:


    pd.set_option('display.max_colwidth', -1)
    df = pd.read_csv("predictions/predictions.csv")
    
    
    # In[3]:
    
    
    def name_filter(nome):
        nome = nome.split()
        nome_final = ' '.join(
            [
                word.upper() for word in nome 
                     if word.replace('(', '').replace(')', '').replace(',', '').replace('.', '').lower()
                            in ['ventilador', 'artificial', 'artificiais', 
                                'pulmonar', 'mecanico', 'microprocessado', 'mecânico', 
                                'ventiladores', 'pulmonares', 'respiradores'
                               ]
            ])
    
        return nome_final
    
    df_filtered = df.copy()
    df_filtered['nome_original'] = df['nome']
    df_filtered['nome'] = df['nome'].apply(name_filter)
    
    
    # In[4]:
    
    
    df_filtered.head()
    
    
    # In[5]:
    
    
    df_filtered = df_filtered[df_filtered['nome'] != ""]
    df_filtered.head()
    
    
    # In[6]:
    
    
    df_filtered.to_csv("predictions/predictions.csv", index=False)
    
