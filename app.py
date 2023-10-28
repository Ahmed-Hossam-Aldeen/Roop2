# app.py
import streamlit as st
import os

def save_uploadedfile(uploadedfile):
     with open(os.path.join("./",uploadedfile.name),"wb") as f:
         f.write(uploadedfile.getbuffer())
     return st.success(f"{uploadedfile.name} File Uploaded Successfully!")


@st.experimental_singleton
def utils(suppress_st_warning=True):
# Clone the repository and navigate to the roop folder
     os.system("git clone https://github.com/based9based/roop")
     #os.chdir("roop")

# Install requirements
     #os.system("pip install -r requirements-headless.txt")

# Download the model file
     os.system("wget https://civitai.com/api/download/models/85159 -O inswapper_128.onnx")

# Import required modules
from PIL import Image
import io
import subprocess

# Streamlit app header
st.title("Face Swapper Streamlit App")
utils()
# Upload source and target images
source_image = st.file_uploader("Upload source image (AS.jpg)", type=["jpg", "png"])
target_video = st.file_uploader("Upload target video (NSF.mp4)", type=["mp4"])

# Run the face swapping and enhancement process
if source_image and target_video:
    st.info("Processing... This may take a while.")
    
    # Save uploaded files
    save_uploadedfile(source_image)
    save_uploadedfile(target_video)
    target_path=source_image.name
    source_path=target_video.name
    # Run face swapping and enhancement
    command = f"python run.py --target {target_path} --source {source_path} -o swapped.mp4 --execution-provider cuda --frame-processor face_swapper"
    subprocess.run(command, shell=True)
    
    # Display processed video
    processed_video = open("swapped.mp4", "rb")
    video_bytes = processed_video.read()
    st.video(video_bytes)
    st.success("Processing complete!")

# Note to the user
st.info("Note: Make sure to upload a source image and a target video to perform the face swapping and enhancement.")
