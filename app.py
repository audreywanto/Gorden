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
        category = st.selectbox('Tipe Gorden', ('Smokring', 'Kronille', 'Cantel S', 'Vitrase'), help= 'Kronille hanya untuk Bahan Vitrase dan Linen Non Blackout')
        material = st.selectbox('Bahan Gorden', ('Blackout Doft Doft 230gsm', 'Blackout Doft Shiny 200gsm', 'Blackout Doft Doft 200gsm', 'Blackout Doft Doft 230gsm (Khusus Dark Grey/Pale Khaky)', 'Linen Blackout 100%', 'Juliet Blackout', 'Java Silk', 'Java Slub', 'Java Mos', 'Java Sya', 'Java Shiren', 'Linen Non Blackout', 'Amaro', 'Otis', 'Vitrase', 'Micro'), help= 'Vitrase hanya bisa dihitung jika Tipe nya Vitrase atau Kronille')
        lebar = st.number_input('Lebar', 0, 9999, 130, help='Ukuran dalam cm')
        tinggi = st.number_input('Tinggi', 0, 9999, 230, help='Ukuran dalam cm')
        
        st.markdown('---')
        
        # Base price
        blackoutdoft = 190000
        blackoutshiny = 130000
        blackoutDGPK = 230000
        blackout200 = 170000
        linenbo = 350000
        juliet = 279000
        silk = 130000
        slub = 130000
        mos = 135000
        sya = 135000
        shiren = 99000
        linen = 90000
        jacquard = 110000
        amaro = 165000
        otis = 165000
        firework = 165000
        waffle = 165000
        klinen = 130000
        kblackoutdoft = 140000
        kblackoutshiny = 120000
        kmicro = 80000
        ringmicro = 120000
        
        # Base Calculations
        helai = lebar / 70
        decimal = helai % 1
        oddeven = helai % 2
        
        # Height Calculations
        if tinggi >= 400:
            multiplier = 3
        elif tinggi >= 390:
            multiplier = 2.9
        elif tinggi >= 380:
            multiplier = 2.8
        elif tinggi >= 370:
            multiplier = 2.7
        elif tinggi >= 360:
            multiplier = 2.6
        elif tinggi >= 350:
            multiplier = 2.5
        elif tinggi >= 340:
            multiplier = 2.4
        elif tinggi >= 330:
            multiplier = 2.3
        elif tinggi >= 320:
            multiplier = 2.2
        elif tinggi >= 310:
            multiplier = 2.1
        elif tinggi >= 300:
            multiplier = 2
        elif tinggi >= 290:
            multiplier = 1.9
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
        if category == 'Smokring' and (material == 'Blackout Doft Doft 230gsm' or material == 'Blackout Doft Shiny 200gsm' or material == 'Blackout Doft Doft 200gsm' or material == 'Blackout Doft Doft 230gsm (Khusus Dark Grey/Pale Khaky)' or material == 'Linen Blackout 100%' or material == 'Juliet Blackout' or material == 'Linen Non Blackout' or material == 'Amaro' or material == 'Otis' or material == 'Firework' or material == 'Waffle'):
            if decimal > 0.3 or oddeven == 1:
                val = math.ceil(helai/2.)*2
            else:
                val = math.floor(helai)
            if tinggi <= 270 and lebar < 240 and lebar >= 160:
                if val % 2 == 0:
                    val = val - 1
            if tinggi <= 270 and lebar < 350 and lebar >= 310:
                if val % 2 == 0:
                    val = val - 1
                
            # Calculations
            if material == 'Blackout Doft Doft 230gsm':
                price = blackoutdoft * val
                price = price * multiplier + 20000
            elif material == 'Amaro' or material == 'Otis' or material == 'Firework' or material == 'Waffle':
                price = amaro * val
                price = price * multiplier + 20000
            elif material == 'Blackout Doft Shiny 200gsm':
                price = blackoutshiny * val
                price = price * multiplier + 20000
            elif material == 'Blackout Doft Doft 200gsm':
                price = blackout200 * val
                price = price * multiplier + 20000
            elif material == 'Blackout Doft Doft 230gsm (Khusus Dark Grey/Pale Khaky)':
                price = blackoutDGPK * val
                price = price * multiplier + 20000
            elif material == 'Linen Blackout 100%':
                price = linenbo * val
                price = price * multiplier + 20000
            elif material == 'Juliet Blackout':
                price = juliet * val
                price = price * multiplier + 20000
            elif material == 'Linen Non Blackout':
                price = linen * val
                price = price * multiplier + 20000
        
        # Helai Calculations 140 Smokring
        elif category == 'Smokring' and (material == 'Java Mos' or material == 'Java Silk' or material == 'Java Slub' or material == 'Java Sya' or material == 'Jacquard' or material == 'Micro' or material == 'Java Shiren'):
            if decimal < 0.4:
                val = math.floor(helai)
            else:
                val = math.floor(helai) + 1
                
            # Calculations
            if material == 'Java Silk':
                price = silk * val
                price = price * multiplier + 20000
            elif material == 'Java Slub':
                price = slub * val
                price = price * multiplier + 20000
            elif material == 'Java Mos':
                price = mos * val
                price = price * multiplier + 20000
            elif material == 'Java Sya':
                price = sya * val
                price = price * multiplier + 20000
            elif material == 'Java Shiren':
                price = shiren * val
                price = price * multiplier + 20000
            elif material == 'Jacquard':
                price = jacquard * val
                price = price * multiplier + 20000
            elif material == 'Micro':
                price = ringmicro * val
                price = price * multiplier + 20000
        
        # Helai Calculations NON 140 Cantel S
        elif category == 'Cantel S' and (material == 'Blackout Doft Doft 230gsm' or material == 'Blackout Doft Shiny 200gsm' or material == 'Blackout Doft Doft 200gsm' or material == 'Blackout Doft Doft 230gsm (Khusus Dark Grey/Pale Khaky)' or material == 'Linen Blackout 100%' or material == 'Juliet Blackout' or material == 'Linen Non Blackout' or material == 'Amaro' or material == 'Otis' or material == 'Firework' or material == 'Waffle'):
            if decimal > 0:
                val = math.ceil(helai/2.)*2
            else:
                val = math.floor(helai)
            if tinggi <= 270 and lebar < 240 and lebar > 160:
                if val % 2 == 0:
                    val = val-1
            if tinggi <= 270 and lebar < 350 and lebar >= 310:
                if val % 2 == 0:
                    val = val - 1
                
            # Calculations
            if material == 'Blackout Doft Doft 230gsm':
                price = blackoutdoft * val
                price = price * multiplier + 50000
            elif material == 'Blackout Doft Shiny 200gsm':
                price = blackoutshiny * val
                price = price * multiplier + 50000
            elif material == 'Blackout Doft Doft 200gsm':
                price = blackout200 * val
                price = price * multiplier + 50000
            elif material == 'Blackout Doft Doft 230gsm (Khusus Dark Grey/Pale Khaky)':
                price = blackoutDGPK * val
                price = price * multiplier + 50000
            elif material == 'Amaro' or material == 'Otis' or material == 'Firework' or material == 'Waffle':
                price = amaro * val
                price = price * multiplier + 50000
            elif material == 'Linen Blackout 100%':
                price = linenbo * val
                price = price * multiplier + 50000
            elif material == 'Juliet Blackout':
                price = juliet * val
                price = price * multiplier + 50000
            elif material == 'Linen Non Blackout':
                price = linen * val
                price = price * multiplier + 50000
        
        # Helai Calculations 140 Cantel S
        elif category == 'Cantel S' and (material == 'Java Mos' or material == 'Java Silk' or material == 'Java Slub' or material == 'Java Sya' or material == 'Jacquard' or material == 'Java Shiren'):
            if decimal > 0 :
                val = math.floor(helai) + 1
            else:
                val = math.floor(helai)
                
            # Calculations
            if material == 'Java Silk':
                price = silk * val
                price = price * multiplier + 50000
            elif material == 'Java Slub':
                price = slub * val
                price = price * multiplier + 50000
            elif material == 'Java Mos':
                price = mos * val
                price = price * multiplier + 50000
            elif material == 'Java Sya':
                price = sya * val
                price = price * multiplier + 50000
            elif material == 'Java Shiren':
                price = shiren * val
                price = price * multiplier + 50000
            elif material == 'Jacquard':
                price = jacquard * val
                price = price * multiplier + 50000
        
        # Vitrase Calculations
        elif category == 'Vitrase':
            vhelai = lebar / 100
            vhelai = round(vhelai, 1)
            price = 122500 * vhelai
            price = price * multiplier
        
        # Kronille Calculations
        elif category == 'Kronille' and material == 'Linen Non Blackout':
            if decimal > 0.3 or oddeven == 1:
                val = math.ceil(helai/2.)*2
            else:
                val = math.floor(helai)
            
            # Calculations
            if material == 'Linen Non Blackout':
                price = linen * val
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
            price = 57500 * val
            price = price * multiplier
            formatted_price = "{:,.2f}".format(price)
            
        formatted_price = "{:,.2f}".format(price)
        submitted = st.form_submit_button('Harga')
    
    if submitted:
        st.write('### Harga per Jendela Adalah:')
        st.write('#### Rp.', formatted_price)
                
if __name__ == '__main__':
    run()
