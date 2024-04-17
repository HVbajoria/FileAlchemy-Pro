import os
import zipfile
import streamlit as st
import shutil
import textract

name_count = [1,1,1,1,1,1,1,1]
# Function that removes extra newlines and spaces from the extracted text and trim each line
def remover(text):
    # remove the extra newlines
    text = text.replace(b'\n\n', b'\n')
    # remove extra spaces
    text = text.replace(b'  ', b' ')
    # trim each line
    text = b'\n'.join([line.strip() for line in text.split(b'\n') if line.strip()])
    return text

def convert_doc_to_txt(input_dir, output_dir):
    # Check if the output directory exists, create it if not
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Get a list of all files in the input directory
    files = os.listdir(input_dir)
    # Sort the files list
    files.sort()
    # Iterate over the files and convert .doc and .docx files to .txt
    for file in files:
        text=""
        if file.endswith('.txt'):
            # For .txt files, read the content and remove extra newlines and spaces
            txt_path = os.path.join(input_dir, file)
            with open(txt_path, 'rb') as txt_file:
                text = txt_file.read()
            text = remover(text)
            # remove this file
            os.remove(txt_path)
        if file.endswith(('.doc', '.docx')):
            # For .doc and .docx files, use textract library to extract text
            doc_path = os.path.join(input_dir, file)
            text = textract.process(doc_path, encoding='utf-8')
            text = remover(text)
        # Create the output .txt file path
        txt_filename = os.path.splitext(file)[0].lower()
        txt_filename = txt_filename.replace(" ", "")
        
        print(txt_filename)
        ## if file name contains level and input or output
            
        if txt_filename.find('basic') != -1 and txt_filename.find('input') != -1:
            txt_filename = 'Basic_input_'+str(name_count[0])
            name_count[0]+=1
        if txt_filename.find('basic') != -1 and txt_filename.find('output') != -1:
            txt_filename = 'Basic_output_'+str(name_count[1])
            name_count[1]+=1
        if txt_filename.find('boundary') != -1 and txt_filename.find('input') != -1:
            txt_filename = 'Boundary_input_'+str(name_count[2])
            name_count[2]+=1
        if txt_filename.find('boundary') != -1 and txt_filename.find('output') != -1:
            txt_filename = 'Boundary_output_'+str(name_count[3])
            name_count[3]+=1
        if txt_filename.find('corner') != -1 and txt_filename.find('input') != -1:
            txt_filename = 'Corner_input_'+str(name_count[4])
            name_count[4]+=1
        if txt_filename.find('corner') != -1 and txt_filename.find('output') != -1:
            txt_filename = 'Corner_output_'+str(name_count[5])
            name_count[5]+=1
        if txt_filename.find('edge') != -1 and txt_filename.find('input') != -1:
            txt_filename = 'Edge_input_'+str(name_count[6])
            name_count[6]+=1
        if txt_filename.find('edge') != -1 and txt_filename.find('output') != -1:
            txt_filename = 'Edge_output_'+str(name_count[7])
            name_count[7]+=1

        # if file name contains level and solution
        if txt_filename.find('basic') != -1 and txt_filename.find('solution') != -1:
            txt_filename = 'Basic_output_'+str(name_count[1])
            name_count[1]+=1
        if txt_filename.find('boundary') != -1 and txt_filename.find('solution') != -1:
            txt_filename = 'Boundary_output_'+str(name_count[3])
            name_count[3]+=1
        if txt_filename.find('corner') != -1 and txt_filename.find('solution') != -1:
            txt_filename = 'Corner_output_'+str(name_count[5])
            name_count[5]+=1
        if txt_filename.find('edge') != -1 and txt_filename.find('solution') != -1:
            txt_filename = 'Edge_output_'+str(name_count[7])
            name_count[7]+=1

        # if file name only contains level but has its corresponding output ready
        if txt_filename.find('basic') != -1 and name_count[1]==4:
            txt_filename = 'Basic_input_'+str(name_count[0])
            name_count[0]+=1
        if 'boundary' in txt_filename and name_count[3]==2:
            txt_filename = 'Boundary_input_'+str(name_count[2])
            name_count[2]+=1
        if 'corner' in txt_filename and name_count[5]==2:
            txt_filename = 'Corner_input_'+str(name_count[4])
            name_count[4]+=1
        if 'edge' in txt_filename and name_count[7]==2:
            txt_filename = 'Edge_input_'+str(name_count[6])
            name_count[6]+=1
        
        if txt_filename == 'basic1':
            txt_filename = 'Basic_input_1'
            name_count[0]+=1
        if txt_filename == 'basic2':
            txt_filename = 'Basic_input_2'
            name_count[0]+=1
        if txt_filename == 'basic3':
            txt_filename = 'Basic_input_3'
            name_count[0]+=1
        if txt_filename == 'basic4':
            txt_filename = 'Basic_input_4'
            name_count[0]+=1
        if txt_filename == 'basic1_output':
            txt_filename = 'Basic_output_1'
            name_count[1]+=1
        if txt_filename == 'basic2_output':
            txt_filename = 'Basic_output_2'
            name_count[1]+=1
        if txt_filename == 'basic3_output':
            txt_filename = 'Basic_output_3'
            name_count[1]+=1
        if txt_filename == 'basic4_output':
            txt_filename = 'Basic_output_4'
            name_count[1]+=1
        if txt_filename == 'boundary1':
            txt_filename = 'Boundary_input_1'
            name_count[2]+=1
        if txt_filename == 'boundary2':
            txt_filename = 'Boundary_input_2'
            name_count[2]+=1
        if txt_filename == 'boundary1_output':
            txt_filename = 'Boundary_output_1'
            name_count[3]+=1
        if txt_filename == 'boundary2_output':
            txt_filename = 'Boundary_output_2'
            name_count[3]+=1
        if txt_filename == 'corner1':
            txt_filename = 'Corner_input_1'
            name_count[4]+=1
        if txt_filename == 'corner2':
            txt_filename = 'Corner_input_2'
            name_count[4]+=1
        if txt_filename == 'corner1_output':
            txt_filename = 'Corner_output_1'
            name_count[5]+=1
        if txt_filename == 'corner2_output':
            txt_filename = 'Corner_output_2'
            name_count[5]+=1
        if txt_filename == 'edge1':
            txt_filename = 'Edge_input_1'
            name_count[6]+=1
        if txt_filename == 'edge2':
            txt_filename = 'Edge_input_2'
            name_count[6]+=1
        if txt_filename == 'edge1_output':
            txt_filename = 'Edge_output_1'
            name_count[7]+=1
        if txt_filename == 'edge2_output':
            txt_filename = 'Edge_output_2'
            name_count[7]+=1
        if txt_filename == 'sample1':
            txt_filename = 'Sample_input_1'
        if txt_filename == 'sample2':
            txt_filename = 'Sample_input_2'
        if txt_filename == 'sample1_output':
            txt_filename = 'Sample_output_1'
        if txt_filename == 'sample2_output':
            txt_filename = 'Sample_output_2'
        if txt_filename == 'boundary1_solution':
            txt_filename = 'Boundary_output_1'
        if txt_filename == 'boundary2_solution':
            txt_filename = 'Boundary_output_2'
        if txt_filename == 'corner1_solution':
            txt_filename = 'Corner_output_1'
        if txt_filename == 'corner2_solution':
            txt_filename = 'Corner_output_2'
        if txt_filename == 'edge1_solution':
            txt_filename = 'Edge_output_1'
        if txt_filename == 'edge2_solution':
            txt_filename = 'Edge_output_2'
        if txt_filename == 'sample1_solution':
            txt_filename = 'Sample_output_1'
        if txt_filename == 'sample2_solution':
            txt_filename = 'Sample_output_2'
        if txt_filename == 'basic1_solution':
            txt_filename = 'Basic_output_1'
        if txt_filename == 'basic2_solution':
            txt_filename = 'Basic_output_2'
        if txt_filename == 'basic3_solution':
            txt_filename = 'Basic_output_3'
        if txt_filename == 'basic4_solution':
            txt_filename = 'Basic_output_4'
        txt_filename = txt_filename + ".txt"
        txt_path = os.path.join(output_dir, txt_filename)

            # Save the extracted text as .txt
        with open(txt_path, 'wb') as txt_file:
            txt_file.write(text)

        print(f"Converted {file} to {txt_filename}")

def process_zip_files(zip_file):
    # Create a directory to extract the zip contents
    output_dir = "extracted_files"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Extract the contents of the zip file
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(output_dir)

    # Process the extracted files and convert .doc and .docx to .txt
    convert_doc_to_txt(output_dir, output_dir)

    # Create a new zip file containing the processed .txt files
    processed_zip_file = "processed_files.zip"
    with zipfile.ZipFile(processed_zip_file, 'w', zipfile.ZIP_DEFLATED) as zip_out:
        for root, _, files in os.walk(output_dir):
            for file in files:
                if file.endswith('.txt'):
                    txt_path = os.path.join(root, file)
                    zip_out.write(txt_path, os.path.relpath(txt_path, output_dir))

    # Remove the temporary extracted directory
    shutil.rmtree(output_dir)

    return processed_zip_file

def main():
    st.set_page_config(
        page_title="FileAlchemy Pro",
        page_icon="📑",
    )
    

    def gradient_text(text, color1, color2):
        gradient_css = f"""
        background: -webkit-linear-gradient(left, {color1}, {color2});
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
        font-size: 36px;
        """
        return f'<span style="{gradient_css}">{text}</span>'

    def gradient(text, color1, color2):
        gradient_css = f"""
        background: -webkit-linear-gradient(left, {color2}, {color1});
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
        font-size: 18px;
        """
        return f'<span style="{gradient_css}">{text}</span>'

    color1 = "#FA5C3B"
    color2 = "#2B45D5"
    text = "FileAlchemy Pro"
  
    left_co, cent_co,last_co = st.columns(3)
    with cent_co:
        st.image("logo.png", width=140)

    styled_text = gradient_text(text, color1, color2)
    st.write(f"<div style='text-align: center;'>{styled_text}</div>", unsafe_allow_html=True)

    text="Unleashing Intelligent Solutions for a Smarter Tomorrow."
    styled_text = gradient(text, color1, color2)
    st.write(f"<div style='text-align:center;'>{styled_text}</div>",unsafe_allow_html=True)

    uploaded_file = st.file_uploader("Choose a zip file", type="zip")
    st.write("Note: Upload a zip file containing .doc and .docx files")
    name_count =[1,1,1,1,1,1,1,1]
    if uploaded_file is not None:
        # Create a temporary directory to process the zip file
        temp_dir = "temp_zip"
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)

        # Save the uploaded zip file to the temporary directory
        zip_path = os.path.join(temp_dir, "uploaded.zip")
        with open(zip_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.snow()
        print("Processing the uploaded zip file...")
        # Process the zip file and get the processed zip file path
        processed_zip_file = process_zip_files(zip_path)
        st.success('Processed Successfully!', icon="✅")
        # Offer the processed zip file for download
        st.download_button(
            label="Download Processed Zip File",
            data=open(processed_zip_file, "rb").read(),
            file_name="processed_files.zip",
        )

        # Clean up the temporary directory
        shutil.rmtree(temp_dir)

if __name__ == "__main__":
    main()

footer="""<style>

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤️ by <a style='display: inline; text-align: center;' href="https://www.linkedin.com/in/harshavardhan-bajoria/" target="_blank">Harshavardhan Bajoria</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)
