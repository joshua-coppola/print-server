import streamlit as st
import os
import random
import datetime

from config import color_printer
from config import black_white_printer
from config import allowed_extensions


# TODO:
#- authentication
 

def app():
    st.image("cif_logo.jpg", width=100)
    st.markdown("## CIF Print Server")
    st.write("\n")

    # Code to read a single file 

    uploaded_file = st.file_uploader("Choose a file", type=allowed_extensions)
    file_name = None
    if uploaded_file is not None:
        try:
            extension = uploaded_file.name.split(".")[1]
            salt = random.randint(0,100000)
            with open(f"temp/print_file{salt}.{extension}","wb") as f:
                f.write(uploaded_file.getbuffer())
            file_name = f"print_file{salt}.{extension}"
        except Exception as e:
            print(e)

    copy_count = st.slider("Number of Copies", 1, 5, 1)
    st.markdown("If more than 5 copies are needed, please print in person.")
    st.markdown("Color cannot be combined with double sided printing.")


    double_sided = "one-sided"

    if st.checkbox("Color"):
        printer_name = color_printer
    else:
        printer_name = black_white_printer
        if st.checkbox("Double Sided", value=True):
            double_sided = "two-sided-long-edge"
        else:
            double_sided = "one-sided"
    if st.checkbox("Landscape"):
        orientation = "-o orientation-requested=4"
        if "two-sided" in double_sided:
            double_sided = "two-sided-short-edge"
    else:
        orientation = ""
        if "two-sided" in double_sided:
            double_sided = "two-sided-long-edge"
    if not st.checkbox("Print All Pages", value = True):
        start = st.number_input("Start Page", min_value = 1, value = 1, step = 1)
        end = st.number_input("End Page", min_value = 1, value = 1, step = 1)
        page_range = f"-o page-ranges={start}-{end}"
    else:
        page_range = ""

    if st.button("Print"):

        if file_name is not None:
            #st.markdown(f"Printing {file_name}")
            #st.markdown(f"temp/{file_name}")
            status = os.system(f'lpr -P {printer_name} temp/"{file_name}" -# {copy_count} -o sides={double_sided} {orientation} {page_range}')
            os.system(f'rm temp/*')
            st.markdown("Printing...")
            with open('logs.csv', 'a') as output:
                output.write(f'{datetime.datetime.now()},{uploaded_file.name},{copy_count},{printer_name},{double_sided},{page_range},{status}\n')
        else:
            st.markdown("No file provided")



app()