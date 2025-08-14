📄 AI Resume Analyzer
Project Overview

The AI Resume Analyzer is a web-based application built with Python and Streamlit that allows users to upload a resume and a job description. The tool automatically analyzes the resume, extracts relevant text, and compares it with the job description to provide:

ATS (Applicant Tracking System) Match Score

Matched Keywords

Missing Keywords

Skill Gap Analysis with a bar chart

Downloadable PDF Report summarizing the analysis

This project helps job seekers optimize their resumes to match job descriptions better and improve their chances of passing ATS screening.

Features

Upload resumes in PDF, DOCX, or TXT formats.

Paste the job description in a text area.

Extract text from the uploaded resume.

Compare the resume with the job description:

Calculate match score as a percentage.

List matched keywords.

List missing keywords.

Display a skill gap bar chart (matched vs missing keywords).

Generate a downloadable PDF report containing:

Resume match score

Matched and missing keywords

Job description and extracted resume content

User-friendly interface with Streamlit.

Project Structure
resume-analyzer/
│
├─ main.py                  # Functions to extract text from PDF, DOCX, TXT
├─ app.py                   # Streamlit app, keyword matching, PDF generation
├─ requirements.txt         # Required Python packages
├─ README.md                # Project documentation
├─ temp_uploads/            # Temporary folder for uploaded resumes
└─ resume_analysis_report.pdf  # Generated PDF report

Installation & Setup

Clone the repository or copy the project folder:

git clone <repository-url>
cd resume-analyzer


Install Python dependencies:

pip install -r requirements.txt


Required packages:

streamlit

fpdf (or fpdf2)

matplotlib

python-docx

PyPDF2

If you don’t have requirements.txt, you can install manually:

pip install streamlit fpdf matplotlib python-docx PyPDF2

Running the Application

Run Streamlit app:

streamlit run app.py


Open the URL shown in the terminal (usually http://localhost:8501) in your web browser.

Steps inside the app:

Upload your resume file.

Paste the job description text.

Wait for the analysis results:

ATS Match Score

Matched keywords

Missing keywords

Skill gap bar chart

Download the PDF report by clicking the download button.

Example Output

ATS Match Score: 75% 🟡 Good

Matched Keywords: Python, SQL, Java, Git

Missing Keywords: Django, REST API

Skill Gap Analysis Chart: Green = Matched, Red = Missing

PDF Report: Contains full summary with resume and job description.

Project Commands Summary
# Navigate to project folder
cd path/to/resume-analyzer

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py

Additional Notes

Only text-based PDFs are supported (scanned images may fail).

Large resumes or job descriptions may take a few seconds to process.

Use fpdf2 for full Unicode support if your resume contains special characters.

Temporary uploads are saved in temp_uploads/ and can be deleted after use.

Author

Muni Hrudai – Community Project: Automatic Resume Analyzer for Job Seekers