# Student Performance Analyzer

Bu loyiha — **Talabalar baholarini analiz qiluvchi Streamlit web ilova**.  
U foydalanuvchiga CSV fayl yuklash, talabalarning ballarini ko‘rsatish va natijalarni grafik tarzida vizualizatsiya qilish imkonini beradi.

## 🔹 Loyiha maqsadi
- Talabalarning ballarini tez va qulay ko‘rish
- Har bir talabani baholash tizimiga qarab avtomatik baholash
- Natijalarni chiroyli jadval va grafikda chiqarish
- Streamlit asoslarini amalda o‘rganish

## 🔹 Asosiy funksiyalar
- CSV fayl yuklash
- Talabalar ma’lumotlarini jadval ko‘rinishida ko‘rsatish
- Talabalar ballari bo‘yicha grafik chizish (x=o‘qda ism, y=o‘qda ball)
- Baholash tizimini tanlash (100 ballik yoki 5 ballik)
- Talabalarni avtomatik baholash (`A'lo`, `Yaxshi`, `Qoniqarli`, `Yomon`)

## 🔹 Loyihada ishlatilgan texnologiyalar
- Python
- Streamlit
- Pandas

## 🔹 Qanday ishlatish
1. Repository-ni klonlash:
```bash
git clone https://github.com/Panjiyevsuhrob84parol/student-performance-analyzer.git
Kerakli kutibxonalar
pip install -r requirements.txt
streamlit run app.py
```
🔹 CSV fayl formati

Fayl quyidagi ustunlardan iborat bo‘lishi kerak:

name,score


Masalan:

Ali,95
Vali,67
Hasan,40




