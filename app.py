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

        
# *********************************************************************************************

#----------------------------------------   PRIORITY ANALYSIS  -----------------------------

# *********************************************************************************************

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
    

    

#------------------------------------------------------------------------------------------------
#  *******************************     year wise analysis   **************************************
#-------------------------------------------------------------------------------------------------

    st.subheader('YEAR WISE ANALYSIS')
    #st.selectbox('select year',ticket_df['year'].unique().tolist())
    
    selected_option=st.selectbox('Select year',ticket_df['Date / Time'].dt.year.unique().tolist())

    # year line chart 
    year_wise_line_chart = ticket_df[ticket_df['year']==selected_option].groupby('YearMonth')['Ticket No'].count()
    # line chart

    year_wise_line_chart=pd.DataFrame(year_wise_line_chart)
    #year_line_chart.set_index('YearMonth', inplace=True)
    st.title('Line Chart of Counts by YearMonth')
    st.line_chart(year_wise_line_chart)


    


    status_count_per_year=ticket_df[ticket_df['year']==selected_option].groupby('Status')['Ticket No'].count()

    col3,col4 = st.columns(2)
    with col3:
        st.title('year wise status')
        fig3,ax3=plt.subplots(figsize=(2, 2))
        ax3.pie(status_count_per_year,labels=status_count_per_year.index,autopct="%0.01f%%",radius=1, textprops={'fontsize': 5})
        st.pyplot(fig3)

    with col4:
        # delay histogram
        year_wise_Delay_hist= ticket_df[ticket_df['year']==selected_option].groupby('Category')['dealay_days'].count()
        # Create a histogram with 20 bins
        year_wise_Delay_hist=pd.DataFrame(year_wise_Delay_hist)
        #ticket_hist = ticket_hist.set_index('Category')
        st.title('Year wise delay ')
        st.bar_chart(year_wise_Delay_hist)


# ***********************************************************************************************
# ***********************************************************************************************
# ***********************************************************************************************
# ***********************************************************************************************
# --------------------- NOT USING ABOVE CODE IN THIS VISULAIZATION -----------------------------
# ***********************************************************************************************
# ***********************************************************************************************
# ***********************************************************************************************
# ***********************************************************************************************
# ***********************************************************************************************
# ***********************************************************************************************




# ***********************************************************************************************

# ***************************       'DROPDOWN ANALYSIS'        ***********************************

# ***********************************************************************************************





def load_dropdown_analysis(option_year,option_issue_type):
    st.title('Ticket  Analysis')

    #st.subheader('DROPDOWN ANALYSIS')
    #**********************************************************************************************
    st.subheader('Year wise metric')
    total_ticket_2021=ticket_df[ticket_df['year']==2021].count().values[0]
    total_ticket_2022=ticket_df[ticket_df['year']==2022].count().values[0]
    total_ticket_2023=ticket_df[ticket_df['year']==2023].count().values[0]

    col1,col2,col3=st.columns(3)
    with col1:
        st.metric('2021',str(round(total_ticket_2021)))

    with col2:
        st.metric('2022',str(round(total_ticket_2022)))

    with col3:
        st.metric('2023',str(round(total_ticket_2023)))


    #**********************************************************************************************
    st.header('')
    st.header('YEAR WISE ANALYSIS')
    st.header('')

    #**********************************************************************************************
    st.subheader('Priority metric')

    low_Priority=ticket_df[(ticket_df['Priority']=='Low') & (ticket_df['year'].isin(option_year))].count().values[0]

    medium_Priority=ticket_df[(ticket_df['Priority']=='Medium') & (ticket_df['year'].isin(option_year))].count().values[0]

    high_Priority=ticket_df[(ticket_df['Priority']=='High') & (ticket_df['year'].isin(option_year))].count().values[0]

    urgent_Priority=ticket_df[(ticket_df['Priority']=='Urgent') & (ticket_df['year'].isin(option_year))].count().values[0]


    col1,col2,col3,col4=st.columns(4)

    with col1:
        st.metric('Low',str(round(low_Priority)))

    with col2:
        st.metric('medium',str(round(medium_Priority)))

    with col3:
        st.metric('High',str(round(high_Priority)))

    with col4:
        st.metric('Urgent',str(round(urgent_Priority)))
   

    st.header('')


    # ***********************************************************************************************
        
    
    #print("status_wise_year_priority_issue_type_count",status_wise_year_priority_issue_type_count)

    # delay histogram and pie chart
    status_wise_year_count=ticket_df[ticket_df['year'].isin(option_year)].groupby('Status')['Ticket No'].count()


    col5,col6 = st.columns(2)

    with col5:
        
        
        st.markdown("**Year wise status**")
        st.write(' ')
        fig3,ax3=plt.subplots(figsize=(2, 2))
        ax3.pie(status_wise_year_count,labels=status_wise_year_count.index,autopct="%0.01f%%",radius=1, textprops={'fontsize': 5})
        st.pyplot(fig3)
        

    with col6:
        ticket_year_count=ticket_df[ticket_df['year'].isin(option_year)].groupby('year')['Ticket No'].count()
        # Create a histogram with 20 bins
        ticket_year_count=pd.DataFrame(ticket_year_count)
        #ticket_hist = ticket_hist.set_index('Category')
        st.markdown("**Ticket count per year**")
        st.bar_chart(ticket_year_count)
        

    # logic

    
    
   

    


#***********************************************************************************************

    # line chart

    #year_line_chart = ticket_df[ticket_df['year'].isin(option_year)].groupby('YearMonth')['Ticket No'].count()

    #year_line_chart=pd.DataFrame(year_line_chart)
    #year_line_chart.set_index('YearMonth', inplace=True)
    #st.title('Line Chart of Counts by YearMonth')
    #st.line_chart(year_line_chart)

#***********************************************************************************************
    
#***********************************************************************************************
    

    
    #***********************************************************************************************
    
    option=st.selectbox('select ',['Quater wise analysis','Priority wise analysis','Status wise analysis'])

    #******************************************************************************************
    
    #bar chart
    if option == 'Quater wise analysis':

        yr_qtr_bar_chart = ticket_df[ticket_df['year'].isin(option_year)].groupby('yr_qtr')['Ticket No'].count()

        yr_qtr_bar_chart=pd.DataFrame(yr_qtr_bar_chart)
        st.markdown("**Quater wise ticket count**")
        st.bar_chart(yr_qtr_bar_chart)


#***********************************************************************************************
  
# stacked bar chart   priority wise
    elif option == 'Priority wise analysis':

        qtr_wise_stacked_bar_chart=ticket_df[ticket_df['year'].isin(option_year)].groupby(['year','yr_qtr','Priority'])['Ticket No'].count()
        qtr_wise_stacked_bar_chart=pd.DataFrame(qtr_wise_stacked_bar_chart)
        qtr_wise_stacked_bar_chart=qtr_wise_stacked_bar_chart.reset_index()
    
        fig = px.bar(qtr_wise_stacked_bar_chart, x='yr_qtr', y='Ticket No', color='Priority',
                    labels={'Ticket No': 'Category Value'},
                    title=' Year wise Priority stacked Bar Chart ')
        
        # Add hover data for tooltips
        fig.update_traces(texttemplate='%{y}', textposition='outside')

        # Display the chart in Streamlit
        st.plotly_chart(fig)


#***********************************************************************************************
    # stacked bar chart status wise :  this will show year wise selected data
    else:

        qtr_wise_status_bar_chart=ticket_df[ticket_df['year'].isin(option_year)].groupby(['year','yr_qtr','Status'])['Ticket No'].count()
        qtr_wise_status_bar_chart=pd.DataFrame(qtr_wise_status_bar_chart)
        qtr_wise_status_bar_chart=qtr_wise_status_bar_chart.reset_index()
        color_map = {
        'Status1': 'black',
        'Status2': 'yellow',
        'Status3': 'green',
        # Add more colors for other Status categories as needed
    }
        
        fig1 = px.bar(qtr_wise_status_bar_chart, x='yr_qtr', y='Ticket No', color='Status',
                    labels={'Ticket No': 'Category Value'},
                    title='Year wise Status stacked Bar Chart ',
                    color_discrete_map=color_map)
        
        # Add hover data for tooltips
        fig1.update_traces(texttemplate='%{y}', textposition='outside')

        # Display the chart in Streamlit
        st.plotly_chart(fig1)
    



#***********************************************************************************************
    st.subheader('AS PER DROP DOWN ANALYSIS')
    st.header('')
#***********************************************************************************************


  
#*********************************************************************************************
  # status and priority selection
#*********************************************************************************************

    col20,col21 = st.columns(2)
    with col20:
        option_priority = st.multiselect('select priority',ticket_df['Priority'].unique().tolist())
    with col21:
        option_status = st.multiselect('select status',ticket_df['Status'].unique().tolist())
# stacked bar chart   drop down bases


    qtr_wise_priority_issue_stacked_bar_chart=ticket_df[ticket_df['year'].isin(option_year) & ticket_df['Priority'].isin(option_priority) & ticket_df['Issue Type'].isin(option_issue_type) & ticket_df['Status'].isin(option_status)].groupby(['year','yr_qtr','Priority'])['Ticket No'].count()
    qtr_wise_priority_issue_stacked_bar_chart=pd.DataFrame(qtr_wise_priority_issue_stacked_bar_chart)
    qtr_wise_priority_issue_stacked_bar_chart=qtr_wise_priority_issue_stacked_bar_chart.reset_index()

    fig = px.bar(qtr_wise_priority_issue_stacked_bar_chart, x='yr_qtr', y='Ticket No', color='Priority',
                labels={'Ticket No': 'Category Value'},
                title='Priority stacked Bar Chart ')
    

    # Add hover data for tooltips
    fig.update_traces(texttemplate='%{y}', textposition='outside')
   #Display the chart in Streamlit
    st.plotly_chart(fig)
 #***********************************************************************************************
    # stacked bar chart status wise

 #***********************************************************************************************
    
    qtr_wise_priority_issue_status_bar_chart=ticket_df[ticket_df['year'].isin(option_year) & ticket_df['Priority'].isin(option_priority) & ticket_df['Issue Type'].isin(option_issue_type) & ticket_df['Status'].isin(option_status)].groupby(['year','yr_qtr','Status'])['Ticket No'].count()
    qtr_wise_priority_issue_status_bar_chart=pd.DataFrame(qtr_wise_priority_issue_status_bar_chart)
    qtr_wise_priority_issue_status_bar_chart=qtr_wise_priority_issue_status_bar_chart.reset_index()
    color_map = {
        'Status1': 'black',
        'Status2': 'yellow',
        'Status3': 'green',
        # Add more colors for other Status categories as needed
    }
    fig1 = px.bar(qtr_wise_priority_issue_status_bar_chart, x='yr_qtr', y='Ticket No', color='Status',
                labels={'Ticket No': 'Category Value'},
                title='Status Stacked Bar Chart ',
                color_discrete_map=color_map)
    
    # Add hover data for tooltips
    fig1.update_traces(texttemplate='%{y}', textposition='outside')

    # Display the chart in Streamlit
    st.plotly_chart(fig1)


#***********************************************************************************************
    #stacked bar chart for delay timing
# **************************************************************************************************
    
    
    delay_day_count_category_wise=ticket_df[ticket_df['year'].isin(option_year) & ticket_df['Priority'].isin(option_priority) & ticket_df['Issue Type'].isin(option_issue_type)].groupby('Category')['dealay_days'].count()
    # year wise total status

    #delay

    ticket_hist= ticket_df[ticket_df['year'].isin(option_year) & ticket_df['Priority'].isin(option_priority) & ticket_df['Issue Type'].isin(option_issue_type) & ticket_df['Status'].isin(option_status)].groupby(['Category','Priority'])['dealay_days'].count()
    
    ticket_hist=pd.DataFrame(ticket_hist)
    #custom_order = ['No delay', 'Less than 6 days' , 'Less than 10 days','Less than 20 days','More than 20 days','In Process or Open']
    #ticket_hist = ticket_hist.loc[custom_order]
    ticket_hist=ticket_hist.reset_index()
        #ticket_hist
    #st.dataframe(ticket_hist)
        #ticket_hist = ticket_hist.set_index('Category')
    st.subheader('Ticket delay time')
        #st.bar_chart(ticket_hist)

    fig1 = px.bar(ticket_hist, x='Category', y='dealay_days', color='Priority',
            labels={'dealay_days': 'Category Value'},
            title='Delay Stacked Bar Chart as per priority')
    
        # Add hover data for tooltips
    fig1.update_traces(texttemplate='%{y}', textposition='outside')

        # Display the chart in Streamlit
    st.plotly_chart(fig1)
            
        


    #status_wise_year_priority_issue_type_count=ticket_df[ticket_df['year'].isin(option_year) & ticket_df['Priority'].isin(option_priority) & ticket_df['Issue Type'].isin(option_issue_type)].groupby('Status')['Ticket No'].count()
    #st.write(' status count')
    #fig6,ax6=plt.subplots(figsize=(2, 2))
    #ax6.pie(status_wise_year_priority_issue_type_count,labels=status_wise_year_priority_issue_type_count.index,autopct="%0.01f%%",radius=0.9, textprops={'fontsize': 5})
       
    #st.pyplot(fig6)


#**************************************************************************************************
   


     # dataframe
    st.title('Data frame')
    drop_down_data_csv=ticket_df[(ticket_df['Issue Type'].isin(option_issue_type))& (ticket_df['Priority'].isin(option_priority)) & (ticket_df['year'].isin(option_year)) & (ticket_df['Status'].isin(option_status))]
    drop_down_data_csv=drop_down_data_csv[['Ticket No','Date / Time','Department','Assignee','Priority','Issue Type','Issue Sub Type','Source','Status','Due Date','Resolve Date']]
    st.dataframe(drop_down_data_csv)

   

    # CSV Download button

    csv_data = drop_down_data_csv.to_csv().encode()
    st.download_button(
    label="Download CSV",
    data=csv_data,
    key="download-csv",
    file_name="data.csv",
    mime="text/csv",
    )
        







# ****************************************************************************************************

# begin from here




ticket_df=pd.read_csv(r"https://raw.githubusercontent.com/ratankj/streamlit_accen_tickets/main/ticket_df_new_csv.csv")
ticket_df['Date / Time'] = pd.to_datetime(ticket_df['Date / Time'])
ticket_df['Due Date'] = pd.to_datetime(ticket_df['Due Date'])
ticket_df['Resolve Date'] = pd.to_datetime(ticket_df['Resolve Date'])
ticket_df['year']=ticket_df['Date / Time'].dt.year
#ticket_df['year'] = ticket_df['year'].astype(str)
ticket_df['Status']=ticket_df['Status'].replace(['Closed'], 'Resolved')
ticket_df['dealay_days']=(ticket_df['Resolve Date'] - ticket_df['Due Date']).dt.days
ticket_df.loc[ticket_df['dealay_days'] < 1, 'dealay_days'] = 0
ticket_df['dealay_days'] = ticket_df['dealay_days'].fillna(-5)
ticket_df['Category']=ticket_df['dealay_days'].apply(lambda x: 
    '6  In Process or Open' if x == -5 else(
    '1  No delay' if x == 0 else(
    '2  Less than 6 days' if x < 5 else (
    '3  Less than 10 days' if x < 10 else (
    '4  Less than 20 days' if x < 21 else '5  More than 20 days')))))

ticket_df['YearMonth'] = ticket_df['Date / Time'].dt.strftime('%Y-%m')
#ticket_df['Year_new'] = pd.to_datetime(ticket_df['Date / Time'], format='%Y')
# Extract the quarter and create a new column
#ticket_df['Quarter'] = ticket_df['Year_new'].dt.quarter
#ticket_df['Quarter'] = ticket_df['Quarter'].astype(str)
#ticket_df['yr_qtr']=ticket_df['year']+ '-' +ticket_df['Quarter']
# Convert the 'Year' column to datetime objects

ticket_df['Year_new'] = pd.to_datetime(ticket_df['Date / Time'], format='%Y')
# Extract the year and quarter
ticket_df['Year_new'] = ticket_df['Year_new'].dt.year
#ticket_df['Quarter_new_new_check'] = ticket_df['Year_alpha'].index.to_series().add(1)
# Extract the quarter and create a new column
ticket_df['Quarter'] = ticket_df['Date / Time'].dt.quarter
# Create a custom function to format the year and quarter
ticket_df['Year_new_modification']=ticket_df['Year_new'].astype(str).str[-2:]
def format_year_quarter(row):
    return f"{row['Year_new_modification']}-Q{row['Quarter']}"

# Apply the custom function to create the 'YearQuarter' column
ticket_df['yr_qtr'] = ticket_df.apply(format_year_quarter, axis=1)




# *******************************************************************************************

# start from here

# *******************************************************************************************




st.sidebar.title('Accenture tickets')

st.sidebar.image('Électricité_de_France.svg.png')

#-------------------------------------------------------------------
#st.sidebar.header('drop down analysis')

#option=st.sidebar.selectbox('select ',['overall analysis','drop down analysis'])

#if option == 'overall analysis':   
#    load_overall_analysis()


#else:

option_year = st.sidebar.multiselect('select year',ticket_df['Date / Time'].dt.year.unique().tolist())

#option_priority = st.sidebar.multiselect('select priority',ticket_df['Priority'].unique().tolist())
#option_status = st.sidebar.multiselect('select status',ticket_df['Status'].unique().tolist())

option_issue_type = st.sidebar.multiselect('select issue type',ticket_df['Issue Type'].unique().tolist())

#btn1=st.sidebar.button('find ticket detail')


load_dropdown_analysis(option_year,option_issue_type)


# or 'option_priority' or 'option_issue_type'
# ,option_priority,option_issue_type