import streamlit as st
import pandas as pd
import plotly.express as px


from app.Functions.dataManagement import csvToPickleWithoutOutlier
from app.preProcessing.pre_processing import return_ds_balanced

ds_balanced = return_ds_balanced()

boxPlotBmi = px.box(ds_balanced, y="BMI")
boxPlotPH = px.box(ds_balanced, y="PhysicalHealth")
boxPlotMH = px.box(ds_balanced, y="MentalHealth")
boxPlotST = px.box(ds_balanced, y="SleepTime")


ds_balanced.to_csv('data/personal-key-indicators-of-heart-disease-dataset-balanced.csv')
ds_balanced_csv = pd.read_csv('data/personal-key-indicators-of-heart-disease-dataset-balanced.csv')

# Tratamento dos outlier
## Bmi
ds_balanced_csv['BMI'].where(ds_balanced['BMI'] <= 40, 27.78, inplace=True)
ds_balanced_csv['BMI'].where(ds_balanced['BMI'] >= 14.7, 14.7, inplace=True)
## PhysicalHealth
ds_balanced_csv['PhysicalHealth'].where(ds_balanced['PhysicalHealth'] <= 12, 12, inplace=True)
## MentalHealth
ds_balanced_csv['MentalHealth'].where(ds_balanced['MentalHealth'] <= 7, 7, inplace=True)
## SleepTime
ds_balanced_csv['SleepTime'].where(ds_balanced['SleepTime'] <= 11, 7, inplace=True)
ds_balanced_csv['SleepTime'].where(ds_balanced['SleepTime'] >= 3, 3, inplace=True)

# BoxPlot
boxPlot_Bmi_outlier_treatment = px.box(ds_balanced_csv, y="BMI")
boxPlot_PH_outlier_treatment = px.box(ds_balanced_csv, y="PhysicalHealth")
boxPlot_MH_outlier_treatment = px.box(ds_balanced_csv, y="MentalHealth")
boxPlot_ST_outlier_treatment = px.box(ds_balanced_csv, y="SleepTime")

csvToPickleWithoutOutlier(ds_balanced_csv, 'heartDiseaseWithoutOutlier')

def outlier():
  st.markdown("#### Visão geral do dataset balanceado 50% heartDisease yes e no")
  st.write(ds_balanced.head(10))

  st.markdown("#### Analisando os outlier das variáveis númericas")
  row1_space1, row1_space2, row1_space3 = st.columns(3)
  with row1_space1:
    st.plotly_chart(boxPlotBmi)
  with row1_space2:
    st.plotly_chart(boxPlotPH)
  with row1_space3:
    st.plotly_chart(boxPlotMH)
  st.plotly_chart(boxPlotST)

  st.markdown("#### Tratando os outlier")
  row2_space1, row2_space2, row2_space3 = st.columns(3)
  with row2_space1:
    st.plotly_chart(boxPlot_Bmi_outlier_treatment)
  with row2_space2:
    st.plotly_chart(boxPlot_PH_outlier_treatment)
  with row2_space3:
    st.plotly_chart(boxPlot_MH_outlier_treatment)
  st.plotly_chart(boxPlot_ST_outlier_treatment)