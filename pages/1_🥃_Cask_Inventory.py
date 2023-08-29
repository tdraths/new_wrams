import streamlit as st
from pyairtable import Api
import pandas as pd

# Access Airtable API here
api = Api('patMVlukgnFqZYWUn.66fec3a8abdcc8df0a767ce830d1589e60508a36c2d7d59ae3f50c1d910f4a32')

st.set_page_config(page_title='Cask Inventory', page_icon='🥃', layout='wide')

# Setting some custom Markdown CSS
st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

############ APP STRUCTURE STARTS HERE ############
step_1 = '<p style="font-family:Roboto; font-size: 36px;">Step 1</p>'
step_2 = '<p style="font-family:Roboto; font-size: 36px;">Step 2</p>'
step_3 = '<p style="font-family:Roboto; font-size: 36px;">Step 2</p>'

logo_col1, logo_col2, logo_col3 = st.columns([1,1,1])
with logo_col1:
    st.write("")
with logo_col2:
    st.image("WDOC_Logo_Black.jpg")
with logo_col3:
    st.write("")


st.title('Cask Inventory')

st.markdown(step_1, unsafe_allow_html=True)
# Selectbox options
option_0 = ''
option_1 = 'Add a Cask to the Inventory'
option_2 = 'View the Cask Inventory'

# Selectbox Label
st.subheader('Pick A Starting Point:')
option = st.selectbox(label='Step One Selection', options=[option_0,option_1, option_2], label_visibility='collapsed')

# Picking Option 0
if option == option_0:
    st.write('You gotta select an option bro')

# Picking Option 1...
if option == option_1:
    st.subheader('Enter Details Below')

    # Get Incoming Cask Details via User Input
    new_cask = st.form('cask number, pallet number, spirit type, cask type, fill date, bulk liters, ABV')

    # Entering Cask Number
    new_cask.subheader('What is the cask number?')
    cask_number = new_cask.text_input(label='cask number', value='', label_visibility='collapsed')

    # Entering Pallet Number
    new_cask.subheader('What is the pallet number?')
    pallet_number = new_cask.text_input(label='pallet number', value='', label_visibility='collapsed')

    # Entering Spirit Type
    new_cask.subheader('Enter Spirit Type')
    spirit_type = new_cask.selectbox(label='spirit type', options=['', 'New Make', 'Pot Still', 'Malt', 'Grain'], label_visibility='collapsed')

    # Entering Cask Type
    new_cask.subheader('Enter Cask Type')
    cask_type = new_cask.text_input(label='cask type', value='', label_visibility='collapsed')

    # Entering Fill Date


    # Entering Bulk Liters

    # Entering ABV

    submitted = new_cask.form_submit_button('COMPLETE NEW CASK ENTRY')

    # Show the cask entry data as entered
    if submitted:
        new_cask_df = pd.DataFrame(index=['New Cask Entry Data'])
        new_cask_df['Cask Number'] = cask_number
        new_cask_df['Pallet'] = pallet_number
        new_cask_df['Spirit Type'] = spirit_type
        new_cask_df['Cask Type'] = cask_type

        st.subheader('New Cask Data')
        st.dataframe(new_cask_df)

        confirmed = st.form('confirm details')
        confirmed.subheader("Confirm your cask details are correct and then hit 'Submit to Airtable' ")
        confirmed_submitted = confirmed.form_submit_button('SUBMIT TO AIRTABLE')
        if confirmed_submitted:
            # Create record dictionary for API
            api = Api('patMVlukgnFqZYWUn.66fec3a8abdcc8df0a767ce830d1589e60508a36c2d7d59ae3f50c1d910f4a32')

            base_id = 'appktvo1bXQDKvcCZ'
            table_id = 'tblV3Xyo7CcyWbNSg'
            cask_number_field_id = 'fldcKPvGO5CB9kUvp'
            cask_record = {
                cask_number_field_id: cask_number}
            
            # Access table
            cask_table = api.table(base_id, table_id)
            cask_table.create(cask_record)

            st.write(cask_table.all())