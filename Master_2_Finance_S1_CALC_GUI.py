import streamlit as st


for subject in [
    "Théorie de la Décision et des Jeux","Stratégie d'Entreprise", "Théorie Financière",
    "Marchés des Capitaux", "Comptabilité Approfondie", "PMO","Séries Temporelles",
    "Systèmes d'Information", "Contrôle de Gestion", "Technique Bancaires"
]:
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

        except ValueError:
            st.error(f"Invalid input for {subject}. Please enter numbers only.")
            return  
        except TypeError:
            st.error(f"Invalid input for {subject}. Please enter numbers only.")
            return  

    total = 0
    for subject, grades in subjects_data.items():
        average = (grades["exam"] * 0.67) + (grades["td"] * 0.33)  
        weight = 3 if subject in [ "Théorie de la Décision et des Jeux","Stratégie d'Entreprise", "Théorie Financière",
                                   "Marchés des Capitaux", "Comptabilité Approfondie", "PMO","Séries Temporelles",
                                   "Systèmes d'Information", "Contrôle de Gestion", "Technique Bancaires"] else 3
        total += average * weight

    semester_average = total / 30
    formatted_float = "{:.2f}".format(semester_average)
    better_total = "{:.2f}".format(total)

    st.success(f"Moyenne Semestrielle Estimée: {formatted_float}")
    st.success(f"Total: {better_total}")


# Streamlit app
st.title("Master 2 Finance - S1 Grade Calculator ~ By Sofiane Belkacem Nacer")

subjects = [
     "Théorie de la Décision et des Jeux","Stratégie d'Entreprise", "Théorie Financière",
     "Marchés des Capitaux", "Comptabilité Approfondie", "PMO","Séries Temporelles",
     "Systèmes d'Information", "Contrôle de Gestion", "Technique Bancaires" 
]

for subject in subjects:
    st.subheader(subject)  
    col1, col2 = st.columns(2)
    with col1:
        st.number_input(
            "Exam",  
            key=f"{subject}_exam", 
            min_value=0.0, 
            value=None,  
            step=0.05,  
            format="%.2f"  
        )
    with col2:
        st.number_input(
            "TD", 
            key=f"{subject}_TD", 
            min_value=0.0, 
            value=None,  
            step=0.05,  
            format="%.2f"  
        )

if st.button("Calculate"):
    calculate_semester_average()

