import xml.etree as etree
import xml.etree.ElementTree as ET
import configparser
import shutil

def extract_file(file_path):
	"""
	Extract information from the xml

	:param file_path:
	:return: extracted xml
	"""
	config = configparser.ConfigParser()
	config.read('config.ini')
	objects = config['OBJECTS']
	listobjects = []
	for object in objects:
		listobjects.append(objects[object].replace('"', ''))

	try:
		tr = ET.parse(file_path)
		root = tr.getroot()
		list = root.findall('.//*/reference')
		for element in list:
			name = element.find('.//*prop[@name="FileName"]')
			if name.text in listobjects:
				shapes = element.findall('.//shape/properties/prop[@type="TRANSFORM"]')
				if shapes:
					shapes_to_remove = element.findall('.//shape[@shapeType="RefShape"]')
					for shape in shapes_to_remove:
						element.remove(shape)
		tr.write(file_path)
		return True
	except Exception as e:
		print(e)
		return False
