import pandas as pd
import xml.etree.ElementTree as ET
from config import CSV_FILE, EXCEL_FILE, XML_FILE

def convert_to_csv(df):
    df.to_csv(CSV_FILE, index=False)
    return CSV_FILE

def convert_to_excel(df):
    df.to_excel(EXCEL_FILE, index=False)
    return EXCEL_FILE

def convert_to_xml(df):
    root = ET.Element("weather_data")
    for index, row in df.iterrows():
        city_element = ET.SubElement(root, "city")
        # Ensure these keys match the names in process_data.py exactly
        ET.SubElement(city_element, "name").text = str(row['City'])
        ET.SubElement(city_element, "temperature").text = str(row['Temperature'])        
        ET.SubElement(city_element, "humidity").text = str(row['Humidity'])
        ET.SubElement(city_element, "description").text = str(row['Description'])
        ET.SubElement(city_element, "wind_speed").text = str(row['Wind Speed'])
        ET.SubElement(city_element, "pressure").text = str(row['Pressure'])
    
    tree = ET.ElementTree(root)
    tree.write(XML_FILE)
    return XML_FILE