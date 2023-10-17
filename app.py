import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px


st.set_page_config(layout='wide',page_title='Ticket Analysis')
#ticket_df['year']=ticket_df['Date / Time'].dt.year
st.set_option('deprecation.showPyplotGlobalUse', False)



# *******************************   Ticket priority ******************************************




#1. Priority
#    a. low
#    b. medium
#    c. high
#    d. urgent
#
#    - total no. of ticket as per priority
#    - no of ticket closed , open, inprocess
#    - no. of ticket closed on time and no. of ticket not closed on tiime
#    - diplay the csv if still ticket is still open


def load_overall_analysis():
    

    st.header('OVERALL ANALYSIS')

    st.subheader('PRIORITY ANALYSIS')

    low_Priority=ticket_df[ticket_df['Priority']=='Low'].count().values[0]

    medium_Priority=ticket_df[ticket_df['Priority']=='Medium'].count().values[0]

    high_Priority=ticket_df[ticket_df['Priority']=='High'].count().values[0]

    urgent_Priority=ticket_df[ticket_df['Priority']=='Urgent'].count().values[0]


    col1,col2,col3,col4=st.columns(4)

    with col1:
        st.metric('Low',str(round(low_Priority)))

    with col2:
        st.metric('medium',str(round(medium_Priority)))

    with col3:
        st.metric('High',str(round(high_Priority)))

    with col4:
        st.metric('Urgent',str(round(urgent_Priority)))


    col1,col2=st.columns(2)
    
    priority_analysis=ticket_df.groupby('Priority')['Ticket No'].count().sort_values(ascending=False)
    

    
    with col1:
        fig1,ax1=plt.subplots(figsize=(2, 3))
        ax1.pie(priority_analysis,labels=priority_analysis.index,autopct="%0.01f%%",radius=1, textprops={'fontsize': 5})
        st.pyplot(fig1)


    
    with col2:
         # Group the data by year and category
        grouped_data = ticket_df.groupby(['year','Priority'])['Ticket No'].count().unstack()
        grouped_data.plot(kind='bar', stacked=True, figsize=(8, 6))

        # Customize the chart (add labels, title, etc.)
        plt.xlabel('Year')
        plt.ylabel('Value')
        plt.title('Stacked Bar Chart of Categories by Year')

        

        # Display the plot in Streamlit
        st.pyplot()

#------------------------------------------------------------------------------

        
    # Sample data
    data = {
        'Year': ['2021', '2021', '2021', '2021', '2022', '2022', '2022', '2022', '2023', '2023', '2023', '2023'],
        'Category': ['low', 'medium', 'high', 'urgent'] * 3,
        'Value': [6, 33, 36, 4, 31, 14, 64, 34, 137, 94, 15, 15]
    }

    # Create a DataFrame from the data
    df = pd.DataFrame(data)
    #df=ticket_df.groupby(['year','Priority'])['Ticket No'].count().unstack()

    # Create a stacked bar chart using Plotly
    fig = px.bar(df, x='Year', y='Value', color='Category',
                labels={'Value': 'Category Value'},
                title='Stacked Bar Chart of Categories by Year')

    # Add hover data for tooltips
    fig.update_traces(texttemplate='%{y}', textposition='outside')

    # Display the chart in Streamlit
    st.plotly_chart(fig)
    


    
    low_Priority_status= ticket_df[ticket_df['Priority']=='Low'].groupby('Status')['Ticket No'].count()
    medium_Priority_status= ticket_df[ticket_df['Priority']=='Medium'].groupby('Status')['Ticket No'].count()
    high_Priority_status= ticket_df[ticket_df['Priority']=='High'].groupby('Status')['Ticket No'].count()
    urgent_Priority_status= ticket_df[ticket_df['Priority']=='Urgent'].groupby('Status')['Ticket No'].count()


    col1,col2 = st.columns(2)

    with col1:
        fig1,ax1=plt.subplots(figsize=(2, 2))
        #fig1.set_facecolor('black')
        ax1.pie(low_Priority_status,labels=low_Priority_status.index,autopct="%0.01f%%",radius=1, textprops={'fontsize': 5})
        plt.xlabel('Low Priority')
        st.pyplot(fig1)

    with col2:
        fig2,ax2=plt.subplots(figsize=(2, 2))
        ax2.pie(medium_Priority_status,labels=medium_Priority_status.index,autopct="%0.01f%%",radius=1, textprops={'fontsize': 5})
        plt.xlabel('Medium Priority')
        st.pyplot(fig2)



    col3,col4 = st.columns(2)
    with col3:
        fig3,ax3=plt.subplots(figsize=(2, 2))
        ax3.pie(high_Priority_status,labels=high_Priority_status.index,autopct="%0.01f%%",radius=1, textprops={'fontsize': 5})
        plt.xlabel('High Priority')
        st.pyplot(fig3)


    with col4:
        fig4,ax4=plt.subplots(figsize=(2, 2))
        ax4.pie(urgent_Priority_status,labels=urgent_Priority_status.index,autopct="%0.01f%%",radius=1, textprops={'fontsize': 5})
        plt.xlabel('Urgent Priority')
        st.pyplot(fig4)
        
    
# *********************************************************************************************

#----------------------------------------   ISSUE TYPE ANALYSIS  -----------------------------

# *********************************************************************************************


    st.header('ISSUE TYPE ANALYSIS')


    # dropdown
    issue_type_analysis_year_wise =st.selectbox('select issue type',ticket_df['Issue Type'].unique().tolist())


    issue_type_analysis=ticket_df.groupby('Issue Type')['year'].count().sort_values(ascending=False)

    # this is issue type year wise code
    issue_type_year_wise=ticket_df[ticket_df['Issue Type']==issue_type_analysis_year_wise].groupby('year')['Ticket No'].count()
    
    # this is issue type status wise code
    issue_type_status_wise=ticket_df[ticket_df['Issue Type']==issue_type_analysis_year_wise].groupby('Status')['Ticket No'].count()




    col4,col5 = st.columns(2)
    
    with col4:
        fig9,ax9=plt.subplots()    
        colors = ['red', 'green', 'blue', 'orange']
        bars = ax9.bar(issue_type_year_wise.index,issue_type_year_wise.values,color=colors)
        plt.xticks(rotation='vertical')

        for bar in bars:
            height = bar.get_height()
            ax9.annotate(f'{height}', xy=(bar.get_x() + bar.get_width() / 2, height), xytext=(0, 3),
                        textcoords="offset points", ha='center', va='bottom')

            # Display the plot in Streamlit
        st.pyplot(fig9)
    
    with col5:
        fig10,ax10=plt.subplots(figsize=(2, 3))
        ax10.pie(issue_type_status_wise,labels=issue_type_status_wise.index,autopct="%0.01f%%",radius=0.8, textprops={'fontsize': 5})
        st.pyplot(fig10)
        

    # if it is open then dataframe 


    issue_type_status_wise_open_on_process=ticket_df[(ticket_df['Issue Type']==issue_type_analysis_year_wise)  & ((ticket_df['Status']=='Open') | (ticket_df['Status']=='In Process')) ]

    st.dataframe(issue_type_status_wise_open_on_process)
    

    

#--------------------------

#--------------------------------------

    st.subheader('YEAR WISE ANALYSIS')
    #st.selectbox('select year',ticket_df['year'].unique().tolist())
    selected_option=st.selectbox('Select year',ticket_df['Date / Time'].dt.year.unique().tolist())

    if selected_option =='Total':
        col1,col2=st.columns(2)

        with col1:
            st.metric('revenue','rs 3L','3%')
           
        
        with col2:
            st.metric('revenue','rs 3L','3%')


# ***********************************************************************************************

# ***************************       'DROPDOWN ANALYSIS'        ***********************************

# ***********************************************************************************************


def load_dropdown_analysis(option_year,option_priority,option_issue_type):
    st.title('Ticket  Analysis')

    st.subheader('DROPDOWN ANALYSIS')

    

    #print('asdf:', option_issue_type, option_priority)
    drop_down_analysis=ticket_df[(ticket_df['Issue Type'].isin(option_issue_type))& (ticket_df['Priority'].isin(option_priority)) & (ticket_df['year'].isin(option_year))]

    st.dataframe(drop_down_analysis)


    # *********************************  logic  *****************************************************

    status_wise_year_count=ticket_df[ticket_df['year'].isin(option_year)].groupby('Status')['Ticket No'].count()
    status_wise_year_priority_issue_type_count=ticket_df[ticket_df['year'].isin(option_year) & ticket_df['Priority'].isin(option_priority) & ticket_df['Issue Type'].isin(option_issue_type)].groupby('Status')['Ticket No'].count()
    delay_day_count_category_wise=ticket_df[ticket_df['year'].isin(option_year) & ticket_df['Priority'].isin(option_priority) & ticket_df['Issue Type'].isin(option_issue_type)].groupby('Category')['dealay_days'].count()
    # year wise total status

    col3,col4 = st.columns(2)
    with col3:
        st.title('year wise status')
        fig3,ax3=plt.subplots(figsize=(2, 2))
        ax3.pie(status_wise_year_count,labels=status_wise_year_count.index,autopct="%0.01f%%",radius=1, textprops={'fontsize': 5})
        st.pyplot(fig3)


    with col4:
        # Sample data

        st.title(' status count')
        fig6,ax6=plt.subplots(figsize=(2, 2))
        ax6.pie(status_wise_year_priority_issue_type_count,labels=status_wise_year_priority_issue_type_count.index,autopct="%0.01f%%",radius=1, textprops={'fontsize': 5})
       
        st.pyplot(fig6)

        
    
    #print("status_wise_year_priority_issue_type_count",status_wise_year_priority_issue_type_count)


    col5,col6 = st.columns(2)

    with col5:
        ticket_hist= ticket_df[ticket_df['year'].isin(option_year) & ticket_df['Priority'].isin(option_priority) & ticket_df['Issue Type'].isin(option_issue_type)].groupby('Category')['dealay_days'].count()
        # Create a histogram with 20 bins
        ticket_hist=pd.DataFrame(ticket_hist)
        #ticket_hist = ticket_hist.set_index('Category')
        st.title('Ticket delay time')
        st.bar_chart(ticket_hist)
        

    with col6:
        st.title(' Delay count')
        fig7,ax7=plt.subplots(figsize=(2, 2))
        ax7.pie(delay_day_count_category_wise,labels=delay_day_count_category_wise.index,autopct="%0.01f%%",radius=1, textprops={'fontsize': 5})
       
        st.pyplot(fig7)
        

    # logic

    ticket_year_count=ticket_df[ticket_df['year'].isin(option_year)].groupby('year')['Ticket No'].count()


    col7,col8 = st.columns(2)
    with col7:
        st.metric('revenue','rs 3L','3%')

    with col8:
        
        # Create a histogram with 20 bins
        ticket_year_count=pd.DataFrame(ticket_year_count)
        #ticket_hist = ticket_hist.set_index('Category')
        st.title('Ticket year count')
        st.bar_chart(ticket_year_count)
    

        







# ****************************************************************************************************

# begin from here



ticket_df=pd.read_excel(r"C:\Users\Ratan Kumar Jha\Desktop\accenture_ticket\Accenture tickets.xlsx")
ticket_df['year']=ticket_df['Date / Time'].dt.year
ticket_df['Status']=ticket_df['Status'].replace(['Closed'], 'Resolved')
ticket_df['dealay_days']=(ticket_df['Resolve Date'] - ticket_df['Due Date']).dt.days
ticket_df.loc[ticket_df['dealay_days'] < 1, 'dealay_days'] = 0
ticket_df['dealay_days'] = ticket_df['dealay_days'].fillna(-5)
ticket_df['Category']=ticket_df['dealay_days'].apply(lambda x: 
    'In Process or Open' if x == -5 else(
    'No delay' if x == 0 else(
    'less than 6 days' if x < 5 else (
    'less than 10 days' if x < 10 else (
    'less than 20 days' if x < 21 else 'more than 20 days')))))
#ticket_df['year'] = pd.to_datetime(ticket_df['year'])

st.sidebar.title('Accenture tickets')

st.sidebar.image('Électricité_de_France.svg.png')

#-------------------------------------------------------------------
#st.sidebar.header('drop down analysis')

option=st.sidebar.selectbox('select ',['overall analysis','drop down analysis'])

if option == 'overall analysis':   
    load_overall_analysis()


else:

    option_year = st.sidebar.multiselect('select year',ticket_df['Date / Time'].dt.year.unique().tolist())

    option_priority = st.sidebar.multiselect('select priority',ticket_df['Priority'].unique().tolist())

    option_issue_type = st.sidebar.multiselect('select issue type',ticket_df['Issue Type'].unique().tolist())

    btn1=st.sidebar.button('find ticket detail')

    if btn1:
        load_dropdown_analysis(option_year,option_priority,option_issue_type)


# or 'option_priority' or 'option_issue_type'
# ,option_priority,option_issue_type