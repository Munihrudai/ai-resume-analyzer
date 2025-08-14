import streamlit as st
import os
import re
import matplotlib.pyplot as plt
from main import extract_text
from fpdf import FPDF


# Function to match job description and resume
def match_job_description(resume_text, job_description):
    try:
        resume_words = re.findall(r"\w+", resume_text.lower())
        jd_words = re.findall(r"\w+", job_description.lower())

        matched_words = set(resume_words) & set(jd_words)
        missing_words = set(jd_words) - set(resume_words)

        score = (len(matched_words) / len(set(jd_words))) * 100 if jd_words else 0
        return round(score, 2), matched_words, missing_words
    except Exception as e:
        st.error(f"Error comparing resume and job description: {e}")
        return 0, set(), set()


# Function to clean text for PDF compatibility
def clean_text(text):
    # Keep only Latin-1 characters (avoids PDF unicode issues)
    return text.encode('latin-1', 'ignore').decode('latin-1')


# Function to generate PDF report
def generate_pdf(score, matched_words, missing_words, resume_text, job_description):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    pdf.set_font("Arial", size=12)

    pdf.multi_cell(0, 10, f"Resume Match Score: {score}%")
    pdf.multi_cell(0, 10, f"Matched Keywords: {', '.join(matched_words) if matched_words else 'None'}")
    pdf.multi_cell(0, 10, f"Missing Keywords: {', '.join(missing_words) if missing_words else 'None'}")
    pdf.multi_cell(0, 10, f"Total Keywords in Job Description: {len(matched_words) + len(missing_words)}")

    pdf.ln(5)
    pdf.multi_cell(0, 10, "=== Job Description ===")
    pdf.multi_cell(0, 10, clean_text(job_description))

    pdf.ln(5)
    pdf.multi_cell(0, 10, "=== Resume Content ===")
    pdf.multi_cell(0, 10, clean_text(resume_text))

    pdf_path = "resume_analysis_report.pdf"
    pdf.output(pdf_path)
    return pdf_path


# ================= STREAMLIT APP =================
st.title("📄 AI Resume Analyzer")
st.write("Upload your resume and paste the job description to see how well they match!")

uploaded_resume = st.file_uploader("Upload Resume (PDF, DOCX, TXT)", type=["pdf", "docx", "txt"])
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
        # Match job description
        score, matched_words, missing_words = match_job_description(resume_text, job_description)

        # ATS grading
        if score >= 80:
            grade = "🟢 Excellent"
        elif score >= 50:
            grade = "🟡 Good"
        else:
            grade = "🔴 Needs Improvement"

        st.success(f"✅ ATS Match Score: {score}% - {grade}")

        st.write("### Matched Keywords:")
        st.write(", ".join(matched_words) if matched_words else "None")

        st.write("### Missing Keywords (Add these to improve score):")
        st.write(", ".join(missing_words) if missing_words else "None")

        # Skill gap bar chart
        st.write("### Skill Gap Analysis:")
        fig, ax = plt.subplots()
        ax.bar(["Matched", "Missing"], [len(matched_words), len(missing_words)], color=["green", "red"])
        ax.set_ylabel("Number of Keywords")
        st.pyplot(fig)

        # Generate and download PDF
        pdf_path = generate_pdf(score, matched_words, missing_words, resume_text, job_description)
        with open(pdf_path, "rb") as f:
            st.download_button(
                "📥 Download PDF Report",
                f,
                file_name="resume_analysis_report.pdf",
                mime="application/pdf"
            )

else:
    st.info("Please upload a resume and paste a job description to start.")
