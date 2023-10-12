"""

if option_priority =='Ticket priority':
    select_ticket_priority = st.sidebar.selectbox('select priority',ticket_df['Priority'].unique().tolist())
    btn1 =st.sidebar.button('find priority tickets')

    if btn1:
        load_ticket_priority(select_ticket_priority)

elif option_year =='Ticket year':
    select_ticket_year = st.sidebar.selectbox('select year',ticket_df['Date / Time'].dt.year.unique().tolist())
    btn2 =st.sidebar.button('find  Tickets date')

    if btn2:
        load_ticket_year(select_ticket_year)


else option_issue_type =='Ticket Issue Type':
    select_ticket_issue_type = st.sidebar.selectbox('select issue type',ticket_df['Issue Type'].unique().tolist())
    btn3 =st.sidebar.button('find  issue type')

    if btn3:
        load_ticket_issue_type(select_ticket_issue_type)


#elif option =='Ticket Assignee':
#    select_ticket_assignee = st.sidebar.selectbox('select Assignee',ticket_df['Assignee'].unique().tolist())
#    btn4 =st.sidebar.button('find  Assignee')

#   if btn4:
#        load_ticket_assignee(select_ticket_assignee)
        


# use diff col to display these matrix in the columns
    col1,col2=st.columns(2)
    
    with col1:
        total_count=ticket_df[(ticket_df['Priority']==select_ticket_priority)].count().values[0]
        st.metric('Total count',total_count)
        print(total_count)
    
    with col2:
        st.metric('revenue','rs 3L','3%')
 
 def load_overall_analysis():
    st.title('overall analysis')
"""