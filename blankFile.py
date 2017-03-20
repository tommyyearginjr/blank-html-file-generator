from pathlib import Path
fileName = raw_input('Name the file. Don\'t forget to add suffix! : ')
Path(fileName).touch()
