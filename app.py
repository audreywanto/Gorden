import streamlit as st
import math

st.set_page_config(
    page_title='Hitungan Gorden',
    layout='wide',
    initial_sidebar_state='expanded'
)

def run():
    st.title('Hitungan Custom Gorden JJ Interior Collections PER Jendela')
    with st.form(key='form parameters'):
        category = st.selectbox('Tipe Gorden', ('Smokring/Kronille', 'Cantel S', 'Vitrase'))
        material = st.selectbox('Bahan Gorden', ('Blackout', 'Linen Blackout', 'Juliet', 'Java Silk', 'Java Slub', 'Java Mos', 'Java Sya', 'Linen Non Blackout', 'Jacquard', 'Amaro', 'Otis', 'Firework', 'Waffle', 'Vitrase'))
        lebar = st.number_input('Lebar', 0, 9999, 130, help='Ukuran dalam cm')
        tinggi = st.number_input('Tinggi', 0, 9999, 230, help='Ukuran dalam cm')
        
        st.markdown('---')
        
        # Base price
        blackout = 165000
        linenbo = 275000
        juliet = 185000
        silk = 115000
        slub = 125000
        mos = 115000
        sya = 125000
        linen = 120000
        jacquard = 89000
        amaro = 165000
        otis = 165000
        firework = 165000
        waffle = 165000
        
        # Base Calculations
        helai = lebar / 70
        decimal = helai % 1
        oddeven = helai % 2
        
        # Height Calculations
        if tinggi >= 300:
            multiplier = 2
        elif tinggi >= 280:
            multiplier = 1.8
        elif tinggi >=  270:
            multiplier = 1.7
        elif tinggi >= 260:
            multiplier = 1.6
        elif tinggi >= 250:
            multiplier = 1.5
        elif tinggi >= 240:
            multiplier = 1.4
        else:
            multiplier = 1.25
        
        # Helai Calculations NON 140 Smokring/Kronille
        if category == 'Smokring/Kronille' and (material == 'Blackout' or material == 'Linen Blackout' or material == 'Juliet' or material == 'Linen Non Blackout' or material == 'Amaro' or material == 'Otis' or material == 'Firework' or material == 'Waffle'):
            if decimal > 3 or oddeven == 1:
                val = math.ceil(helai/2.)*2
            else:
                val = math.floor(helai)
                
            # Calculations
            if material == 'Blackout' or material == 'Amaro' or material == 'Otis' or material == 'Firework' or material == 'Waffle':
                price = blackout * val
                price = price * multiplier
            elif material == 'Linen Blackout':
                price = linenbo * val
                price = price * multiplier
            elif material == 'Juliet':
                price = juliet * val
                price = price * multiplier
            elif material == 'Linen Non Blackout':
                price = linen * val
                price = price * multiplier
        
        # Helai Calculations 140 Smokring/Kronille
        elif category == 'Smokring/Kronille' and (material == 'Java Mos' or material == 'Java Silk' or material == 'Java Slub' or material == 'Java Sya' or material == 'Jacquard'):
            if decimal < 4:
                val = math.floor(helai)
            else:
                val = math.floor(helai) + 1
                
            # Calculations
            if material == 'Java Silk' or material == 'Java Mos':
                price = silk * val
                price = price * multiplier
            elif material == 'Java Slub' or material == 'Java Sya':
                price = slub * val
                price = price * multiplier
            elif material == 'Jacquard':
                price = jacquard * val
                price = price * multiplier
        
        # Helai Calculations NON 140 Cantel S
        elif category == 'Cantel S' and (material == 'Blackout' or material == 'Linen Blackout' or material == 'Juliet' or material == 'Linen Non Blackout' or material == 'Amaro' or material == 'Otis' or material == 'Firework' or material == 'Waffle'):
            if decimal > 0:
                val = math.ceil(helai/2.)*2
            else:
                val = math.floor(helai)
                
            # Calculations
            if material == 'Blackout' or material == 'Amaro' or material == 'Otis' or material == 'Firework' or material == 'Waffle':
                price = blackout * val
                price = price * multiplier
            elif material == 'Linen Blackout':
                price = linenbo * val
                price = price * multiplier
            elif material == 'Juliet':
                price = juliet * val
                price = price * multiplier
            elif material == 'Linen Non Blackout':
                price = linen * val
                price = price * multiplier
        
        # Helai Calculations 140 Cantel S
        elif category == 'Cantel S' and (material == 'Java Mos' or material == 'Java Silk' or material == 'Java Slub' or material == 'Java Sya' or material == 'Jacquard'):
            if decimal > 0 :
                val = math.floor(helai) + 1
            else:
                val = math.floor(helai)
                
            # Calculations
            if material == 'Java Silk' or material == 'Java Mos':
                price = silk * val
                price = price * multiplier
            elif material == 'Java Slub' or material == 'Java Sya':
                price = slub * val
                price = price * multiplier
            elif material == 'Jacquard':
                price = jacquard * val
                price = price * multiplier
        
        # Vitrase Calculations
        elif category == 'Vitrase':
            vhelai = lebar / 100
            vhelai = round(vhelai, 1)
            price = 115000 * vhelai
            price = price * multiplier
        
        submitted = st.form_submit_button('Harga')
    
    if submitted:
        st.write('### Harga per Jendela Adalah:')
        st.write('####', price)
                
if __name__ == '__main__':
    run()
