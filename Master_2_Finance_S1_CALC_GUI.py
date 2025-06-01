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
    /* Removed .subject-header as expander handles titles */

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

    .s2-color { /* For S2 subject headers in expanders */
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
    
    /* Styling for NumberInput labels and boxes */
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
    
    .module-average-label { /* Label for "Moyenne" */
        font-weight: normal;
        color: #dcdcdc;
        margin-bottom: 0.2rem;
        display: block;
        font-size: 0.9rem; 
    }
    
    .module-average-display { /* The box displaying the "Moyenne" value */
        border-radius: 4px;
        border: 1px solid #4A5568;
        background-color: #1A202C; 
        padding: 0.4rem 0.6rem;
        font-size: 0.9rem; 
        height: 38px; 
        box-sizing: border-box;
        display: flex;
        align-items: center;
        opacity: 0.9; 
        width: 100%;
    }

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

    /* Expander styling */
    .stExpander > div > button { /* Target expander header button */
        font-size: 1.1rem; /* Slightly smaller than original subject-header */
        /* color: #FFCDAC; <- Removed default color here, will be set by tab */
    }
    .stExpander > div > button p { /* Target the paragraph inside the button */
        font-weight: normal; /* Make expander title normal weight if desired */
    }
    .stExpander[aria-expanded="true"] > div > button {
        /* Style for expanded header if needed */
    }
    .stExpander div[data-testid="stVerticalBlock"] { /* Content of expander */
        padding-top: 0.5rem; /* Add some padding to content */
    }
    
    /* Styling for S1 expander headers (content of the first tab) */
    section[aria-labelledby$="-tab-0"] .stExpander > div > button {
        color: #FFCDAC; /* S1 color */
    }

    /* Styling for S2 expander headers (content of the second tab) */
    section[aria-labelledby$="-tab-1"] .stExpander > div > button {
        color: #E6BEA3; /* S2 color */
    }
    /* Removed .s2-expander rule as it's no longer used */

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

s1_subjects_coef = {
    "Théorie de la Décision et des Jeux": 3, "Stratégie d'Entreprise": 3, "Théorie Financière": 3,
    "Marchés des Capitaux": 3, "Comptabilité Approfondie": 3, "PMO": 3, "Séries Temporelles": 3,
    "Systèmes d'Information": 3, "Contrôle de Gestion": 3, "Technique Bancaires": 3
}

s2_subjects_coef = {
    "Économie de l'information": 1.5, "Stage": 3, "Droit pénal des affaires": 3, "Économie managériale": 3,
    "Initiation à la méthodologie": 1.5, "Économie monétaire": 3, "Gestion de portefeuille": 3,
    "Évaluation des projets d'investissement": 3, "Analyse et conception de systèmes d'information": 3,
    "Convexité et optimisation": 3, "Modèles stochastiques": 3
}

for subject in s1_subjects_coef.keys():
    exam_key = f"S1_{subject}_exam"
    td_key = f"S1_{subject}_TD"
    module_avg_key = f"S1_{subject}_module_avg"
    if exam_key not in st.session_state: st.session_state[exam_key] = None
    if td_key not in st.session_state: st.session_state[td_key] = None
    if module_avg_key not in st.session_state: st.session_state[module_avg_key] = 0.0

for subject in s2_subjects_coef.keys():
    exam_key = f"S2_{subject}_exam"
    td_key = f"S2_{subject}_TD"
    module_avg_key = f"S2_{subject}_module_avg"
    if exam_key not in st.session_state: st.session_state[exam_key] = None
    if td_key not in st.session_state: st.session_state[td_key] = None
    if module_avg_key not in st.session_state: st.session_state[module_avg_key] = 0.0

def calculate_and_store_module_average(prefix, subject_name):
    exam_key = f"{prefix}_{subject_name}_exam"
    td_key = f"{prefix}_{subject_name}_TD"
    module_avg_storage_key = f"{prefix}_{subject_name}_module_avg"

    exam_grade_val = st.session_state.get(exam_key)
    td_grade_val = st.session_state.get(td_key)

    try: exam_grade_float = float(exam_grade_val) if exam_grade_val is not None else 0.0
    except (ValueError, TypeError): exam_grade_float = 0.0
    
    try: td_grade_float = float(td_grade_val) if td_grade_val is not None else 0.0
    except (ValueError, TypeError): td_grade_float = 0.0
    
    exam_grade_float = max(0.0, min(20.0, exam_grade_float))
    td_grade_float = max(0.0, min(20.0, td_grade_float))

    average = (exam_grade_float * 0.67) + (td_grade_float * 0.33)
    st.session_state[module_avg_storage_key] = average

def calculate_semester_average(semester_num, subjects_with_coef_map):
    prefix = f"S{semester_num}"
    total_weighted_sum = 0
    total_credits = sum(subjects_with_coef_map.values())
    
    for subject, coef in subjects_with_coef_map.items():
        module_avg_key = f"{prefix}_{subject}_module_avg"
        if st.session_state.get(f"{prefix}_{subject}_exam") is not None or \
           st.session_state.get(f"{prefix}_{subject}_TD") is not None:
            calculate_and_store_module_average(prefix, subject)
            
        module_avg = float(st.session_state.get(module_avg_key, 0.0))
        total_weighted_sum += module_avg * coef

    semester_average = total_weighted_sum / total_credits if total_credits else 0
    formatted_float = "{:.2f}".format(semester_average)
    
    color = "#FF0000"  
    if semester_average >= 15: color = "#D89CF6"  
    elif semester_average >= 14: color = "#12CAD6"  
    elif semester_average >= 12: color = "#50D890"  
    elif semester_average >= 10: color = "#FE9801"  
    
    st.markdown(f"""
        <div class="result-box">
            <h3 style="color: #2F855A; margin: 0;">📊 Résultats Semestre {semester_num}</h3>
            <p style="font-size: 1.2rem; margin: 0.5rem 0;">
                Moyenne S{semester_num}: <strong style="color: {color}">{formatted_float}</strong>
            </p>
        </div>
    """, unsafe_allow_html=True)

col_tabs_outer1, col_tabs_main, col_tabs_outer2 = st.columns([0.5, 3, 0.5])
with col_tabs_main:
    semester_tabs = st.tabs(["Semestre 1", "Semestre 2"])

with semester_tabs[0]:
    st.markdown("<h2 style='text-align: center; color: #FFCDAC;'>Semestre 1</h2>", unsafe_allow_html=True)
    
    s1_list = list(s1_subjects_coef.keys())
    half_s1 = len(s1_list) // 2
    col_s1_left, col_s1_right = st.columns(2)

    for i, subject in enumerate(s1_list):
        current_column = col_s1_left if i < half_s1 else col_s1_right
        with current_column:
            coef = s1_subjects_coef[subject]
            with st.expander(f"{subject} (Coef: {coef})", expanded=True):
                exam_key_s1 = f"S1_{subject}_exam"
                td_key_s1 = f"S1_{subject}_TD"
                module_avg_key_s1 = f"S1_{subject}_module_avg"

                subcol_exam, subcol_td, subcol_avg = st.columns(3)
                with subcol_exam:
                    st.number_input("Exam", key=exam_key_s1, min_value=0.0, max_value=20.0,
                                    value=st.session_state.get(exam_key_s1), step=0.05, format="%.2f",
                                    on_change=calculate_and_store_module_average, args=("S1", subject), label_visibility="collapsed")
                with subcol_td:
                    st.number_input("TD", key=td_key_s1, min_value=0.0, max_value=20.0,
                                    value=st.session_state.get(td_key_s1), step=0.05, format="%.2f",
                                    on_change=calculate_and_store_module_average, args=("S1", subject), label_visibility="collapsed")
                with subcol_avg:
                    avg_val = float(st.session_state.get(module_avg_key_s1, 0.0))
                    avg_color = "#FF0000" 
                    if avg_val >= 15: avg_color = "#D89CF6" 
                    elif avg_val >= 10: avg_color = "#50D890" 
                    elif avg_val >= 7: avg_color = "#4682B4"
                    
                    module_avg_html = f"""
                    <div style="margin-top: 0rem;">
                        {'' if avg_val == 0.0 else '<label class="module-average-label">Moyenne</label>'}
                        <div class="module-average-display" style="color: {avg_color};">
                            {avg_val:.2f}
                        </div>
                    </div>
                    """
                    st.markdown(module_avg_html, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    btn_col_s1_1, btn_col_s1_2, btn_col_s1_3 = st.columns([1,1,1])
    with btn_col_s1_2:
        if st.button("Calculer Moyenne S1", key="calc_s1_btn", use_container_width=True):
            calculate_semester_average(1, s1_subjects_coef)

with semester_tabs[1]:
    st.markdown("<h2 style='text-align: center;' class='s2-color'>Semestre 2</h2>", unsafe_allow_html=True)

    s2_list = list(s2_subjects_coef.keys())
    half_s2 = len(s2_list) // 2
    col_s2_left, col_s2_right = st.columns(2)

    for i, subject in enumerate(s2_list):
        current_column = col_s2_left if i < half_s2 else col_s2_right
        # REMOVED: current_column.markdown('<div class="s2-expander">', unsafe_allow_html=True)
        with current_column: 
            coef = s2_subjects_coef[subject]
            with st.expander(f"{subject} (Coef: {coef})", expanded=True):
                exam_key_s2 = f"S2_{subject}_exam"
                td_key_s2 = f"S2_{subject}_TD"
                module_avg_key_s2 = f"S2_{subject}_module_avg"

                subcol_exam, subcol_td, subcol_avg = st.columns(3)
                with subcol_exam:
                    st.number_input("Exam",key=exam_key_s2, min_value=0.0, max_value=20.0,
                                    value=st.session_state.get(exam_key_s2), step=0.05, format="%.2f",
                                    on_change=calculate_and_store_module_average, args=("S2", subject), label_visibility="collapsed")
                with subcol_td:
                    st.number_input("TD", key=td_key_s2, min_value=0.0, max_value=20.0,
                                    value=st.session_state.get(td_key_s2), step=0.05, format="%.2f",
                                    on_change=calculate_and_store_module_average, args=("S2", subject), label_visibility="collapsed")
                with subcol_avg:
                    avg_val = float(st.session_state.get(module_avg_key_s2, 0.0))
                    avg_color = "#FF0000"
                    if avg_val >= 15: avg_color = "#D89CF6"
                    elif avg_val >= 10: avg_color = "#50D890"
                    elif avg_val >= 7: avg_color = "#4682B4"
                    
                    module_avg_html = f"""
                    <div style="margin-top: 0rem;">
                        {'' if avg_val == 0.0 else '<label class="module-average-label">Moyenne</label>'}
                        <div class="module-average-display" style="color: {avg_color};">
                            {avg_val:.2f}
                        </div>
                    </div>
                    """
                    st.markdown(module_avg_html, unsafe_allow_html=True)
        # REMOVED: current_column.markdown('</div>', unsafe_allow_html=True) 


    st.markdown("<br>", unsafe_allow_html=True)
    btn_col_s2_1, btn_col_s2_2, btn_col_s2_3 = st.columns([1,1,1])
    with btn_col_s2_2:
        if st.button("Calculer Moyenne S2", key="calc_s2_btn", use_container_width=True):
            calculate_semester_average(2, s2_subjects_coef)

st.markdown("""
<div style="text-align: center; margin-top: 50px; padding: 20px; background-color: #0e1118; border-radius: 10px;">
    <p style="color: #dcdcdc; margin: 0;">© 2025 Master Finance Grade Calculator | Created by Sofiane Belkacem Nacer</p>
</div>
""", unsafe_allow_html=True)
