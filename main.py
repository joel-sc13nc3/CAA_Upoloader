import pandas as pd
import streamlit as st

Loading_files=st.container()
Participants_list=st.container()

demo_upload=Loading_files.file_uploader("Please upload the demographics template", type={"csv", "txt"},key="demo")
wf2=Loading_files.file_uploader("Please upload the 2.WeeklyActivityBySeller csv file", type={"csv", "txt"},key="2.Weekly" )
wf3=Loading_files.file_uploader("Please upload the 3.WeeklyDomainCollabMetricsBySeller csv file", type={"csv", "txt"},key="2.Weekly" )
wf6=Loading_files.file_uploader("Please upload the 6.MonthlyManagerMetricsBySeller.csv csv file", type={"csv", "txt"},key="2.Weekly" )
wf3=Loading_files.file_uploader("Please upload the 8.TOTAL_WinRoom_Dashboard_Data csv file", type={"csv", "txt"},key="2.Weekly" )


if  wf2 is not None:
    df_wf2=pd.read_csv(wf2).astype("str")
    df_wf2_cols=["Meeting External time","Meeting Internal time","Email external time","Email internal time","Total internal time",
                 "Total external time","Total workweek time","Non-collaboration time","Meetings external","Emails external",
                 "Emails internal","Sales only meeting time","Sales only email time","Sales only meetings","Sales only emails",
                 "Total collaboration time","Single domain collaboration time","Multiple domain collaboration time",
                 "Total meaningful external participants","Total external participants","Multiple Domain Collaboration Time"]
    df_wf2=df_wf2[df_wf2_cols]



if  wf2 is not None:
    df_wf3=pd.read_csv(wf2).astype("str")

if  wf2 is not None:
    df_wf4=pd.read_csv(wf2).astype("str")

if  wf2 is not None:
    df_wf5=pd.read_csv(wf2).astype("str")






