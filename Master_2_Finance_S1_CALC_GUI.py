import streamlit as st


st.set_page_config(
    page_title="Master 2 Finance Calculator",
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
    </style>
    """, unsafe_allow_html=True)

st.markdown("""
    <div class="main-title">
        Master 2 Finance - S1 Grade Calculator<br>
        <span style="font-size: 1.2rem; color: #dcdcdc;">By Sofiane Belkacem Nacer</span>
    </div>
    """, unsafe_allow_html=True)

subjects = [
    "Théorie de la Décision et des Jeux", "Stratégie d'Entreprise", "Théorie Financière",
    "Marchés des Capitaux", "Comptabilité Approfondie", "PMO", "Séries Temporelles",
    "Systèmes d'Information", "Contrôle de Gestion", "Technique Bancaires"
]

for subject in subjects:
    exam_key = f"{subject}_exam"
    td_key = f"{subject}_TD"
    if exam_key not in st.session_state:
        st.session_state[exam_key] = None
    if td_key not in st.session_state:
        st.session_state[td_key] = None

def calculate_semester_average():
    subjects_data = {}
    for subject in subjects:
        exam_key = f"{subject}_exam"
        td_key = f"{subject}_TD"
        try:
            exam_grade = float(st.session_state.get(exam_key, 0.0) or 0.0)
            td_grade = float(st.session_state.get(td_key, 0.0) or 0.0)
            subjects_data[subject] = {"exam": exam_grade, "td": td_grade}
        except (ValueError, TypeError):
            st.error(f"Entrée invalide pour {subject}. Veuillez saisir uniquement des nombres.")
            return

    total = 0
    for subject, grades in subjects_data.items():
        average = (grades["exam"] * 0.67) + (grades["td"] * 0.33)
        weight = 3  
        total += average * weight

    semester_average = total / 30
    formatted_float = "{:.2f}".format(semester_average)
    better_total = "{:.2f}".format(total)
    
    st.markdown(f"""
        <div class="result-box">
            <h3 style="color: #2F855A; margin: 0;">📊 Résultats</h3>
            <p style="font-size: 1.2rem; margin: 0.5rem 0;">
                Moyenne Semestrielle: <strong>{formatted_float}</strong><br>
                Total: <strong>{better_total}</strong>
            </p>
        </div>
    """, unsafe_allow_html=True)


with st.container():
    col1, col2 = st.columns(2)
    
    half = len(subjects) // 2
    
    for i, subject in enumerate(subjects):
        current_col = col1 if i < half else col2
        with current_col:
            st.markdown(f'<div class="subject-header">{subject}</div>', unsafe_allow_html=True)
            subcol1, subcol2 = st.columns(2)
            with subcol1:
                st.number_input(
                    "Exam",
                    key=f"{subject}_exam",
                    min_value=0.0,
                    value=None,
                    step=0.05,
                    format="%.2f"
                )
            with subcol2:
                st.number_input(
                    "TD",
                    key=f"{subject}_TD",
                    min_value=0.0,
                    value=None,
                    step=0.05,
                    format="%.2f"
                )

st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("Calculer la moyenne"):
        calculate_semester_average()
