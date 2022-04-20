# print-server

This application provides a web page for individuals to upload files to print.

## Dependencies

- python3
- pip package: streamlit

## Configuration

Printer Names are configured in config.py.

## Running the program

`streamlit run main.py --theme.base light --server.maxUploadSize 20 --server.port X`

This will make the webpage appear on `localhost:X` and `IP:X`.
