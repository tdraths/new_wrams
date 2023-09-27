
# NEXT STEPS
# Add cost of spirit
# LPA cost vs bulk cost


# Importing Packages
import streamlit as st
import pandas as pd

# Some Page Configurations
st.set_page_config(page_title='Cutting & Blending Calculator', page_icon="⚗️", layout='wide')

# Setting some custom Markdown CSS
st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)


step_1 = '<p style="font-family:Roboto; font-size: 36px;">Step 1</p>'
step_2 = '<p style="font-family:Roboto; font-size: 36px;">Step 2</p>'

logo_col1, logo_col2, logo_col3 = st.columns([1,1,1])
with logo_col1:
    st.write("")
with logo_col2:
    st.image("WDOC_Logo_Black.jpg")
with logo_col3:
    st.write("")

# Global Variables
spirit_count = 0

perc_alc_1 = 0
perc_alc_2 = 0
perc_alc_3 = 0
perc_alc_4 = 0
perc_alc_5 = 0

vol_alc_1 = 0
vol_alc_2 = 0
vol_alc_3 = 0
vol_alc_4 = 0
vol_alc_5 = 0

abv_alc_1 = 0.0
abv_alc_2 = 0.0
abv_alc_3 = 0.0
abv_alc_4 = 0.0
abv_alc_5 = 0.0

water_required = 0.0


# Functions to Use
def get_blend(strong_alcohol_volume, strong_alcohol_abv, weak_alcohol_volume, weak_alcohol_abv):

    blend_volume = (strong_alcohol_volume + weak_alcohol_volume) - ((strong_alcohol_volume + weak_alcohol_volume)*.027)

    blend_abv = ((strong_alcohol_volume*strong_alcohol_abv) + (weak_alcohol_volume*weak_alcohol_abv)) / (strong_alcohol_volume + weak_alcohol_volume)

    return blend_volume, blend_abv

def get_water_requirement(starting_volume, starting_abv, target_abv):
    water_required = ((starting_volume*starting_abv) - (target_abv*starting_volume)) / target_abv
    return water_required

# New Step 2 Functions
def get_prelimVol(target_volume, quotient):
    pVol = target_volume + (quotient*target_volume)
    return pVol

def get_water_req(pVol, target_abv, starting_abv):
    water = pVol - (pVol*(target_abv / starting_abv))
    return water

def get_starting_volume(pVol, water):
    sVol = pVol - water
    return sVol
    

########## APP STRUCTURE STARTS HERE ##########

# App Title
st.title('Cutting & Blending Assistant')

# Step One - Setting the first blend specifics
st.markdown(step_1, unsafe_allow_html=True)

#Selectbox options
option_0 = ''
option_1 = 'Start with Number of Spirts, Starting Bulk Litres & Target ABV'
option_2 = 'Start with Number of Spirits, Target Bulk Litres & Target ABV'

# Selectbox Label
st.subheader('Pick A Starting Point:')

option = st.selectbox(label='Step One Selectioon', options=[option_0, option_1, option_2], label_visibility="collapsed")

# Picking Option 1...
if option == option_1:
    st.subheader('Enter Details Below')

    # Get Number of Spirits in Blend
    qty = st.form('spirit count, starting bulk, target abv')
    qty.subheader('How many spirits are in the blend')
    spirit_count = qty.slider(label='spirit count',min_value=1, max_value=5, step=1, label_visibility='collapsed')

    # Get Desired Total Blend Volume
    qty.subheader('Total Volume of Samples (mL or L):')
    total_volume = qty.number_input(label='total volume', min_value=0, max_value=5000, step=100, label_visibility='collapsed')

    # Get Desired Final Blend ABV
    qty.subheader('Desired Final Blended ABV %:')
    target_abv = qty.number_input(label='target abv', min_value=0.0, max_value=70.0, value=46.0, step=0.5, label_visibility='collapsed')

    # Step One Submit Button
    qty.form_submit_button('COMPLETE STEP ONE HERE')

if option == option_2:
    st.subheader('Enter Details Below')
    
    # Get Final Bulk Liters
    qty = st.form('target bulk, target abv, starting abv')
    qty.subheader("What's the target bulk volume (ml or L): ")
    target_volume = qty.number_input(label='target volume', min_value=0.0, step=100.0, label_visibility='collapsed')

    # Get Final ABV
    qty.subheader('Desired Final ABV %:')
    target_abv = qty.number_input(label='target abv', min_value=0.0, value=46.0, step=0.5, label_visibility='collapsed')

    # Get Starting ABV
    qty.subheader('Starting ABV %:')
    starting_abv = qty.number_input(label='starting abv', min_value=0.0, value=63.0, step=0.5, label_visibility='collapsed')

    # Step One Submit Button
    qty.form_submit_button('COMPLETE STEP ONE HERE')


# After Picking Option 1,  Step Two
st.markdown(step_2, unsafe_allow_html=True)
if option == option_1:
    st.subheader('Enter Blend Components')

    # Get Details of Each Spirit in Blend
    details = st.form('get_spirit_details')
    with details:
        # If the total number of spirits in the blend is 1
        if spirit_count == 1:
            with st.container():
                st.subheader('Spirit 1 Details')
                perc_alc_1 = 100.0

                #vol_alc_1 = st.number_input('Spirit volume in mL or L:', min_value=1, max_value = 1000, value=500, step=1, key='vol_1')
                        
                name_alc_1 = st.text_input('Alcohol Name:', value="Single Malt", key='name_1')

                abv_alc_1 = st.number_input('Spirit ABV %:', value=63.0, step=0.05, key='abv_1')

                vol_alc_1 = total_volume*(perc_alc_1/100)

        # If the total number of spirits in the blend is 2
        if spirit_count == 2:
            col1, col2 = st.columns(2)
            with col1:
                st.subheader(' Spirit 1 Details')
                perc_alc_1 = st.number_input('Percent of overall volume of blend:', min_value=0.0, max_value=100.0, key='perc_alc_1')
                
                #vol_alc_1 = st.number_input('Spirit volume in mL or L:', min_value=1, max_value = 1000, value=500, step=1, key='vol_1')

                name_alc_1 = st.text_input('Alcohol Name:', value="Single Malt", key='name_1')
            
                abv_alc_1 = st.number_input('Spirit ABV %:', value=63.0, step=0.05, key='abv_1')

                vol_alc_1 = total_volume*(perc_alc_1/100)

            with col2:
                st.subheader('Spirit 2 Details')
                perc_alc_2 = st.number_input('Percent of overall volume of blend:', min_value=0.0, max_value=100.0, key='perc_alc_2')
                
                #vol_alc_2 = st.number_input('Spirit volume in mL or L:', min_value=1, max_value = 1000, value=500, step=1, key='vol_2')

                name_alc_2 = st.text_input('Alcohol Name:', value="Single Malt", key='name_2')
            
                abv_alc_2 = st.number_input('Spirit ABV %:', value=63.0, step=0.05, key='abv_2')

                vol_alc_2 = total_volume*(perc_alc_2/100)

        # If the total number of spirits in the blend is 3
        if spirit_count == 3:
            col1, col2, col3 = st.columns(3)
            with col1:
                st.subheader(' Spirit 1 Details')
                perc_alc_1 = st.number_input('Percent of overall volume of blend:', min_value=0.0, max_value=100.0, key='perc_alc_1')
                
                #vol_alc_1 = st.number_input('Spirit volume in mL or L:', min_value=1, max_value = 1000, value=500, step=1, key='vol_1')

                name_alc_1 = st.text_input('Alcohol Name:', value="Single Malt", key='name_1')
            
                abv_alc_1 = st.number_input('Spirit ABV %:', value=63.0, step=0.05, key='abv_1')

                vol_alc_1 = total_volume*(perc_alc_1/100)

            with col2:
                st.subheader('Spirit 2 Details')
                perc_alc_2 = st.number_input('Percent of overall volume of blend:', min_value=0.0, max_value=100.0, key='perc_alc_2')

                #vol_alc_2 = st.number_input('Spirit volume in mL or L:', min_value=1, max_value = 1000, value=500, step=1, key='vol_2')

                name_alc_2 = st.text_input('Alcohol Name:', value="Single Malt", key='name_2')
            
                abv_alc_2 = st.number_input('Spirit ABV %:', value=63.0, step=0.05, key='abv_2')

                vol_alc_2 = total_volume*(perc_alc_2/100)


            with col3:
                st.subheader('Spirit 3 Details')
                perc_alc_3 = st.number_input('Percent of overall volume of blend:', min_value=0.0, max_value=100.0, key='perc_alc_3')

                #vol_alc_3 = st.number_input('Spirit volume in mL or L:', min_value=1, max_value = 1000, value=500, step=1, key='vol_3')

                name_alc_3 = st.text_input('Alcohol Name:', value="Single Malt", key='name_3')
            
                abv_alc_3 = st.number_input('Spirit ABV %:', value=63.0, step=0.05, key='abv_3')

                vol_alc_3 = total_volume*(perc_alc_3/100)

        # If the total number of spirits in the blend is 4
        if spirit_count == 4:
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.subheader(' Spirit 1 Details')
                perc_alc_1 = st.number_input('Percent of overall volume of blend:', min_value=0.0, max_value=100.0, key='perc_alc_1')
                
                #vol_alc_1 = st.number_input('Spirit volume in mL or L:', min_value=1, max_value = 1000, value=500, step=1, key='vol_1')

                name_alc_1 = st.text_input('Alcohol Name:', value="Single Malt", key='name_1')
                
                abv_alc_1 = st.number_input('Spirit ABV %:', value=63.0, step=0.05, key='abv_1')

                vol_alc_1 = total_volume*(perc_alc_1/100)

            with col2:
                st.subheader('Spirit 2 Details')
                perc_alc_2 = st.number_input('Percent of overall volume of blend:', min_value=0.0, max_value=100.0, key='perc_alc_2')
                
                #vol_alc_2 = st.number_input('Spirit volume in mL or L:', min_value=1, max_value = 1000, value=500, step=1, key='vol_2')

                name_alc_2 = st.text_input('Alcohol Name:', value="Single Malt", key='name_2')
                
                abv_alc_2 = st.number_input('Spirit ABV %:', value=63.0, step=0.05, key='abv_2')

                vol_alc_2 = total_volume*(perc_alc_2/100)

            with col3:
                st.subheader('Spirit 3 Details')
                perc_alc_3 = st.number_input('Percent of overall volume of blend:', min_value=0.0, max_value=100.0, key='perc_alc_3')

                #vol_alc_3 = st.number_input('Spirit volume in mL or L:', min_value=1, max_value = 1000, value=500, step=1, key='vol_3')

                name_alc_3 = st.text_input('Alcohol Name:', value="Single Malt", key='name_3')
            
                abv_alc_3 = st.number_input('Spirit ABV %:', value=63.0, step=0.05, key='abv_3')

                vol_alc_3 = total_volume*(perc_alc_3/100)

            with col4:
                st.subheader('Spirit 4 Details')
                perc_alc_4 = st.number_input('Percent of overall volume of blend:', min_value=0.0, max_value=100.0, key='perc_alc_4')

                #vol_alc_4 = st.number_input('Spirit volume in mL or L:', min_value=1, max_value = 1000, value=500, step=1, key='vol_4')

                name_alc_4 = st.text_input('Alcohol Name:', value="Single Malt", key='name_4')
                
                abv_alc_4 = st.number_input('Spirit ABV %:', value=63.0, step=0.05, key='abv_4')

                vol_alc_4 = total_volume*(perc_alc_4/100)


        # If the total number of spirits in the blend is 5
        if spirit_count == 5:
            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                st.subheader(' Spirit 1 Details')
                perc_alc_1 = st.number_input('Percent of overall volume of blend:', min_value=0.0, max_value=100.0, key='perc_alc_1')
                
                #vol_alc_1 = st.number_input('Spirit volume in mL or L:', min_value=1, max_value = 1000, value=500, step=1, key='vol_1')

                name_alc_1 = st.text_input('Alcohol Name:', value="Single Malt", key='name_1')
                
                abv_alc_1 = st.number_input('Spirit ABV %:', value=63.0, step=0.05, key='abv_1')

                vol_alc_1 = total_volume*(perc_alc_1/100)

            with col2:
                st.subheader('Spirit 2 Details')
                perc_alc_2 = st.number_input('Percent of overall volume of blend:', min_value=0.0, max_value=100.0, key='perc_alc_2')
                
                #vol_alc_2 = st.number_input('Spirit volume in mL or L:', min_value=1, max_value = 1000, value=500, step=1, key='vol_2')

                name_alc_2 = st.text_input('Alcohol Name:', value="Single Malt", key='name_2')
                
                abv_alc_2 = st.number_input('Spirit ABV %:', value=63.0, step=0.05, key='abv_2')

                vol_alc_2 = total_volume*(perc_alc_2/100)

            with col3:
                st.subheader('Spirit 3 Details')
                perc_alc_3 = st.number_input('Percent of overall volume of blend:', min_value=0.0, max_value=100.0, key='perc_alc_3')

                #vol_alc_3 = st.number_input('Spirit volume in mL or L:', min_value=1, max_value = 1000, value=500, step=1, key='vol_3')

                name_alc_3 = st.text_input('Alcohol Name:', value="Single Malt", key='name_3')
            
                abv_alc_3 = st.number_input('Spirit ABV %:', value=63.0, step=0.05, key='abv_3')

                vol_alc_3 = total_volume*(perc_alc_3/100)

            with col4:
                st.subheader('Spirit 4 Details')
                perc_alc_4 = st.number_input('Percent of overall volume of blend:', min_value=0.0, max_value=100.0, key='perc_alc_4')

                #vol_alc_4 = st.number_input('Spirit volume in mL or L:', min_value=1, max_value = 1000, value=500, step=1, key='vol_4')

                name_alc_4 = st.text_input('Alcohol Name:', value="Single Malt", key='name_4')
                
                abv_alc_4 = st.number_input('Spirit ABV %:', value=63.0, step=0.05, key='abv_4')

                vol_alc_4 = total_volume*(perc_alc_4/100)

            with col5:
                st.subheader('Spirit 5 Details')
                perc_alc_5 = st.number_input('Percent of overall volume of blend:', min_value=0.0, max_value=100.0, key='perc_alc_5')

                #vol_alc_4 = st.number_input('Spirit volume in mL or L:', min_value=1, max_value=1000, value=500, step=1, key='vol_5')

                name_alc_5 = st.text_input('Alcohol Name:', value="Single Malt", key='name_5')

                abv_alc_5 = st.number_input('Spirit ABV%:', value=63.0, step=0.05, key='abv_5')

                vol_alc_5 = total_volume*(perc_alc_5/100)

    submitted = details.form_submit_button('COMPLETE STEP TWO HERE')


    if submitted:
        blended_df = pd.DataFrame(index=['Final Blend Numbers'])
        if spirit_count == 1:
            water_used = get_water_requirement(vol_alc_1, abv_alc_1, target_abv)

            components_df = pd.DataFrame(index=[name_alc_1])
            components_df['Alcohol Volume'] = vol_alc_1
            components_df['Alcohol ABV'] = abv_alc_1
            
            blend_volume = vol_alc_1
            blend_abv = abv_alc_1
            volume_after_dilution = vol_alc_1 + water_used
            volume_lost_to_contraction = volume_after_dilution*(3.1/100)
            total_blended_volume = volume_after_dilution - volume_lost_to_contraction
        
        if spirit_count == 2:
            blend_1_vol, blend_1_abv = get_blend(vol_alc_1, abv_alc_1, vol_alc_2, abv_alc_2)

            water_used = get_water_requirement(blend_1_vol, blend_1_abv, target_abv)

            components_df = pd.DataFrame(index=[
                name_alc_1, name_alc_2, 'Components Blended'])
            components_df['Alcohol Volume'] = [
                vol_alc_1, vol_alc_2, blend_1_vol]
            components_df['Alcohol ABV'] = [
                abv_alc_1, abv_alc_2, blend_1_abv]

            blend_volume = blend_1_vol
            blend_abv = blend_1_abv
            volume_after_dilution = blend_1_vol + water_used
            volume_lost_to_contraction = volume_after_dilution*(3.1/100)
            total_blended_volume = volume_after_dilution - volume_lost_to_contraction

        if spirit_count == 3:
            blend_1_vol, blend_1_abv = get_blend(vol_alc_1, abv_alc_1, vol_alc_2, abv_alc_2)

            blend_2_vol, blend_2_abv = get_blend(vol_alc_3, abv_alc_3, blend_1_vol, blend_1_abv)

            water_used = get_water_requirement(blend_2_vol, blend_2_abv, target_abv)

            components_df = pd.DataFrame(index=[
                name_alc_1, name_alc_2, 'First Components Blended', name_alc_3, 'Third Component Blended'])
            components_df['Alcohol Volume'] = [
                vol_alc_1, vol_alc_2, blend_1_vol, vol_alc_3, blend_2_vol]
            components_df['Alcohol ABV'] = [
                abv_alc_1, abv_alc_2, blend_1_abv, abv_alc_3, blend_2_abv]

            blend_volume = blend_2_vol
            blend_abv = blend_2_abv
            volume_after_dilution = blend_2_vol + water_used
            volume_lost_to_contraction = volume_after_dilution*(3.1/100)
            total_blended_volume = volume_after_dilution - volume_lost_to_contraction

        if spirit_count == 4:
            blend_1_vol, blend_1_abv = get_blend(vol_alc_1, abv_alc_1, vol_alc_2, abv_alc_2)

            blend_2_vol, blend_2_abv = get_blend(vol_alc_3, abv_alc_3, blend_1_vol, blend_1_abv)

            blend_3_vol, blend_3_abv = get_blend(vol_alc_4, abv_alc_4, blend_2_vol, blend_2_abv)

            water_used = get_water_requirement(blend_3_vol, blend_3_abv, target_abv)

            components_df = pd.DataFrame(index=[
                name_alc_1, name_alc_2, 'First Components Blended', name_alc_3, 'Third Component Blended', name_alc_4, 'Fourth Component Blended'])
            components_df['Alcohol Volume'] = [
                vol_alc_1, vol_alc_2, blend_1_vol, vol_alc_3, blend_2_vol, vol_alc_4, blend_3_vol]
            components_df['Alcohol ABV'] = [
                abv_alc_1, abv_alc_2, blend_1_abv, abv_alc_3, blend_2_abv, abv_alc_4, blend_3_abv]

            blend_volume = blend_3_vol
            blend_abv = blend_3_abv
            volume_after_dilution = blend_3_vol + water_used
            volume_lost_to_contraction = volume_after_dilution*(3.1/100)
            total_blended_volume = volume_after_dilution - volume_lost_to_contraction

        if spirit_count == 5:
            blend_1_vol, blend_1_abv = get_blend(vol_alc_1, abv_alc_1, vol_alc_2, abv_alc_2)

            blend_2_vol, blend_2_abv = get_blend(vol_alc_3, abv_alc_3, blend_1_vol, blend_1_abv)

            blend_3_vol, blend_3_abv = get_blend(vol_alc_4, abv_alc_4, blend_2_vol, blend_2_abv)

            blend_4_vol, blend_4_abv = get_blend(vol_alc_5, abv_alc_5, blend_3_vol, blend_3_abv)

            water_used = get_water_requirement(blend_4_vol, blend_4_abv, target_abv)
            
            components_df = pd.DataFrame(index=[
                name_alc_1, name_alc_2, 'First Components Blended', name_alc_3, 'Third Component Blended', name_alc_4, 'Fourth Component Blended', name_alc_5, 'Fifth Component Blended'])
            components_df['Alcohol Volume'] = [
                vol_alc_1, vol_alc_2, blend_1_vol, vol_alc_3, blend_2_vol, vol_alc_4, blend_3_vol, vol_alc_5, blend_4_vol]
            components_df['Alcohol ABV'] = [
                abv_alc_1, abv_alc_2, blend_1_abv, abv_alc_3, blend_2_abv, abv_alc_4, blend_3_abv, abv_alc_5, blend_4_abv]

            blend_volume = blend_4_vol
            blend_abv = blend_4_abv
            volume_after_dilution = blend_4_vol + water_used
            volume_lost_to_contraction = volume_after_dilution*(3.1/100)
            total_blended_volume = volume_after_dilution - volume_lost_to_contraction

        blended_df['Initial Blend Volume'] = blend_volume
        blended_df['Initial Blend ABV'] = blend_abv
        blended_df['Water Used'] = round(water_used, 2)
        blended_df['Post-Water Blend Volume'] = round(volume_after_dilution,2)
        blended_df['Volume Lost to Contraction'] = round(volume_lost_to_contraction, 2)
        blended_df['Final Blend Volume'] = round(total_blended_volume, 2)
        

        st.subheader('Blend Components')
        st.dataframe(components_df.style.format('{:.2f}'))

        st.subheader('Blend Volumes')
        st.dataframe(blended_df.style.format('{:.2f}'))

# Picking Option 2, Step 2:
if option == option_2:
    if target_abv <=.65:
        quotient = .0319
    else:
        quotient = .027
    pVol = get_prelimVol(target_volume, quotient)
    water = get_water_req(pVol, target_abv, starting_abv)
    sVol = get_starting_volume(pVol, water)

    contract_vol = target_volume - pVol

    cutting_df = pd.DataFrame(index=['Initial Bulk Liters Required','Starting ABV', 'Water Required', 'Preliminary Volume pre-Contraction', 'Volume Lost to Contraction', 'Final Bulk Liters', 'Final ABV', 'Final LPAs'])
    cutting_df['Volumes & Percentages'] = [sVol, starting_abv ,water, pVol, contract_vol, target_volume, target_abv, (target_volume*target_abv)/100]

    st.subheader('Requirements & Effects of Cutting')
    st.dataframe(cutting_df.style.format('{:.1f}'))
