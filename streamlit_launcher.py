import streamlit as st

from job_description_analyzer import analyze_desired_candidate_profile, refine_resume

st.set_page_config(layout="wide")
st.title('Resume Optimizer')

# User's resume input
resume_input = st.text_area("Enter your detailed resume and self-introduction:")

# Job description input
job_description = st.text_area("Paste the job description or requirements here:")

# Temporary function to generate optimized resume
def generate_optimized_resume(resume_input, job_description):
    desired_candidate_profile = analyze_desired_candidate_profile(job_description)
    resume = refine_resume(desired_candidate_profile, resume_input)
    return resume

# Generate button
if st.button("Generate Optimized Resume"):
    optimized_resume = generate_optimized_resume(resume_input, job_description)
    st.text_area("Generated Optimized Resume:", value=optimized_resume, height=300)
    st.download_button("Download Optimized Resume", data=optimized_resume, file_name="optimized_resume.txt", mime="text/plain")
