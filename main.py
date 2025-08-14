import PyPDF2
import re
from docx import Document

def extract_text(file_path):
    text = ""
    try:
        if file_path.endswith(".pdf"):
            with open(file_path, "rb") as f:
                reader = PyPDF2.PdfReader(f)
                for page in reader.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"

        elif file_path.endswith(".docx"):
            doc = Document(file_path)
            for para in doc.paragraphs:
                text += para.text + "\n"

        elif file_path.endswith(".txt"):
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                text = f.read()

        else:
            print("Unsupported file format")
            return ""

    except Exception as e:
        print(f"Error reading file: {e}")

    return text.strip()


def match_job_description(resume_text, job_description):
    if not resume_text:  # Empty resume text
        return 0, []

    resume_words = re.findall(r"\w+", resume_text.lower())
    jd_words = re.findall(r"\w+", job_description.lower())

    matched_words = list(set(resume_words) & set(jd_words))
    score = int((len(matched_words) / len(set(jd_words))) * 100) if jd_words else 0

    return score, matched_words
