import streamlit as st

st.set_page_config(
    page_title="Master Finance Calculator",
    page_icon="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fcdn2.iconfinder.com%2Fdata%2Ficons%2Fcurrency-32%2F55%2Fcurrency-18-4096.png&f=1&nofb=1&ipt=925920844e55526262ccb6bc80b9f2cecfa279d58f8d79f576f16b989b686d43",
    layout="wide"
)

st.markdown("""
    <style>
    .main-title {
        font-size: 2.5rem;
        color: #FFCDAC;
        text-align: center;
        padding: 1.5rem 0;
        background: #0e1118;
        border-radius: 10px;
        margin-bottom: 2rem;
        font-weight: bold;
    }
    .subject-header {
        color: #FFCDAC;
        font-size: 1.2rem;
        padding: 0.5rem 0;
        border-bottom: 2px solid #E2E8F0;
        margin-top: 1rem;
        margin-bottom: 0.5rem; /* Space before inputs */
    }
    .stButton > button {
        width: 100%;
        background-color: #ff812f;
        color: white;
    }
    .result-box {
        padding: 1rem;
        border-radius: 5px;
        margin-top: 1rem;
        background-color: #0e1118;
        border: 1px solid #48BB78;
    }
    .semester-selector { /* This class seems unused in the provided reverted code, keeping for reference */
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-bottom: 30px;
    }
    .semester-button { /* This class seems unused, keeping for reference */
        background-color: #4f8bf9;
        color: white;
        padding: 10px 30px;
        border-radius: 20px;
        text-align: center;
        cursor: pointer;
        width: 150px;
    }
    .semester-button.active { /* This class seems unused, keeping for reference */
        background-color: #2662de;
        font-weight: bold;
    }
    .s2-color { /* For S2 subject headers */
        color: #E6BEA3 !important; 
    }
    
    /* Corner GIF Styles */
    .corner-gif {
        position: fixed;
        top: 85px;
        right: 10px;
        z-index: 9999;
        width: 80px;
        height: 80px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.3);
        opacity: 0.8;
        transition: opacity 0.3s ease;
    }
    .corner-gif:hover {
        opacity: 1;
        transform: scale(1.1);
        transition: all 0.3s ease;
    }
    
    /* Styling for NumberInput labels and boxes - general styling */
    div[data-testid="stNumberInput"] > label {
        font-weight: normal;
        color: #dcdcdc; 
        margin-bottom: 0.2rem;
        display: block;
        font-size: 0.9rem;
    }

    div[data-testid="stNumberInput"] input {
        border-radius: 4px;
        border: 1px solid #4A5568; 
        background-color: #1A202C; 
        color: #E2E8F0;            
        padding: 0.4rem 0.6rem;
        height: 38px; 
        box-sizing: border-box; 
        width: 100%; 
    }

    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
        justify-content: center;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        padding: 0px 24px;
        background-color: #262730; 
        border-radius: 10px 10px 0px 0px;
        color: white;
        font-weight: bold;
    }
    .stTabs [aria-selected="true"] {
        background-color: #ff812f; 
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("""
    <img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fbestanimations.com%2FAnimals%2FMammals%2FCats%2Fcats%2Fcute-kitty-animated-gif-61.gif&f=1&nofb=1&ipt=9b9f49feca4c1a8d04b816cebb11048d1cba7254539b845380dd510c43cb5d4e" class="corner-gif" alt="Finance GIF">
    """, unsafe_allow_html=True)

st.markdown("""
    <div class="main-title">
        Master Finance<br>Grade Calculator<br>
        <span style="font-size: 1.2rem; color: #dcdcdc;">By Sofiane Belkacem Nacer</span>
    </div>
    """, unsafe_allow_html=True)

s1_subjects_coef = { # Renamed to s1_subjects_coef for clarity with S2
    "Théorie de la Décision et des Jeux": 3,
    "Stratégie d'Entreprise": 3,
    "Théorie Financière": 3,
    "Marchés des Capitaux": 3,
    "Comptabilité Approfondie": 3,
    "PMO": 3,
    "Séries Temporelles": 3,
    "Systèmes d'Information": 3,
    "Contrôle de Gestion": 3,
    "Technique Bancaires": 3
}

s2_subjects_coef = { # Renamed to s2_subjects_coef for clarity with S1
    "Économie de l'information": 1.5,
    "Stage": 3,
    "Droit pénal des affaires": 3,
    "Économie managériale": 3,
    "Initiation à la méthodologie": 1.5,
    "Économie monétaire": 3,
    "Gestion de portefeuille": 3,
    "Évaluation des projets d'investissement": 3,
    "Analyse et conception de systèmes d'information": 3,
    "Convexité et optimisation": 3,
    "Modèles stochastiques": 3
}

# Session state initialization (only for exam and TD)
for subject in s1_subjects_coef.keys(): # Use .keys() for clarity
    exam_key = f"S1_{subject}_exam"
    td_key = f"S1_{subject}_TD"
    if exam_key not in st.session_state:
        st.session_state[exam_key] = None
    if td_key not in st.session_state:
        st.session_state[td_key] = None

for subject in s2_subjects_coef.keys(): # Use .keys() for clarity
    exam_key = f"S2_{subject}_exam"
    td_key = f"S2_{subject}_TD"
    if exam_key not in st.session_state:
        st.session_state[exam_key] = None
    if td_key not in st.session_state:
        st.session_state[td_key] = None

def calculate_semester_average(semester_num, subjects_map): # Parameter name changed for clarity
    subjects_data = {}
    prefix = f"S{semester_num}_" # Corrected prefix to S1_ or S2_
    
    for subject, coef in subjects_map.items():
        exam_key = f"{prefix}{subject}_exam"
        td_key = f"{prefix}{subject}_TD"
        try:
            exam_grade = float(st.session_state.get(exam_key, 0.0) or 0.0)
            td_grade = float(st.session_state.get(td_key, 0.0) or 0.0)
            # Input validation
            if not (0 <= exam_grade <= 20 and 0 <= td_grade <= 20):
                st.error(f"Les notes pour '{subject}' doivent être entre 0 et 20.")
                # Optionally clear the invalid inputs or mark them as invalid for processing
                st.session_state[exam_key] = 0.0 
                st.session_state[td_key] = 0.0
                exam_grade, td_grade = 0.0, 0.0 # Reset for calculation if error
                # return # Could also return here to stop calculation on error

            subjects_data[subject] = {"exam": exam_grade, "td": td_grade, "coef": coef}
        except (ValueError, TypeError):
            st.error(f"Entrée invalide pour {subject}. Veuillez saisir uniquement des nombres.")
            return # Stop calculation if there's a non-numeric input

    total_weighted_sum = 0
    total_credits = sum(subjects_map.values())
    if total_credits == 0:
        st.error("Total des crédits est zéro. Impossible de calculer la moyenne.")
        return

    for subject, data in subjects_data.items():
        average = (data["exam"] * 0.67) + (data["td"] * 0.33)
        total_weighted_sum += average * data["coef"]

    semester_average = total_weighted_sum / total_credits if total_credits else 0
    formatted_float = "{:.2f}".format(semester_average)
    # better_total = "{:.2f}".format(total_weighted_sum) # This was in original, but not used in result display
    
    color = "#FF0000"  
    if semester_average >= 15: color = "#D89CF6"  
    elif semester_average >= 14: color = "#12CAD6"  
    elif semester_average >= 12: color = "#50D890"  
    elif semester_average >= 10: color = "#FE9801"  
    
    st.markdown(f"""
        <div class="result-box">
            <h3 style="color: #2F855A; margin: 0;">📊 Résultats Semestre {semester_num}</h3>
            <p style="font-size: 1.2rem; margin: 0.5rem 0;">
                Moyenne S{semester_num}: <strong style="color: {color}">{formatted_float}</strong><br>
                {'' if semester_num == 2 else f"Total Points Pondérés: <strong>{total_weighted_sum:.2f}</strong>"}
            </p>
        </div>
    """, unsafe_allow_html=True)

# Using columns to center the tabs
col_tabs_outer1, col_tabs_main, col_tabs_outer2 = st.columns([0.5, 3, 0.5]) 
with col_tabs_main:
    semester_tabs = st.tabs(["Semestre 1", "Semestre 2"])

with semester_tabs[0]:
    st.markdown("<h2 style='text-align: center; color: #FFCDAC;'>Semestre 1</h2>", unsafe_allow_html=True)

    # Using two columns for S1 subjects layout
    s1_list = list(s1_subjects_coef.keys())
    half_s1 = len(s1_list) // 2
    col_s1_left, col_s1_right = st.columns(2)

    for i, subject in enumerate(s1_list):
        current_column = col_s1_left if i < half_s1 else col_s1_right
        with current_column:
            coef = s1_subjects_coef[subject]
            st.markdown(f'<div class="subject-header">{subject} (Coef: {coef})</div>', unsafe_allow_html=True)

            # Exam and TD inputs in two sub-columns
            sub_col_exam, sub_col_td = st.columns(2)
            with sub_col_exam:
                st.number_input(
                    "Exam", key=f"S1_{subject}_exam", min_value=0.0, max_value=20.0,
                    value=st.session_state.get(f"S1_{subject}_exam"), step=0.05, format="%.2f"
                )
            with sub_col_td:
                st.number_input(
                    "TD", key=f"S1_{subject}_TD", min_value=0.0, max_value=20.0,
                    value=st.session_state.get(f"S1_{subject}_TD"), step=0.05, format="%.2f"
                )

    st.markdown("<br>", unsafe_allow_html=True)
    # Centering the button for S1
    btn_col_s1_1, btn_col_s1_2, btn_col_s1_3 = st.columns([1,1,1]) 
    with btn_col_s1_2:
        if st.button("Calculer Moyenne S1", key="calc_s1_btn", use_container_width=True):
            calculate_semester_average(1, s1_subjects_coef)

with semester_tabs[1]:
    st.markdown("<h2 style='text-align: center;' class='s2-color'>Semestre 2</h2>", unsafe_allow_html=True)

    # Using two columns for S2 subjects layout
    s2_list = list(s2_subjects_coef.keys())
    half_s2 = len(s2_list) // 2
    col_s2_left, col_s2_right = st.columns(2)

    for i, subject in enumerate(s2_list):
        current_column = col_s2_left if i < half_s2 else col_s2_right
        with current_column:
            coef = s2_subjects_coef[subject]
            # Added s2-color class for S2 subject headers
            st.markdown(f'<div class="subject-header s2-color">{subject} (Coef: {coef})</div>', unsafe_allow_html=True)

            # Exam and TD inputs in two sub-columns
            sub_col_exam, sub_col_td = st.columns(2)
            with sub_col_exam:
                st.number_input(
                    "Exam", key=f"S2_{subject}_exam", min_value=0.0, max_value=20.0,
                    value=st.session_state.get(f"S2_{subject}_exam"), step=0.05, format="%.2f"
                )
            with sub_col_td:
                st.number_input(
                    "TD", key=f"S2_{subject}_TD", min_value=0.0, max_value=20.0,
                    value=st.session_state.get(f"S2_{subject}_TD"), step=0.05, format="%.2f"
                )

    st.markdown("<br>", unsafe_allow_html=True)
    # Centering the button for S2
    btn_col_s2_1, btn_col_s2_2, btn_col_s2_3 = st.columns([1,1,1])
    with btn_col_s2_2:
        if st.button("Calculer Moyenne S2", key="calc_s2_btn", use_container_width=True):
            calculate_semester_average(2, s2_subjects_coef)

st.markdown("""
<div style="text-align: center; margin-top: 50px; padding: 20px; background-color: #0e1118; border-radius: 10px;">
    <p style="color: #dcdcdc; margin: 0;">© 2025 Master Finance Grade Calculator | Created by Sofiane Belkacem Nacer</p>
</div>
""", unsafe_allow_html=True)
