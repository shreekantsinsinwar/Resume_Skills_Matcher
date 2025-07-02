# Resume Keyword Matcher (CLI Tool)

A command-line Python tool that compares your resume with a job description and shows:
- Match Score (based on TF-IDF cosine similarity)
- Matched and missing keywords
- The importance of a skill is based on two factors that are TF and IDF and their intersected cost.
- TF == Term Frequency (re-occuring of any term); IDF == Inverse Doc Frequency. 
- The exact formula used is TF * IDF -> Total wieght of that skill.

## 🔧 Requirements

```bash
pip install -r requirements.txt



<p align="center">
  <img src="/home/neo/Pictures/Screenshots/Screenshot_Resume_Matcher.png" alt="Tool Banner" width="80%">
</p>
