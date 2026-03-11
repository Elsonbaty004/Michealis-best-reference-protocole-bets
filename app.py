import streamlit as st
import random

# --- CONFIGURATION ---
st.set_page_config(page_title="Michaelis Scanner", layout="wide")

if "auth" not in st.session_state:
    st.session_state["auth"] = False

# --- SECURITÉ ---
if not st.session_state["auth"]:
    pwd = st.text_input("Mot de passe", type="password")
    if st.button("Entrer"):
        if pwd == "soixante":
            st.session_state["auth"] = True
            st.rerun()
    st.stop()

# --- INTERFACE ---
st.title("🎯 Mes Coupons de la Semaine")

# Zone pour entrer les vrais matchs manuellement (en attendant le robot)
st.sidebar.header("📝 Entrer les matchs réels")
input_matchs = st.sidebar.text_area("Colle les matchs ici (un par ligne)", 
    "Lakers vs Celtics (NBA)\nPSG vs Marseille (Foot)\nReal Madrid vs Barca (Foot)\nMcGregor vs Chandler (UFC)")

matchs_liste = input_matchs.split('\n')

capital = st.sidebar.number_input("Capital (HTG)", value=1000)

if st.button("🚀 Générer 12 Coupons avec ces matchs"):
    cols = st.columns(3)
    for i in range(1, 13):
        # On choisit 3 à 4 matchs parmi ta liste
        selection = random.sample(matchs_liste, min(len(matchs_liste), 4))
        note = round(random.uniform(7.5, 9.9), 1)
        mise = round((capital * 0.15 * note) / (5 + note), 2)
        
        with cols[(i-1)%3]:
            st.markdown(f"""
            <div style="border:2px solid #27ae60; padding:15px; border-radius:10px; margin-bottom:10px;">
                <h3 style="color:#27ae60;">COUPON #{i}</h3>
                <p>Note : <b>{note}/10</b> | Mise : <b>{mise} HTG</b></p>
                <ul style="color: white;">
                    {''.join([f"<li>✅ {m}</li>" for m in selection])}
                </ul>
            </div>
            """, unsafe_allow_html=True)
