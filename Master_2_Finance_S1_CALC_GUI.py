import streamlit as st

st.set_page_config(
    page_title="Master Finance Calculator",
    page_icon="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fcdn2.iconfinder.com%2Fdata%2Ficons%2Fcurrency-32%2F55%2Fcurrency-18-4096.png&f=1&nofb=1&ipt=925920844e55526262ccb6bc80b9f2cecfa279d58f8d79f576f16b989b686d43",
    layout="wide"
)

st.markdown("""
    <style>
    /* Main page and component styles */
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
        margin-bottom: 0.5rem; /* Added for spacing before inputs */
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
    .semester-selector { /* Unused in current Python, kept for reference */
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-bottom: 30px;
    }
    .semester-button { /* Unused in current Python, kept for reference */
        background-color: #4f8bf9;
        color: white;
        padding: 10px 30px;
        border-radius: 20px;
        text-align: center;
        cursor: pointer;
        width: 150px;
    }
    .semester-button.active { /* Unused in current Python, kept for reference */
        background-color: #2662de;
        font-weight: bold;
    }
    .s2-color { /* For S2 specific elements */
        color: #E6BEA3 !important; /* Important to ensure override */
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
        transition: opacity 0.3s ease, transform 0.3s ease; /* Combined transition */
    }
    .corner-gif:hover {
        opacity: 1;
        transform: scale(1.1);
    }

    /* Alternative: Bottom right corner GIF (unused in current HTML) */
    .corner-gif-bottom {
        position: fixed;
        bottom: 20px;
        right: 20px;
        z-index: 9999;
        width: 60px;
        height: 60px;
        border-radius: 50%;
        box-shadow: 0 4px 8px rgba(0,0,0,0.3);
        opacity: 0.7;
    }

    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
        justify-content: center;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        padding: 0px 24px;
        background-color: #262730; /* Default tab color */
        border-radius: 10px 10px 0px 0px;
        color: white;
        font-weight: bold;
    }
    .stTabs [aria-selected="true"] {
        background-color: #ff812f; /* Active tab color */
    }
    
    /* Input styling */
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
        /* height: 38px; /* Consider if explicit height is needed across all apps */
        box-sizing: border-box; 
        width: 100%; 
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

s1_subjects = {
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

s2_subjects = {
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

if 'current_semester' not in st.session_state: # This session state variable seems unused
    st.session_state.current_semester = "S1"

# Initialize session state for S1 subjects
for subject in s1_subjects.keys():
    exam_key = f"S1_{subject}_exam" # Standardized key
    td_key = f"S1_{subject}_TD"   # Standardized key
    if exam_key not in st.session_state:
        st.session_state[exam_key] = None
    if td_key not in st.session_state:
        st.session_state[td_key] = None

# Initialize session state for S2 subjects
for subject in s2_subjects.keys():
    exam_key = f"S2_{subject}_exam" # Standardized key
    td_key = f"S2_{subject}_TD"   # Standardized key
    if exam_key not in st.session_state:
        st.session_state[exam_key] = None
    if td_key not in st.session_state:
        st.session_state[td_key] = None

def calculate_semester_average(semester_num, subjects_with_coef): # Renamed 'semester' to 'semester_num'
    subjects_data = {}
    prefix = f"S{semester_num}_" # Now correctly S1_ or S2_
    
    for subject, coef in subjects_with_coef.items():
        exam_key = f"{prefix}{subject}_exam" # Uses standardized key
        td_key = f"{prefix}{subject}_TD"   # Uses standardized key
        try:
            exam_grade = float(st.session_state.get(exam_key, 0.0) or 0.0)
            td_grade = float(st.session_state.get(td_key, 0.0) or 0.0)
            
            if not (0 <= exam_grade <= 20 and 0 <= td_grade <= 20):
                st.error(f"Les notes pour '{subject}' (S{semester_num}) doivent être entre 0 et 20.")
                # return # Optionally stop calculation on error
            subjects_data[subject] = {"exam": exam_grade, "td": td_grade, "coef": coef}
        except (ValueError, TypeError):
            st.error(f"Entrée invalide pour {subject} (S{semester_num}). Veuillez saisir uniquement des nombres.")
            return

    total_weighted_sum = 0
    total_credits = sum(subjects_with_coef.values())
    if total_credits == 0:
        st.error("Total des crédits est zéro. Impossible de calculer la moyenne.")
        return

    for subject, data in subjects_data.items():
        average = (data["exam"] * 0.67) + (data["td"] * 0.33)
        total_weighted_sum += average * data["coef"]

    semester_average = total_weighted_sum / total_credits if total_credits else 0.0
    formatted_float = "{:.2f}".format(semester_average)
    # better_total = "{:.2f}".format(total_weighted_sum) # This was in original, not used in the original result display

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
                Total Points Pondérés: <strong>{total_weighted_sum:.2f}</strong> {/* Added total points */}
            </p>
        </div>
    """, unsafe_allow_html=True)

# Centering the tabs
col_tabs_outer1, col_tabs_main, col_tabs_outer2 = st.columns([0.5, 3, 0.5])
with col_tabs_main:
    semester_tabs = st.tabs(["Semestre 1", "Semestre 2"])

with semester_tabs[0]:
    st.markdown("<h2 style='text-align: center; color: #FFCDAC;'>Semestre 1</h2>", unsafe_allow_html=True)
    
    subjects_list_s1 = list(s1_subjects.keys())
    half_s1 = len(subjects_list_s1) // 2
    col_s1_left, col_s1_right = st.columns(2) # Two columns for S1 subject layout

    for i, subject in enumerate(subjects_list_s1):
        current_column = col_s1_left if i < half_s1 else col_s1_right
        with current_column:
            coef = s1_subjects[subject]
            st.markdown(f'<div class="subject-header">{subject} (Coef: {coef})</div>', unsafe_allow_html=True)

            col_exam, col_td = st.columns(2)
            with col_exam:
                st.number_input(
                    "Exam", key=f"S1_{subject}_exam", min_value=0.0, max_value=20.0,
                    value=st.session_state.get(f"S1_{subject}_exam"), step=0.05, format="%.2f"
                )
            with col_td:
                st.number_input(
                    "TD", key=f"S1_{subject}_TD", min_value=0.0, max_value=20.0,
                    value=st.session_state.get(f"S1_{subject}_TD"), step=0.05, format="%.2f"
                )

    st.markdown("<br>", unsafe_allow_html=True)
    # Centering the S1 button
    btn_col_s1_center_1, btn_col_s1_center_2, btn_col_s1_center_3 = st.columns([1, 2, 1])
    with btn_col_s1_center_2:
        if st.button("Calculer la Moyenne S1", key="calc_s1", use_container_width=True): # Added key and use_container_width
            calculate_semester_average(1, s1_subjects)

with semester_tabs[1]:
    st.markdown("<h2 style='text-align: center;' class='s2-color'>Semestre 2</h2>", unsafe_allow_html=True)
    
    subjects_list_s2 = list(s2_subjects.keys())
    half_s2 = len(subjects_list_s2) // 2
    col_s2_left, col_s2_right = st.columns(2) # Two columns for S2 subject layout

    for i, subject in enumerate(subjects_list_s2):
        current_column = col_s2_left if i < half_s2 else col_s2_right
        with current_column:
            coef = s2_subjects[subject]
            st.markdown(f'<div class="subject-header s2-color">{subject} (Coef: {coef})</div>', unsafe_allow_html=True)

            col_exam, col_td = st.columns(2) # Renamed for clarity within S2 loop
            with col_exam:
                st.number_input(
                    "Exam", key=f"S2_{subject}_exam", min_value=0.0, max_value=20.0,
                    value=st.session_state.get(f"S2_{subject}_exam"), step=0.05, format="%.2f"
                )
            with col_td:
                st.number_input(
                    "TD", key=f"S2_{subject}_TD", min_value=0.0, max_value=20.0,
                    value=st.session_state.get(f"S2_{subject}_TD"), step=0.05, format="%.2f"
                )

    st.markdown("<br>", unsafe_allow_html=True)
    # Centering the S2 button
    btn_col_s2_center_1, btn_col_s2_center_2, btn_col_s2_center_3 = st.columns([1, 2, 1])
    with btn_col_s2_center_2:
        if st.button("Calculer la Moyenne S2", key="calc_s2", use_container_width=True): # Added key and use_container_width
            calculate_semester_average(2, s2_subjects)

st.markdown("""
    <div style="text-align: center; margin-top: 50px; padding: 20px; background-color: #0e1118; border-radius: 10px;">
        <p style="color: #dcdcdc; margin: 0;">© 2025 Master Finance Grade Calculator | Created by Sofiane Belkacem Nacer</p>
    </div>
    """, unsafe_allow_html=True)
