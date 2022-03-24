import streamlit as st
import os


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

    if st.button("Print"):
        
        printer_name = "HP-LaserJet-500-color-M551"
        #printer_name = "HP-LaserJet-P4015"
        if file_name is not None:
            st.markdown(f"Printing {file_name}")
            st.markdown(f"temp/{file_name}")
            st.write(os.system(f'lpr -P {printer_name} temp/"{file_name}"'))
            os.system(f'rm temp/"{file_name}"')
app()