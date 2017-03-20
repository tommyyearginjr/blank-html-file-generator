from pathlib import Path
fileName = raw_input('Name the webpage you want to create. Don\'t forget to add suffix! : ')
Path(fileName).touch()
print("The webpage " + fileName + " was created. Live long and prosper.")
