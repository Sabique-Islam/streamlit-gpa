import streamlit as st

MARKING = {'S': 10, 'A': 9, 'B': 8, 'C': 7, 'D': 6, 'E': 5, 'F': 4, 'W': 0, 'AP': 0, 'AF': 0}
CREDITS = {
    "physics": [5, 4, 4, 5, 2, 4],
    "chemistry": [5, 4, 4, 5, 2, 4]
}

def load_css():
    st.markdown(
        """
        <style>
        body {
            color: #ffffff;
            background-color: #0e1117;
        }
        .css-1d391kg {
            background-color: #1e1e1e;
        }
        .stSelectbox, .stRadio > div {
            background-color: #1e1e1e;
            color: #ffffff;
            border: 1px solid #444;
            border-radius: 8px;
            padding: 10px;
        }
        .stButton > button {
            background-color: #2563eb;
            color: white;
            border-radius: 8px;
            padding: 10px 20px;
            border: none;
            font-weight: bold;
        }
        .stButton > button:hover {
            background-color: #1d4ed8;
        }
        .stSuccess {
            background-color: #14532d;
            color: #ffffff;
            border-radius: 8px;
            padding: 10px;
        }
        .stError {
            background-color: #7f1d1d;
            color: #ffffff;
            border-radius: 8px;
            padding: 10px;
        }
        /* Header and subheader */
        h1, h2, h3 {
            color: #ffffff;
        }
        .card {
            background-color: #1e1e1e;
            border-radius: 8px;
            padding: 20px;
            margin: 10px 0;
            border: 1px solid #444;
        }
        .stRadio > div > label > div:first-child {
            background-color: #1e1e1e !important;
            border: 2px solid #00FFFF !important;
        }
        .stRadio > div > label > div:first-child:hover {
            border-color: #00FFFF !important;
        }
        .stRadio > div > label > div:first-child > div {
            background-color: #00FFFF !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

def main():
    load_css()

    st.title("🎓 GPA Calculator")
    st.markdown("Calculate your GPA effortlessly with a modern and sleek interface.")

    cycle = st.radio("Select your cycle:", ('Physics', 'Chemistry'), horizontal=True)
    st.subheader("📝 Enter your grades:")
    col1, col2 = st.columns(2)
    with col1:
        maths = st.selectbox("Maths", list(MARKING.keys()), index=0)
        cse = st.selectbox("CSE", list(MARKING.keys()), index=0)
    with col2:
        if cycle == "Physics":
            ele_subject = st.selectbox("Elements of Electrical Engineering", list(MARKING.keys()), index=0)
            eng_subject = st.selectbox("Engineering Physics and Physics Laboratory", list(MARKING.keys()), index=0)
        else:
            ele_subject = st.selectbox("Electronic Principles and Devices", list(MARKING.keys()), index=0)
            eng_subject = st.selectbox("Engineering Chemistry and Chemistry Laboratory", list(MARKING.keys()), index=0)

    col3, col4 = st.columns(2)
    with col3:
        if cycle == "Physics":
            evs_constitution = st.selectbox("Environmental Studies and Life Sciences", list(MARKING.keys()), index=0)
        else:
            evs_constitution = st.selectbox("Constitution of India, Cyber Law and Professional Ethics", list(MARKING.keys()), index=0)
    with col4:
        if cycle == "Physics":
            mech_subject = st.selectbox("Mechanical Engineering Sciences", list(MARKING.keys()), index=0)
        else:
            mech_subject = st.selectbox("Engineering Mechanics – Statics", list(MARKING.keys()), index=0)

    if st.button("🚀 Calculate GPA", type="primary"):
        grades = [maths, cse, ele_subject, eng_subject, evs_constitution, mech_subject]
        failed = any(grade in ['F', 'AF'] for grade in grades)

        if failed:
            st.error("❌ You have failed in one or more subjects.")
        else:
            weighted_sum = 0
            credits = CREDITS["physics"] if cycle == "Physics" else CREDITS["chemistry"]

            for i in range(len(grades)):
                weighted_sum += credits[i] * MARKING[grades[i]]

            total_credits = sum(credits)
            gpa = weighted_sum / total_credits

            st.success(f"✅ Your GPA is: **{gpa:.2f}**")

            st.subheader("📊 Your Grades:")
            st.markdown(
                f"""
                <div class="card">
                    <p>Maths: <strong>{maths}</strong></p>
                    <p>CSE: <strong>{cse}</strong></p>
                    <p>{'Elements of Electrical Engineering' if cycle == 'Physics' else 'Electronic Principles and Devices'}: <strong>{ele_subject}</strong></p>
                    <p>{'Engineering Physics and Physics Laboratory' if cycle == 'Physics' else 'Engineering Chemistry and Chemistry Laboratory'}: <strong>{eng_subject}</strong></p>
                    <p>{'Environmental Studies and Life Sciences' if cycle == 'Physics' else 'Constitution of India, Cyber Law and Professional Ethics'}: <strong>{evs_constitution}</strong></p>
                    <p>{'Mechanical Engineering Sciences' if cycle == 'Physics' else 'Engineering Mechanics – Statics'}: <strong>{mech_subject}</strong></p>
                </div>
                """,
                unsafe_allow_html=True,
            )

if __name__ == "__main__":
    main()
