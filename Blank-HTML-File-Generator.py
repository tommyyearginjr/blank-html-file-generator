from pathlib import Path

fileName = raw_input('Name the webpage you want to create. Don\'t forget to add suffix! : ')

Path(fileName).touch()

f = open(fileName, 'a')

blankHTML = ['<!DOCTYPE html>', '<html>', "     <head>", '          <title>', '          </title>', '          <style>', '          </style>', '          <script>', '          </script>', '     </head>', '     <body>', '          <script>', '          </script>', '     </body>', '</html>']

for item in blankHTML:
    print >>f, item

print("The webpage " + fileName + " was created. Live long and prosper.")
