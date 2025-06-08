"""
import streamlit as st
import pandas as pd
import joblib

try:
    model = joblib.load('best_movie_model.pkl')
except Exception as e:
    st.error(f"Failed to load model: {e}")
    st.stop()

st.title("Movie Box Office Success Prediction")

budget = st.number_input("Budget ($)", min_value=0, step=1000000, value=50000000)
runtime = st.number_input("Runtime (minutes)", min_value=30, max_value=300, value=120)
release_month = st.slider("Release Month", 1, 12, 6)
genre_count = st.number_input("Number of Genres", min_value=0, max_value=10, value=2)
original_language = st.selectbox("Original Language", options=['en', 'fr', 'es', 'de', 'unknown', 'it', 'ja', 'zh', 'ko', 'ru'])

if st.button("Predict Success"):
    input_df = pd.DataFrame({
        'budget': [budget],
        'runtime': [runtime],
        'release_month': [release_month],
        'genre_count': [genre_count],
        'original_language': [original_language]
    })
    try:
        prediction = model.predict(input_df)[0]
        prediction_proba = model.predict_proba(input_df)[0][1]
    except Exception as e:
        st.error(f"Prediction error: {e}")
    else:
        if prediction == 1:
            st.success(f"This movie is predicted to be a BOX OFFICE SUCCESS with probability {prediction_proba:.2f}")
        else:
            st.warning(f"This movie is predicted to NOT be a box office success with probability {1 - prediction_proba:.2f}")

"""
import streamlit as st
import pandas as pd
import joblib

# ✅ Load model once using caching
@st.cache_resource
def load_model():
    return joblib.load('best_movie_model.pkl')

# ✅ Load the model safely
try:
    model = load_model()
except Exception as e:
    st.error(f"❌ Failed to load model: {e}")
    st.stop()

# ✅ App title
st.title("🎬 Movie Box Office Success Prediction")

# ✅ Input fields
budget = st.number_input("Budget ($)", min_value=0, step=1000000, value=50000000)
runtime = st.number_input("Runtime (minutes)", min_value=30, max_value=300, value=120)
release_month = st.slider("Release Month", 1, 12, 6)
genre_count = st.number_input("Number of Genres", min_value=0, max_value=10, value=2)
original_language = st.selectbox(
    "Original Language", 
    options=['en', 'fr', 'es', 'de', 'unknown', 'it', 'ja', 'zh', 'ko', 'ru']
)

# ✅ Prediction
if st.button("Predict Success"):
    input_df = pd.DataFrame({
        'budget': [budget],
        'runtime': [runtime],
        'release_month': [release_month],
        'genre_count': [genre_count],
        'original_language': [original_language]
    })

    try:
        prediction = model.predict(input_df)[0]
        prediction_proba = model.predict_proba(input_df)[0][1]
    except Exception as e:
        st.error(f"❌ Prediction error: {e}")
    else:
        if prediction == 1:
            st.success(f"✅ This movie is predicted to be a BOX OFFICE SUCCESS with probability {prediction_proba:.2f}")
        else:
            st.warning(f"⚠️ This movie is predicted to NOT be a box office success with probability {1 - prediction_proba:.2f}")

