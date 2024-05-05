import streamlit as st
import numpy as np

st.title("Simple implementation of revised IWOS criteria for sarcoid uveitis classification")
st.markdown("Here is a free implementation of the sarcoid uveitis classification according to modified IWOS criteria \n*Mochizuki M, Smith JR, Takase H for the International Workshop on Ocular Sarcoidosis Study Group, et al \nRevised criteria of International Workshop on Ocular Sarcoidosis (IWOS) for the diagnosis of ocular sarcoidosis\nBritish Journal of Ophthalmology 2019;103:1418-1422.*)")

st.subheader("I. Other causes of granulomatous uveitis must be ruled out")
st.subheader("II. Intraocular signs suggestive of ocular sarcoidosis")
st.write("Please check following signs if present: ")
IO_signs_1 = st.checkbox("Mutton-fat keratic precipitates and/or iris nodules (Koeppe or Busacca)")
IO_signs_2 = st.checkbox("Trabecular meshwork nodules and/or tent-shaped peripheral anterior synechia")
IO_signs_3 = st.checkbox("Snowball/string of pearls vitreous opacities")
IO_signs_4 = st.checkbox("Multiple chorioretinal peripheral lesions (active and atrophic)")
IO_signs_5 = st.checkbox("Periphlebitis and/or macroaneurysm in an inflamed eye")
IO_signs_6 = st.checkbox("Optic disc nodules/granulomas and/or choroidal nodule")
IO_signs_7 = st.checkbox("Bilaterality (clinical or imaging)")

suggestive_signs = np.array([IO_signs_1,
                    IO_signs_2,
                    IO_signs_3,
                    IO_signs_4,
                    IO_signs_5,
                    IO_signs_6,
                    IO_signs_7], dtype = bool)
number_sugg_signs = suggestive_signs.sum()

st.subheader("III. Systemic signs suggestive of systemic sarcoidosis")
systemic_signs_1 = st.checkbox("Bilateral hilar lymphadenopathy on X-ray or CT-scan")
systemic_signs_2 = st.checkbox("Negative tuberculin test or IGRA")
systemic_signs_3 = st.checkbox("Elevated serum ACE")
systemic_signs_4 = st.checkbox(" Elevated serum lysozyme")
systemic_signs_5 = st.checkbox("Elevated serum soluble IL-2 receptor")
systemic_signs_6 = st.checkbox("Elevated serum calcium")
systemic_signs_7 = st.checkbox("Elevated serum gammaglobulin")
systemic_signs_8 = st.checkbox("Elevated serum KL-6")
systemic_signs_9 = st.checkbox("Elevated CD4/CD8 ratio (>3.5) in BAL fluid")
systemic_signs_10 = st.checkbox("Abnormal 67Ga scintigraphy or 18F-FDG PET")

suggestive_systemic_signs = np.array([systemic_signs_1,
                                      systemic_signs_2,
                                      systemic_signs_3,
                                      systemic_signs_4,
                                      systemic_signs_5,
                                      systemic_signs_6,
                                      systemic_signs_7,
                                      systemic_signs_8,
                                      systemic_signs_9,
                                      systemic_signs_10], dtype = bool)
number_syst_signs = suggestive_systemic_signs.sum()

st.subheader("Histological granuloma")
histo = st.radio("Was histology contributive?", ["Yes", "No"])

st.subheader("Compatible uveitis")
is_compatible = st.radio("Is uveitis compatible with sarcoidosis?", ["Yes", "No"])

st.subheader("Classification")
if histo == "Yes" and is_compatible =="Yes":
    st.write("Definite OS")
elif histo == "No" and systemic_signs_1 == True and number_sugg_signs>=2:
    st.write("Presumed OS")
elif histo == "No" and systemic_signs_1 == False and np.array([systemic_signs_1,
                                      systemic_signs_2,
                                      systemic_signs_3,
                                      systemic_signs_4,
                                      systemic_signs_5,
                                      systemic_signs_6,
                                      systemic_signs_7,
                                      systemic_signs_8], dtype = bool).sum() >=2 and number_sugg_signs >=3:
    st.write("Probable OS")
else: 
    st.write("Alternative diagnosis is suggested/evidence is lacking for sarcoidosis")
