import streamlit as st

st.set_page_config(
    page_title="Master Finance Calculator",
    page_icon="📊",
    layout="wide"
)

st.markdown("""
    <style>
    .main-title {
        font-size: 2.5rem;
        color: #ff812f;
        text-align: center;
        padding: 1.5rem 0;
        background: #0e1118;
        border-radius: 10px;
        margin-bottom: 2rem;
        font-weight: bold;
    }
    .subject-header {
        color: #ff812f;
        font-size: 1.2rem;
        padding: 0.5rem 0;
        border-bottom: 2px solid #E2E8F0;
        margin-top: 1rem;
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
    .semester-selector {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-bottom: 30px;
    }
    .semester-button {
        background-color: #4f8bf9;
        color: white;
        padding: 10px 30px;
        border-radius: 20px;
        text-align: center;
        cursor: pointer;
        width: 150px;
    }
    .semester-button.active {
        background-color: #2662de;
        font-weight: bold;
    }
    .s2-color {
        color: #2fffe9;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("""
    <div class="main-title">
        Master Finance<br>Grade Calculator<br>
        <span style="font-size: 1.2rem; color: #dcdcdc;">By Sofiane Belkacem Nacer</span>
    </div>
    """, unsafe_allow_html=True)

# Define subjects and coefficients for each semester
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

# Initialize session state for semester selection
if 'current_semester' not in st.session_state:
    st.session_state.current_semester = "S1"

# Create tabs for semester selection
col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    semester_tabs = st.tabs(["Semestre 1", "Semestre 2"])

# Initialize session state for all subjects across all semesters
for subject in s1_subjects:
    exam_key = f"S1_{subject}_exam"
    td_key = f"S1_{subject}_TD"
    if exam_key not in st.session_state:
        st.session_state[exam_key] = None
    if td_key not in st.session_state:
        st.session_state[td_key] = None

for subject in s2_subjects:
    exam_key = f"S2_{subject}_exam"
    td_key = f"S2_{subject}_TD"
    if exam_key not in st.session_state:
        st.session_state[exam_key] = None
    if td_key not in st.session_state:
        st.session_state[td_key] = None

def calculate_semester_average(semester, subjects_with_coef):
    subjects_data = {}
    prefix = f"S{semester}_"
    
    for subject, coef in subjects_with_coef.items():
        exam_key = f"{prefix}{subject}_exam"
        td_key = f"{prefix}{subject}_TD"
        try:
            exam_grade = float(st.session_state.get(exam_key, 0.0) or 0.0)
            td_grade = float(st.session_state.get(td_key, 0.0) or 0.0)
            subjects_data[subject] = {"exam": exam_grade, "td": td_grade, "coef": coef}
        except (ValueError, TypeError):
            st.error(f"Entrée invalide pour {subject}. Veuillez saisir uniquement des nombres.")
            return

    total_weighted_sum = 0
    total_credits = sum(subjects_with_coef.values())
    
    for subject, data in subjects_data.items():
        average = (data["exam"] * 0.67) + (data["td"] * 0.33)
        total_weighted_sum += average * data["coef"]

    semester_average = total_weighted_sum / total_credits
    formatted_float = "{:.2f}".format(semester_average)
    better_total = "{:.2f}".format(total_weighted_sum)
    
    # Determine color based on average score
    color = "#FF0000"  # Default red for below 10
    if semester_average >= 15:
        color = "#D89CF6"  # Purple for 15 and up
    elif semester_average >= 14:
        color = "#12CAD6"  # Teal for 14-15
    elif semester_average >= 12:
        color = "#50D890"  # Green for 12-14
    elif semester_average >= 10:
        color = "#FE9801"  # Orange for 10-12
    
    st.markdown(f"""
        <div class="result-box">
            <h3 style="color: #2F855A; margin: 0;">📊 Résultats</h3>
            <p style="font-size: 1.2rem; margin: 0.5rem 0;">
                Moyenne S{semester}: <strong style="color: {color}">{formatted_float}</strong><br>
                Total: <strong>{better_total}</strong>
            </p>
        </div>
    """, unsafe_allow_html=True)

# Display subjects and input fields based on selected semester
with semester_tabs[0]:
    st.markdown("<h2 style='text-align: center;'>Semestre 1</h2>", unsafe_allow_html=True)
    
    with st.container():
        col1, col2 = st.columns(2)
        
        subjects_list = list(s1_subjects.keys())
        half = len(subjects_list) // 2
        
        for i, subject in enumerate(subjects_list):
            current_col = col1 if i < half else col2
            coef = s1_subjects[subject]
            with current_col:
                st.markdown(f'<div class="subject-header">{subject} (Coef: {coef})</div>', unsafe_allow_html=True)
                subcol1, subcol2 = st.columns(2)
                with subcol1:
                    st.number_input(
                        "Exam",
                        key=f"S1_{subject}_exam",
                        min_value=0.0,
                        value=None,
                        step=0.05,
                        format="%.2f"
                    )
                with subcol2:
                    st.number_input(
                        "TD",
                        key=f"S1_{subject}_TD",
                        min_value=0.0,
                        value=None,
                        step=0.05,
                        format="%.2f"
                    )

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Calculer la Moyenne S1"):
            calculate_semester_average(1, s1_subjects)

with semester_tabs[1]:
    st.markdown("<h2 style='text-align: center;' class='s2-color'>Semestre 2</h2>", unsafe_allow_html=True)
    
    with st.container():
        col1, col2 = st.columns(2)
        
        subjects_list = list(s2_subjects.keys())
        half = len(subjects_list) // 2
        
        for i, subject in enumerate(subjects_list):
            current_col = col1 if i < half else col2
            coef = s2_subjects[subject]
            with current_col:
                st.markdown(f'<div class="subject-header s2-color">{subject} (Coef: {coef})</div>', unsafe_allow_html=True)
                subcol1, subcol2 = st.columns(2)
                with subcol1:
                    st.number_input(
                        "Exam",
                        key=f"S2_{subject}_exam",
                        min_value=0.0,
                        value=None,
                        step=0.05,
                        format="%.2f"
                    )
                with subcol2:
                    st.number_input(
                        "TD",
                        key=f"S2_{subject}_TD",
                        min_value=0.0,
                        value=None,
                        step=0.05,
                        format="%.2f"
                    )

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Calculer la Moyenne S2"):
            calculate_semester_average(2, s2_subjects)

# Add footer with credits
st.markdown("""
<div style="text-align: center; margin-top: 50px; padding: 20px; background-color: #0e1118; border-radius: 10px;">
    <p style="color: #dcdcdc; margin: 0;">© 2025 Master Finance Grade Calculator | Created by Sofiane Belkacem Nacer</p>
</div>
""", unsafe_allow_html=True)

