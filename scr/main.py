import os
import xml.etree.ElementTree as ET
from asyncore import read
from cgitb import reset
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
from Modules import functions
date_time = datetime.now().date()

#---------------------------------- Buil Ouptut.xml---------------------------------------#

# def process_workqueue_files():
#     workqueue_folder = "C:\\Users\\ardit.cuko\\Downloads\\100-Python-Project-main\\100-Python-Project-main\\XML parser\\WorkQueue"

#     # Get a list of XML files in the WorkQueue folder
#     file_list = [file for file in os.listdir(workqueue_folder) if file.endswith(".xml")]

#     # Process each XML file
#     for file_name in file_list:
#         file_path = os.path.join(workqueue_folder, file_name)

#         # Check if the XML file contains the required data
#         if has_required_data(file_path):
#             # Extract the required data from the XML file
#             data = extract_data(file_path)

#             # Create a new XML file with the required data
#             create_new_xml_file(data, file_name)

#     print("Processing of WorkQueue files completed.")

# def has_required_data(file_path):
#     # Add your logic to check if the XML file contains the required data
#     # Return True if the file has the required data, False otherwise
#     # Example:
#     tree = ET.parse(file_path)
#     root = tree.getroot()

#     # Check if the required data is present in the XML file
#     if root.find("required_data_element") is not None:
#         return True
#     else:
#         return False

# def extract_data(file_path):
#     # Add your logic to extract the required data from the XML file
#     # Return the extracted data as a dictionary or in the desired format
#     # Example:
#     tree = ET.parse(file_path)
#     root = tree.getroot()

#     data = {}
#     data["required_data"] = root.find("required_data_element").text

#     return data

# def create_new_xml_file(data, file_name):
#     # Add your logic to create a new XML file with the required data
#     # Use the data dictionary or the extracted data to construct the XML structure
#     # Example:
#     root = ET.Element("root")
#     element = ET.SubElement(root, "element")
#     element.text = data["required_data"]

#     new_tree = ET.ElementTree(root)
#     new_file_path = f"path/to/OutputFolder/{file_name}"  # Replace with the desired output folder path
#     new_tree.write(new_file_path)

#     print(f"New XML file created: {new_file_path}")

# # Example usage
# process_workqueue_files()


print(functions.WorkQueue)



