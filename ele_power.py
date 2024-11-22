import streamlit as st
import math

def Elec_Power(V,I,PF):
    phi = math.acos(PF)            # Angle in radians
    P = V * I * PF                  # Active power
    Q = V * I * math.sin(phi)       # Reactive power
    S = V * I                       # Apparent power
    return P, Q, S
    

st.title("02341A0259-PS6")
st.markdown("This app calculates **Active Power (P)**, **Reactive Power (Q)**, and **Apparent Power (S)**.")


col1, col2 = st.columns(2)
with col1:
        with st.container(border=True):
            V = st.number_input("Input voltage (V)", value=10.0)
            I = st.number_input("Current (I)", value=5.0)
            PF = st.number_input("Power Factor (PF):", value=0.8)
            compute=st.button("Compute")
            

with col2:
        with st.container(border=True):
            if compute:
                if PF <= 1.0:
                    P, Q, S = Elec_Power(V, I, PF)
                    st.write(f"Active Power (P): {P:.2f} W") 
                    st.write(f"Reactive Power (Q): {Q:.2f} VAR")
                    st.write(f"Apparent Power (S): {S:.2f} VA")
            

