import streamlit as st
import os
import re
from main import extract_text

def match_job_description(resume_text, job_description):
    try:
        # Extract words from resume and JD
        resume_words = re.findall(r"\w+", resume_text.lower())
        jd_words = re.findall(r"\w+", job_description.lower())

        # Count matches
        matched_words = set(resume_words) & set(jd_words)
        score = (len(matched_words) / len(set(jd_words))) * 100 if jd_words else 0

        return round(score, 2), matched_words
    except Exception as e:
        st.error(f"Error comparing resume and job description: {e}")
        return 0, set()

st.title("📄 AI Resume Analyzer")
st.write("Upload your resume and paste the job description to see how well they match!")

# File uploader
uploaded_resume = st.file_uploader("Upload Resume (PDF, DOCX, TXT)", type=["pdf", "docx", "txt"])

# Job description input
job_description = st.text_area("Paste Job Description Here")

if uploaded_resume and job_description:
    # Save uploaded file temporarily
    temp_dir = "temp_uploads"
    os.makedirs(temp_dir, exist_ok=True)
    file_path = os.path.join(temp_dir, uploaded_resume.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_resume.getbuffer())

    # Extract text from resume
    resume_text = extract_text(file_path)

    if not resume_text.strip():
        st.error("❌ Could not extract text from the uploaded resume. Please check the file format.")
    else:
        score, matched_words = match_job_description(resume_text, job_description)
        st.success(f"✅ Match Score: {score}%")
        st.write("### Matched Keywords:")
        st.write(", ".join(matched_words))

else:
    st.info("Please upload a resume and paste a job description to start.")
