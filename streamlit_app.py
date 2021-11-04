import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
import pickle



st.set_page_config(layout="wide")





	
def main():
	
	quest = st.sidebar.selectbox('Select a question:', [None]+['Question 1','Question 2','Question 3'])
	
	if quest=='Question 1':
	
		st.title('Which crises show a deterioration in severity, as measured by the INFORM Severity Index, during the last 18 months?')
		
		crisis = pd.read_csv('crisis.csv',sep='\t',index_col=0)
		dico_crisis=pickle.load( open( "dico_crisis.p", "rb" ) )
		all_increase=pickle.load( open("all_increase.p", "rb" ) )
		lastmonths_increase=pickle.load( open("6months_increase.p", "rb" ) )
		allmonths_increase=pickle.load( open("18months_increase.p", "rb" ) )
		
		st.subheader('Methodology')
		st.write('I calculated the linear coefficient over the last 18 months and over the last 6 months which I ponderate with the squared mean level of the crisis to give more weight to severe crisis as a 0.1 increase is not the same for a 4.0 crisis than for a 1.0 crisis')
		st.write('I selected after visualisation of the distribution of the linear coefficient the crisis with a score over 0.5 for at least one of each category. I then made 3 categories')
		st.write('')
		st.write('The result are:')
		
		st.markdown("""---""")	
		
		col1, col2, col3 = st.columns([1,1,1])
		col1.write('Crisis with both an increase over the last 6 months and over the last 18 months')
		for i in all_increase:
			col1.caption(i)
		col2.write('Crisis with a special deterioration over the last 6 months')
		for i in lastmonths_increase:
			col2.caption(i)
		col3.write('Crisis with both an increase over the last 6 months and over the last 18 months')
		for i in allmonths_increase:
			col3.caption(i)
		
		st.markdown("""---""")	
		
		
		st.write('The evolutions can be visualized below:')
		st.caption('Note: for months for which no INFORM Severity Index was available we used the last one that was available')
		
		st.subheader('Crisis with both an increase over the last 6 months and over the last 18 months')
		
		crisis1=st.multiselect('Select which crisis you want to visualize', all_increase)
		
		fig = go.Figure()
		for crise in crisis1:
			fig.add_trace(go.Scatter(x=crisis.columns, y=crisis.loc[dico_crisis[crise]],mode='lines',name=crise))
		st.plotly_chart(fig,use_container_width=True)
		
		st.subheader('Crisis with a special deterioration over the last 6 months')
		
		crisis2=st.multiselect('Select which crisis you want to visualize', lastmonths_increase)
		
		fig = go.Figure()
		for crise in crisis2:
			fig.add_trace(go.Scatter(x=crisis.columns, y=crisis.loc[dico_crisis[crise]],mode='lines',name=crise))
		st.plotly_chart(fig,use_container_width=True)
		
		st.subheader('Crisis with an increase over the last 18 months but quite stable since the last 6 months')
		
		crisis3=st.multiselect('Select which crisis you want to visualize', allmonths_increase)
		
		fig = go.Figure()
		for crise in crisis3:
			fig.add_trace(go.Scatter(x=crisis.columns, y=crisis.loc[dico_crisis[crise]],mode='lines',name=crise))
		st.plotly_chart(fig,use_container_width=True)
		
		
		st.subheader('Other crisis (No significant deterioration)')
		
		crisis4=st.multiselect('Select which crisis you want to visualize', [i for i in dico_crisis if i not in all_increase+lastmonths_increase+\
		allmonths_increase])
		
		fig = go.Figure()
		for crise in crisis4:
			fig.add_trace(go.Scatter(x=crisis.columns, y=crisis.loc[dico_crisis[crise]],mode='lines',name=crise))
		st.plotly_chart(fig,use_container_width=True)
	
	elif quest=='Question 3':
		
		data=pd.read_csv('correlation.csv',sep='\t',index_col=None)
		
		st.title('Is there a correlation between the severity of a crisis, as measured by the INFORM Severity Index, and the humanitarian access score?')
		
		st.subheader('Methodology')
		st.write('For each months and crisis over the last 18 months I collected Inform Severity Index and Humanitarian Access Score.')
		st.write('The calculation of the pearson coefficient gave a value of 0.673 which represent a low correlation between the two variables')
		st.write('With a scater plot diagram whose size of points represents the number of occurence for each points we get this:')
		
		fig = px.scatter(data, x="ACCESS", y="INFORM Severity Index", size='crisis_id', hover_data=['crisis_id'])
		st.plotly_chart(fig,use_container_width=True)
		
		st.write('')
		
		st.write('So we see that the inform severity index tends to increase with the humanitarian access score')
		st.write('What we see is that a high humanitarian access score usualy means a high inform severity index however the it does not work the other way. We can have high inform severity index despite very low access score.')
		st.write('This makes perfectly sense as we have plenty of example of crisis where INGO can access with few or no constraints despite serious humanitarian crisis (From my personal field experience: CAR, Chad, flood in Pakistan, Ivory Coast for example). However usualy when the access is difficult or impossible it is quite frequent that the humanitarian crisis is very much worrying (From my personal field experience: Central Somalia and some places in Myanmar)')
	


if __name__== '__main__':
    main()
