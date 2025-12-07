import streamlit as st
import random
import time

# --- CONFIGURATION AGILE (MODIFIER ICI CHAQUE JOUR) ---
MOT_DE_PASSE_DU_JOUR = "MITOCHONDRIE"
URL_PHOTO_DU_JOUR = "https://images.unsplash.com/photo-1512389142860-9c449e58a543?ixlib=rb-4.0.3&auto=format&fit=crop&w=1000&q=80" # Photo de Noël générique

# --- CONFIGURATION APP ---
st.set_page_config(
    page_title="SYSTEME P.R.O.F v3.0 - SOUMAYYAT EDITION",
    page_icon="🧬",
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
        font-weight: bold;
    }
    .stButton > button:hover {
        background-color: #00ff00;
        color: #000000;
        box-shadow: 0 0 10px #00ff00;
    }
    
    /* Success/Error/Info boxes */
    .stSuccess, .stError, .stInfo {
        background-color: #1a1a1a;
        color: #00ff00;
        border: 1px solid #00ff00;
    }
    
    /* Custom classes */
    .matrix-text {
        font-family: 'Courier New', Courier, monospace;
        color: #00ff00;
        font-size: 1.1em;
    }
    .highlight {
        color: #ff00ff;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- STATE MANAGEMENT ---
if 'intro_shown' not in st.session_state:
    st.session_state.intro_shown = False
if 'gift_unlocked' not in st.session_state:
    st.session_state.gift_unlocked = False

# --- DATA: GÉNÉRATEUR SVT TURBO (50+ PHRASES) ---
PHRASES_SVT_TURBO = [
    "Activité neuronale comparable à un lichen sur sol acide.",
    "Tentative de photosynthèse en cours... échec critique par manque de lumière.",
    "Élève en dormance hivernale, réveil prévu au prochain millénaire.",
    "Aussi dynamique qu'une roche sédimentaire au fond d'un lac.",
    "Métabolisme intellectuel proche du zéro absolu.",
    "Capacité de concentration inversement proportionnelle à la complexité du caryotype.",
    "Évolution darwinienne en pause indéterminée.",
    "Symbiose parfaite avec le radiateur du fond.",
    "Réaction enzymatique lente, très lente... voire inexistante.",
    "Niveau d'énergie : fossile.",
    "Le phénotype 'je dors en cours' est clairement dominant.",
    "Vitesse de sédimentation des connaissances : rapide.",
    "Subduction de la motivation observée dès 8h05.",
    "Activité sismique nulle : encéphalogramme plat.",
    "Une mitose cellulaire a plus d'action que cet élève.",
    "Absence totale de chlorophylle intellectuelle.",
    "Le noyau cellulaire semble vide de toute information.",
    "Migration des neurones vers le sud pour l'hiver.",
    "Fossilisation en cours sur la chaise.",
    "Dérive des continents attentionnels vers le smartphone.",
    "Érosion rapide de la bonne volonté.",
    "Un trilobite aurait plus de réactivité.",
    "La sélection naturelle ne joue pas en sa faveur aujourd'hui.",
    "Tentative de méiose ratée : on a perdu la moitié des informations.",
    "Le cytoplasme est là, mais l'esprit est ailleurs.",
    "Respiration cellulaire en mode économie d'énergie extrême.",
    "Une fougère a plus d'interactions avec son environnement.",
    "Cycle de Krebs bloqué à l'étape 'Sieste'.",
    "L'ADN de cet élève code pour la procrastination.",
    "Héritage génétique : 100% fatigue.",
    "Mutation spontanée vers l'état végétatif.",
    "Le complexe argilo-humique a plus de cohésion que ses idées.",
    "Bilan carbone : rejette plus de CO2 qu'il n'absorbe de savoir.",
    "Tectonique des plaques : ses paupières se ferment par subduction.",
    "Un écosystème à lui tout seul, mais sans producteur primaire.",
    "Niche écologique : le fond de la classe, près de la fenêtre.",
    "Chaîne alimentaire : se nourrit exclusivement de rêves.",
    "Biodiversité des excuses pour ne pas travailler : exceptionnelle.",
    "Adaptation au milieu scolaire : échec.",
    "Le génotype promettait, le phénotype déçoit.",
    "Osmose inverse : le savoir sort au lieu de rentrer.",
    "Turgescence nulle, plasmolyse totale de la motivation.",
    "Stomates fermés, aucun échange gazeux avec le cours.",
    "La sève brute ne monte pas jusqu'au cerveau.",
    "Phototropisme négatif : fuit la lumière du tableau.",
    "Reproduction asexuée de l'ennui.",
    "Un virus latent est plus actif.",
    "Le système immunitaire rejette toute forme de travail.",
    "Homéostasie du sommeil parfaitement maintenue.",
    "Réflexe myotatique absent lors de l'interrogation.",
    "Synapse en grève illimitée.",
    "Potentiel d'action : -70mV (repos total).",
    "Cortex cérébral en vacances aux Bahamas.",
    "Lobe frontal en maintenance technique."
]

# --- MAIN APP ---

def show_intro():
    st.title("🎄 SYSTEME P.R.O.F v3.0 🎅")
    st.subheader("INITIALISATION DU PROTOCOLE 'LUTIN EN RETARD'...")
    
    st.markdown("""
    <div class="matrix-text">
    > CONNECTION ÉTABLIE...<br>
    > IDENTIFICATION : <b>SOUMAYYAT</b> (Professeur SVT - Niveau Expert)<br>
    > STATUT DU LUTIN : <b>CRITIQUE</b><br>
    > CAUSE : <b>BUG DANS LA MATRICE DE NOËL / PANNE DE RÉVEIL QUANTIQUE</b><br>
    <br>
    <i>"Désolé pour le retard, j'étais coincé dans une boucle temporelle entre le 24 et le 25 décembre. 
    Mon traîneau a eu un problème de joint de culasse interdimensionnel. 
    Mais me voilà ! Prêt à rattraper le temps perdu avec une efficacité redoutable."</i>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("ACCEPTER LES EXCUSES DU LUTIN"):
        st.session_state.intro_shown = True
        st.rerun()

def main_app():
    st.title("🧬 P.R.O.F - SOUMAYYAT EDITION 🧬")
    st.markdown("---")
    
    # Feature B: Générateur de Bulletins TURBO
    st.header("📝 GÉNÉRATEUR D'APPRÉCIATIONS 'TURBO SVT'")
    st.markdown("*Algorithme calibré sur la fatigue de fin de trimestre.*")
    
    if st.button("GÉNÉRER UNE APPRÉCIATION CINGLANTE"):
        with st.spinner("Analyse du spécimen en cours..."):
            time.sleep(0.5)
            phrase = random.choice(PHRASES_SVT_TURBO)
            st.success(f"🗣️ {phrase}")
        
    st.markdown("---")
    
    # Feature C: La Cachette (Rallye Photo)
    st.header("🕵️‍♀️ RALLYE PHOTO : LA ZONE SECRÈTE")
    st.markdown("Entre le mot de passe du jour pour révéler l'indice visuel.")
    
    password_input = st.text_input("MOT DE PASSE DU JOUR", type="password")
    
    if st.button("DÉCRYPTER L'INDICE"):
        if password_input == MOT_DE_PASSE_DU_JOUR:
            st.session_state.gift_unlocked = True
            st.balloons()
        else:
            st.error("⛔ MOT DE PASSE INCORRECT. L'ADN NE CORRESPOND PAS.")
            
    if st.session_state.gift_unlocked:
        st.markdown("### 🎯 CIBLE DÉTECTÉE !")
        st.image(URL_PHOTO_DU_JOUR, caption="L'indice se trouve ici...", use_container_width=True)
        st.markdown(f"**Indice visuel chargé depuis :** `{URL_PHOTO_DU_JOUR}`")

# --- ROUTING ---
if not st.session_state.intro_shown:
    show_intro()
else:
    main_app()
