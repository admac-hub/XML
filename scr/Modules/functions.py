import os
import base64
from traceback import print_tb
from unittest import result
import zlib
from base64 import encode
from multiprocessing.sharedctypes import Value
from xml.dom import minidom
import os
import pandas as pd
import xml.etree.ElementTree as ET
from lxml import etree as et
from datetime import datetime

################################################################################################################################
#------------------------------------------Specify Working Directory-----------------------------------------------------------#
################################################################################################################################

InputFile = 'C:\\Users\\ardit.cuko\\Downloads\\100-Python-Project-main\\100-Python-Project-main\\XML parser\\InputFile'
OutputFiles = "C:\\Users\\ardit.cuko\\Downloads\\100-Python-Project-main\\100-Python-Project-main\\XML parser\\OutputFiles"
WorkQueue =  "C:\\Users\\ardit.cuko\\Downloads\\100-Python-Project-main\\100-Python-Project-main\\XML parser\\WorkQueue"

#******************************************************************************************************************************#
#------------------------------------------- XML Instance ---------------------------------------------------------------------#

files = os.listdir(InputFile)
for file_name in files:
    file_path = os.path.join(InputFile, file_name)
    if os.path.isfile(file_path):
        try:
            tree = ET.parse(file_path)
            # Get the file time
            file_time = os.path.getmtime(file_path)
            # print(f"File: {file_name} | File time: {file_time}")
        except ET.ParseError:
            print(f"Skipping file: {file_name} | Not a valid XML file.")


root = tree.getroot()


#-------------------------------------------Building Functions ------------------------------------------------------------#


def translate_to_file():                                                                                                    # This Function goes though main XML page and check to see how many OrderDetail attributes are 
    order_details = root.findall('.//OrderDetail')                                                                          # Finds them , extract`s the BASE64 text from them and them , UNZIP & Decoded and creates 
    for i, order_detail in enumerate(order_details):                                                                        # two new XML with them
        order_detail_text = order_detail.text
        if order_detail_text:
            result = zlib.decompress(base64.b64decode(order_detail_text), 16 + zlib.MAX_WBITS).decode('utf-8')
            file_name = f"order_detail_{i+1}.xml"
            file_path = os.path.join(OutputFiles, file_name)
            with open(file_path, 'w') as file:
              file.write(result)         



def read_files():
    file_list = os.listdir(OutputFiles)

    # Create the destination folder if it doesn't exist
    os.makedirs(WorkQueue, exist_ok=True)

    # Process each file in the source folder
    for file_name in file_list:
        if file_name.endswith('.xml'):  # Process only XML files
            source_file_path = os.path.join(OutputFiles, file_name)  # Full path to the source file
            cleaned_content = clean_xml_file(source_file_path)

            # Write the cleaned content to the destination file
            destination_file_path = os.path.join(WorkQueue, file_name)  # Full path to the destination file
            with open(destination_file_path, 'w') as destination_file:
                destination_file.write(cleaned_content)

    print("Files cleaned and written to the destination folder.")

def clean_xml_file(file_path):
    with open(file_path) as xml_file:
        lines = xml_file.readlines()
        cleaned_lines = [line for line in lines if line.strip()]  # Remove empty lines
        cleaned_content = "".join(cleaned_lines)
        return cleaned_content





#----------------------------------- MAINFILE.XML-------------------------------------------------------------------------#

tree = ET.parse(file_path)
root = tree.getroot()

def cus_name():
    for child in root.iter('Order'):                                  # Get elemet`s from .XML that will be used to create our output.xml
        _ = child.attrib
        customer_name = (_.get('FromContactID'))
        


def shipiing_oder():
    for child in root.iter('Order'):                                  # Get elemet`s from .XML that will be used to create our output.xml
        _ = child.attrib
        ship_order = (_.get('MfgShipToAddressID'))

def main():   
    translate_to_file()
    read_files()     
if __name__ == "__main__":
    main()
