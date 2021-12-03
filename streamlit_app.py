import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt

from plotly.subplots import make_subplots


st.set_page_config(layout="wide")




	
def main():
	data=pd.read_csv('data.csv',sep='\t')
	data['persons']=np.ones(len(data))
	
	quest = st.sidebar.selectbox('Select what you want to do:', ['See some conclusions','Make some vizualizations'])
	
	if quest=='Make some vizualizations':
	
		st.title('Select some features you would like to see in the vizualisation')
		st.markdown("""---""")	
		features=st.multiselect('', [i for i in data if i!='persons'])
		if len(features)>1:
			fig=px.treemap(data, path=features,\
					 values='persons')
			fig.update_layout(title_text='Visualization of '+', '.join(features),font=dict(size=20))
			st.plotly_chart(fig,use_container_width=True)
		
	elif quest=='See some conclusions':					
		
		st.title('Some conclusions')
		
		st.markdown("""---""")				
		features=['Frequency respondant report handwhashing a day','data_collection_round']
		if len(features)>1:
			fig=px.treemap(data, path=features,\
					 values='persons')
			fig.update_layout(title_text='Visualization of '+', '.join(features),font=dict(size=20))
			st.plotly_chart(fig,use_container_width=True)
		st.subheader('Conlusion')
		st.write('People wash more often their hands after the end of the project')
		st.markdown("""---""")	
		
		
		
		
		
		
if __name__== '__main__':
    main()
