import os
from dotenv import load_dotenv
load_dotenv()
import google.generativeai as genai
from PIL import Image
import streamlit as st

genai.configure(api_key=os.getenv("GOOGLE-API-KEY"))
model = genai.GenerativeModel(model_name="gemini-2.0-flash")

st.header(":blue[M.O.M] Generator",divider=True)
st.markdown("Minutes of meeting :Uploadyour handwritten MOMs ")
uploaded_file = st.file_uploader("upload your image ",type=['jpg','jpeg','png'])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img,use_container_width=True)

    prompt = f"""You are an intelligent assistant tasked with generating structured Minutes of Meeting (MoM) based on handwritten notes and to-dos provided as images. Your job is to extract text from the images and organize the information into a clean, professional table with the following columns:

    | Particulars (To-Dos) | Deadline | Status (Completed / Pending / Not Started) | % Completion |

    Requirements:
    OCR: Accurately read and transcribe handwritten text from the uploaded images.

    Task Identification: Identify individual to-do items, action points, or tasks from the transcribed text.

    Deadline Detection: Detect any mentioned dates or inferred deadlines related to each task. If no deadline is present, leave the field blank or mark as “TBD.”

    Status Assignment: Based on context (e.g., checkmarks, strikethroughs, annotations like "done", "in progress", "to-do", etc.), assign a task status:

    ✅ Completed

    🕒 Pending

    ⏳ Not Started

    Completion %: Estimate a percentage completion (e.g., 0%, 50%, 100%) based on the language or markings (e.g., “half done”, “in progress”, “✓✓✓”, etc.)."""

    with st.spinner("Extracting and Analysing the image"):
        response = model.generate_content([img,prompt])
        st.success("Extraction completed")
        st.markdown(response.text)




