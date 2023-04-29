#!/usr/bin/env python
# coding: utf-8
# %%

# %%


import pandas as pd
import getpass
import os
import warnings
warnings.simplefilter("ignore")
import logging
import datetime
import shutil
import time
from GRFE_COUNTRY_SPECIFIC_RULES_3 import APPLY_COUNTRY_RULES,COUNTRY_RULES
from pyarrow import csv, parquet
user_id = getpass.getuser()


# %%
GRFE_DF = pd.read_excel(r"C:\\Users\\"+str(user_id)+"\\Desktop\\Retailer_KPI_dashboard_phase1\\HARMONIZATION_FOLDER\\GRFE_SIRVAL_Harmonization.xlsx",sheet_name=0)


# %%
GRFE_TIER_DF_2 = GRFE_DF[GRFE_DF['TIER'] == 'Tier 4'] 


# %%
GRFE_TIER_DF_3= GRFE_TIER_DF_2[['RE_EDD_name',
 'TIER']]                     


# %%
GRFE_TIER_DF_3.rename(columns = {'RE_EDD_name':'RETAILER NAME'}, inplace = True)


# %%
GRFE_TIER_DF_3 = GRFE_TIER_DF_3.drop_duplicates(subset='RETAILER NAME', keep="first")


# %%
SIRVAL_DF = pd.read_excel(r"C:\\Users\\"+str(user_id)+"\\Desktop\\Retailer_KPI_dashboard_phase1\\HARMONIZATION_FOLDER\\GRFE_SIRVAL_Harmonization.xlsx",sheet_name=1)


# %%
SIRVAL_TIER_DF_1 = SIRVAL_DF[SIRVAL_DF['TIER'] == 'Tier 1'] 


# %%
SIRVAL_TIER_DF_2= SIRVAL_TIER_DF_1[['RE_EDD_name',
 'TIER']]   


# %%
SIRVAL_TIER_DF_2.rename(columns = {'RE_EDD_name':'RETAILER NAME'}, inplace = True)


# %%
SIRVAL_TIER_DF_2 = SIRVAL_TIER_DF_2.drop_duplicates(subset='RETAILER NAME', keep="first")


# %%
Tier1_retailers = GRFE_TIER_DF_3.append(SIRVAL_TIER_DF_2, ignore_index=True)


# %%
Tier1_retailers = Tier1_retailers.drop_duplicates(subset='RETAILER NAME', keep="first")


# %%
Tier1_retailers.to_excel(r"C:\\Users\\"+str(user_id)+"\\Desktop\\Retailer_KPI_dashboard_phase1\\Tier1_retailers.xlsx",index=False) 

