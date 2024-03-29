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
        category = st.selectbox('Tipe Gorden', ('Smokring', 'Kronille', 'Cantel S', 'Vitrase'))
        material = st.selectbox('Bahan Gorden', ('Blackout Doft Doft', 'Blackout Doft Shiny', 'Linen Blackout', 'Juliet', 'Java Silk', 'Java Slub', 'Java Mos', 'Java Sya', 'Java Shiren', 'Linen Non Blackout', 'Jacquard', 'Amaro', 'Otis', 'Firework', 'Waffle', 'Vitrase', 'Micro'))
        lebar = st.number_input('Lebar', 0, 9999, 130, help='Ukuran dalam cm')
        tinggi = st.number_input('Tinggi', 0, 9999, 230, help='Ukuran dalam cm')
        
        st.markdown('---')
        
        # Base price
        blackoutdoft = 165000
        blackoutshiny = 130000
        linenbo = 270000
        juliet = 185000
        silk = 128000
        slub = 123000
        mos = 113000
        sya = 113000
        shiren = 99000
        linen = 125000
        jacquard = 99000
        amaro = 165000
        otis = 165000
        firework = 165000
        waffle = 165000
        klinen = 100000
        kblackoutdoft = 130000
        kblackoutshiny = 120000
        kmicro = 80000
        ringmicro = 120000
        
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
        
        # Helai Calculations NON 140 Smokring
        if category == 'Smokring' and (material == 'Blackout Doft Doft' or material == 'Blackout Doft Shiny' or material == 'Linen Blackout' or material == 'Juliet' or material == 'Linen Non Blackout' or material == 'Amaro' or material == 'Otis' or material == 'Firework' or material == 'Waffle'):
            if decimal > 0.3 or oddeven == 1:
                val = math.ceil(helai/2.)*2
            else:
                val = math.floor(helai)
                
            # Calculations
            if material == 'Blackout Doft Doft':
                price = blackoutdoft * val
                price = price * multiplier
            elif material == 'Amaro' or material == 'Otis' or material == 'Firework' or material == 'Waffle':
                price = amaro * val
                price = price * multiplier
            elif material == 'Blackout Doft Shiny':
                price = blackoutshiny * val
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
        
        # Helai Calculations 140 Smokring
        elif category == 'Smokring' and (material == 'Java Mos' or material == 'Java Silk' or material == 'Java Slub' or material == 'Java Sya' or material == 'Jacquard' or material == 'Micro' or material == 'Java Shiren'):
            if decimal < 0.4:
                val = math.floor(helai)
            else:
                val = math.floor(helai) + 1
                
            # Calculations
            if material == 'Java Silk':
                price = silk * val
                price = price * multiplier
            elif material == 'Java Slub':
                price = slub * val
                price = price * multiplier
            elif material == 'Java Mos':
                price = mos * val
                price = price * multiplier
            elif material == 'Java Sya':
                price = sya * val
                price = price * multiplier
            elif material == 'Java Shiren':
                price = shiren * val
                price = price * multiplier
            elif material == 'Jacquard':
                price = jacquard * val
                price = price * multiplier
            elif material == 'Micro':
                price = ringmicro * val
                price = price * multiplier
        
        # Helai Calculations NON 140 Cantel S
        elif category == 'Cantel S' and (material == 'Blackout Doft Doft' or material == 'Blackout Doft Shiny' or material == 'Linen Blackout' or material == 'Juliet' or material == 'Linen Non Blackout' or material == 'Amaro' or material == 'Otis' or material == 'Firework' or material == 'Waffle'):
            if decimal > 0:
                val = math.ceil(helai/2.)*2
            else:
                val = math.floor(helai)
                
            # Calculations
            if material == 'Blackout Doft Doft':
                price = blackoutdoft * val
                price = price * multiplier
            elif material == 'Blackout Doft Shiny':
                price = blackoutshiny * val
                price = price * multiplier
            elif material == 'Amaro' or material == 'Otis' or material == 'Firework' or material == 'Waffle':
                price = amaro * val
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
        elif category == 'Cantel S' and (material == 'Java Mos' or material == 'Java Silk' or material == 'Java Slub' or material == 'Java Sya' or material == 'Jacquard' or material == 'Java Shiren'):
            if decimal > 0 :
                val = math.floor(helai) + 1
            else:
                val = math.floor(helai)
                
            # Calculations
            if material == 'Java Silk':
                price = silk * val
                price = price * multiplier
            elif material == 'Java Slub':
                price = slub * val
                price = price * multiplier
            elif material == 'Java Mos':
                price = mos * val
                price = price * multiplier
            elif material == 'Java Sya':
                price = sya * val
                price = price * multiplier
            elif material == 'Java Shiren':
                price = shiren * val
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
        
        # Kronille Calculations
        elif category == 'Kronille' and (material == 'Micro' or material == 'Linen Non Blackout' or material == 'Blackout Doft Doft' or material == 'Blackout Doft Shiny'):
            if decimal > 0.3 or oddeven == 1:
                val = math.ceil(helai/2.)*2
            else:
                val = math.floor(helai)
            
            # Calculations
            if material == 'Blackout Doft Doft':
                price = kblackoutdoft * val
                price = price * multiplier
            elif material == 'Linen Non Blackout':
                price = klinen * val
                price = price * multiplier
            elif material == 'Micro':
                price = kmicro * val
                price = price * multiplier
            elif material == 'Blackout Doft Shiny':
                price = kblackoutshiny * val
                price = price * multiplier
        
        # Kronille Vitrase Calculations
        elif category == 'Kronille' and material == 'Vitrase':
            vhelai = lebar / 50
            vehali = round(vehali, 1)
            vdecimal = vhelai % 1
            voddeven = vhelai % 2
            if vdecimal > 0.3 or voddeven == 1:
                val = math.ceil(vhelai/2.)*2
            else:
                val = math.floor(vhelai)
            
            # Calculations
            price = 70000 * val
            price = price * multiplier
        
        submitted = st.form_submit_button('Harga')
    
    if submitted:
        st.write('### Harga per Jendela Adalah:')
        st.write('####', price)
                
if __name__ == '__main__':
    run()
