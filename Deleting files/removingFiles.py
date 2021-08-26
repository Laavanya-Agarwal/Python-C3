import os
import shutil
import time

def main():
	path = "/deleting_path"
	days = 30
	seconds = time.time() - (days * 24 * 60 * 60)

	if os.path.exists(path):
		for main_folder, folders, files in os.walk(path):
			if seconds >= get_age(main_folder):
				remove_folder(main_folder)
			else:
				for folder in folders:
					folder_path = os.path.join(main_folder, folder)
					if seconds >= get_age(folder_path):
						remove_folder(folder_path)

				for file in files:
					file_path = os.path.join(main_folder, file)
					if seconds >= get_age(file_path):
						remove_file(file_path)
		else:
			if seconds >= get_file_or_folder_age(path):
				remove_file(path)

	else:
        print('The path is not found')

def remove_folder(path):
	if not shutil.rmtree(path):
		print('Path is removed successfully')
	else:
		print('Unable to delete the path')

def remove_file(path):
	if not os.remove(path):
		print('Path is removed successfully')
	else:
		print('Unable to delete the path')

def get_age(path):
	ctime = os.stat(path).st_ctime
	return ctime

main()