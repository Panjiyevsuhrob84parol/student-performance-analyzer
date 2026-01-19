import streamlit as st
import pandas as pd

st.title("Student Performance Analyzer")
st.write("Talabalarning baholarini analiz qiluvchi web app.")

st.sidebar.header("Baholash tizimini tanlash")

baholash = st.sidebar.selectbox(
    "Baholash tizimini tanlang:",
    ["100 ballik", "5 ballik"]
)

file = st.file_uploader("CSV fayl yuklang", type=["csv"])

if file is not None:
    df = pd.read_csv(file)

    st.subheader("Ma'lumotlar jadvali")
    st.dataframe(df)

    # Talabalar soni
    st.subheader("Talabalar soni")
    st.info(f"Umumiy talabalar soni: {len(df)} ta")

    # Grafik
    st.subheader("Grafik")
    st.bar_chart(data=df.set_index("name")["score"])

    # 🔹 Baholash funksiyasi
    def bahola(score):
        if baholash == "100 ballik":
            if score >= 90:
                return "A'lo"
            elif 70<=score<= 89:
                return "Yaxshi"
            elif 50<=score<=69:
                return "Qoniqarli"
            elif score<=50:
                return "Yomon"
        if baholash == "5 ballik": 
            if score >= 90:
                return "A'lo"
            elif 70<=score<= 89:
                return "Yaxshi"
            elif 50<=score<=69:
                return "Qoniqarli"
            elif score<=50:   
                return "Yomon"
    # Yangi ustun
    df["natija"] = df["score"].apply(bahola)

    st.subheader("Baholangan jadval")
    st.dataframe(df)
    st.success("Bajarildi ✅")
    st.info("Hammasi yaxshi bajarildi ✅")
else:
    st.info("Iltimos CSV fayl yuklang")
