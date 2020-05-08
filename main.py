import PySimpleGUI as sg
import extract
from winc_cc64 import iconWindow

if __name__ == "__main__":
	# GUI initialization
	sg.theme('DarkBlue15')
	sg.SetOptions(icon=iconWindow, text_justification='center')

	layout = [
		[sg.Text('Program removes the overparametrization')],
		[sg.Text('Object configured through config.ini')],
		[sg.Text('							')],
		[sg.Text('Choose XML panel')],
		[sg.Input(background_color='black'), sg.FilesBrowse(file_types=(("WinCC OA Panel", "*.xml"),))],
		[sg.Button('Process'), sg.Cancel()],
	]

	window = sg.Window('WinCC OA Remove Parameters', layout)
	while True:
		event, values = window.read()

		if event == "Process":
			files = values['Browse'].split(';')
			for file in files:
				if extract.extract_file(file):
					sg.Popup('Success')
				else:
					sg.PopupError('Error in'.format(file))

		if event in (None, 'Cancel'):
			break

	print(values)
	window.close()