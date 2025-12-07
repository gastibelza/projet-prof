import streamlit as st
import random
import time

# --- CONFIGURATION ---
st.set_page_config(
    page_title="SYSTEME P.R.O.F v2.4",
    page_icon="🎄",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- CSS STYLES (HACKER FESTIF) ---
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background-color: #0d0d0d;
        color: #00ff00;
        font-family: 'Courier New', Courier, monospace;
    }
    
    /* Headers */
    h1, h2, h3, h4, h5, h6 {
        color: #00ff00 !important;
        font-family: 'Courier New', Courier, monospace;
        text-shadow: 0 0 5px #00ff00;
    }
    
    /* Inputs */
    .stTextInput > div > div > input {
        background-color: #1a1a1a;
        color: #00ff00;
        border: 1px solid #00ff00;
        font-family: 'Courier New', Courier, monospace;
    }
    
    /* Buttons */
    .stButton > button {
        background-color: #003300;
        color: #00ff00;
        border: 1px solid #00ff00;
        font-family: 'Courier New', Courier, monospace;
        width: 100%;
    }
    .stButton > button:hover {
        background-color: #00ff00;
        color: #000000;
        box-shadow: 0 0 10px #00ff00;
    }
    
    /* Sliders */
    .stSlider > div > div > div > div {
        background-color: #00ff00;
    }
    
    /* Success/Error/Info boxes */
    .stSuccess, .stError, .stInfo {
        background-color: #1a1a1a;
        color: #00ff00;
        border: 1px solid #00ff00;
    }
    
    /* Custom classes */
    .hacker-text {
        font-family: 'Courier New', Courier, monospace;
        color: #00ff00;
    }
    .christmas-emoji {
        font-size: 2em;
    }
    </style>
    """, unsafe_allow_html=True)

# --- STATE MANAGEMENT ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'gift_unlocked' not in st.session_state:
    st.session_state.gift_unlocked = False

# --- DATA ---
PHRASES_SVT = [
    "Élève en dormance hivernale, réveil prévu au printemps.",
    "Activité neuronale comparable à un lichen sur sol acide.",
    "Aussi dynamique qu'une roche sédimentaire.",
    "Tentative de photosynthèse en cours... échec critique.",
    "Métabolisme intellectuel proche du zéro absolu.",
    "Capacité de concentration inversement proportionnelle à la complexité du caryotype.",
    "Évolution darwinienne en pause indéterminée.",
    "Symbiose parfaite avec le radiateur du fond.",
    "Réaction enzymatique lente, très lente...",
    "Niveau d'énergie : fossile."
]

PRESCRIPTIONS_GEO = [
    "ALERTE : Éruption imminente ! Évacuez les élèves vers la zone de subduction.",
    "Stabilité précaire. Risque de séisme magnitude 8 sur l'échelle de Richter du stress.",
    "Niveau de magma critique. Prescription : Chocolat en intraveineuse immédiate.",
    "Calme plat. Plaque tectonique au repos. Profitez-en pour corriger 2 copies.",
    "Pression modérée. Une tisane et ça repart comme une coulée de lave fluide."
]

# --- MAIN APP ---

def login_screen():
    st.title("🔒 ACCÈS RESTREINT")
    st.markdown("### Veuillez vous identifier")
    
    password = st.text_input("Mot de passe", type="password")
    
    if st.button("INITIALISER LA CONNEXION"):
        if password == "MITOSE":
            st.session_state.logged_in = True
            st.success("ACCÈS AUTORISÉ. BIENVENUE AGENT SOUMAYYAT.")
            time.sleep(1)
            st.rerun()
        else:
            st.error("ACCÈS REFUSÉ. ERREUR DE RÉPLICATION.")

def main_app():
    st.title("🎄 SYSTEME P.R.O.F v2.4 🎅")
    st.markdown("---")
    
    # Feature A: Mood Tracker
    st.header("📊 ANALYSE SISMIQUE (Mood Tracker)")
    
    col1, col2 = st.columns(2)
    with col1:
        magma = st.slider("Niveau de Magma (Colère)", 0, 100, 50)
    with col2:
        pression = st.slider("Pression Tectonique (Fatigue)", 0, 100, 50)
        
    if st.button("ANALYSER L'ÉTAT GÉOLOGIQUE"):
        with st.spinner("Calcul des contraintes tectoniques..."):
            time.sleep(1.5)
            prescription = random.choice(PRESCRIPTIONS_GEO)
            st.info(f"📋 RÉSULTAT : {prescription}")
            
    st.markdown("---")
    
    # Feature B: Générateur de Bulletins
    st.header("📝 GÉNÉRATEUR D'APPRÉCIATIONS SVT")
    st.markdown("*Pour les cas désespérés...*")
    
    if st.button("GÉNÉRER APPRÉCIATION"):
        phrase = random.choice(PHRASES_SVT)
        st.code(phrase, language="text")
        
    st.markdown("---")
    
    # Feature C: La Cachette
    st.header("🎁 ZONE SECRÈTE")
    
    if not st.session_state.gift_unlocked:
        code_secret = st.text_input("Code de déverrouillage (Indice : La vie)", type="password")
        if st.button("DÉCRYPTER"):
            if code_secret == "ADN":
                st.session_state.gift_unlocked = True
                st.balloons()
                st.rerun()
            else:
                st.error("CODE INCORRECT. MUTATION DÉTECTÉE.")
    else:
        st.success("🔓 ACCÈS DÉVERROUILLÉ !")
        st.markdown("""
            <div style="border: 2px solid #00ff00; padding: 20px; border-radius: 10px; text-align: center;">
                <h2 style="color: #ff0000 !important;">🎅 CADEAU DÉTECTÉ 🎅</h2>
                <p style="font-size: 1.5em;">Regarde derrière l'imprimante 3D du labo.</p>
                <p>Joyeux Noël Soumayyat !</p>
            </div>
        """, unsafe_allow_html=True)

# --- ROUTING ---
if not st.session_state.logged_in:
    login_screen()
else:
    main_app()
