import json
import os
import yaml
import pandas as pd
import xml.etree.ElementTree as ET

def jsontocsv(jsonfile):
    # Read JSON file
    data = pd.read_json(jsonfile)
    # Convert JSON to CSV
    data.to_csv("./outputs/outputfromjson.csv", index=False)
    print("jsontocsv")
    return data
    
def csvtojson(csvfile):
    data = pd.read_csv(csvfile)
    records = json.loads(data.to_json(orient="records"))
    with open("./outputs/outputfromcsv.json","w") as f:
        data = json.dump(records,f)
    return data
        
def csvtoxml(csvfile):
    data = pd.read_csv(csvfile)
    return data

def csvtoyaml(csvfile):
    data = pd.read_csv(csvfile)
    return data

def jsontoxml(jsonfile):
    data = pd.read_json(jsonfile)
    return data

def xmltojson(xmlfile):
    data = []
    return data

def jsontoyaml(jsonfile):
    data = pd.read_json(jsonfile)
    return data

def xmltoyaml(xmlfile):
    data = []
    return data

def xmltocsv(xmlfile):
    data = []
    return data
        
def read(filename):
    ext = getFormat(filename)
    match(ext):
        case "json":
            data = pd.read_json(filename)
            
        case "csv":
            data = pd.read_csv(filename)
            
        case "yaml":
            with open(filename) as stream:
                try:
                    data = yaml.safe_load(stream)
                except yaml.YAMLError as exc:
                    print(exc)
                    
        case "xml":
            tree = ET.parse(filename)
            racine = tree.getroot()
            
            data = []
            for child in racine.findall('book'):
                title = child.find('title').text
                author = child.find('author').text
                year = child.find('year').text
                data.append([title,author,year])
                
        case _:
            print("Invalid file format")
            
        
    return data

def getFormat(filename):
    """
    Returns the format of a file.
    """
    return os.path.splitext(filename)[1][1:]

