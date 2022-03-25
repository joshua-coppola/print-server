import streamlit as st
import os

from config import color_printer
from config import black_white_printer

def app():
    st.image("cif_logo.jpg", width=100)
    st.markdown("## CIF Print Server")
    st.write("\n")

    # Code to read a single file 
    uploaded_file = st.file_uploader("Choose a file")
    file_name = None
    if uploaded_file is not None:
        try:
            with open(os.path.join("temp", uploaded_file.name),"wb") as f:
                f.write(uploaded_file.getbuffer())
            file_name = uploaded_file.name
        except Exception as e:
            print(e)

    copy_count = st.slider("Number of Copies", 1, 5, 1)
    st.markdown("If more than 5 copies are needed, please print in person.")

    double_sided = "one-sided"

    if st.checkbox("Color"):
        printer_name = color_printer
    else:
        printer_name = black_white_printer
        if st.checkbox("Double Sided", value=True):
            double_sided = "two-sided-long-edge"
        else:
            double_sided = "one-sided"

    if st.button("Print"):

        if file_name is not None:
            #st.markdown(f"Printing {file_name}")
            #st.markdown(f"temp/{file_name}")
            command = f'lpr -P {printer_name} temp/"{file_name}" -# {copy_count} -o sides={double_sided}'
            st.write(os.system(f'lpr -P {printer_name} temp/"{file_name}" -# {copy_count} -o sides={double_sided}'))
            os.system(f'rm temp/"{file_name}"')
            st.markdown("Printing...")



app()