import jinja2
import sys

templateLoader = jinja2.FileSystemLoader( searchpath="./" )
templateEnv = jinja2.Environment( loader=templateLoader )
TEMPLATE_FILE = "template.tmp"
RENDER_FILE = "template_rendered.txt"
template = templateEnv.get_template( TEMPLATE_FILE )

py3 = sys.version_info[0] > 2

if py3:
  response = input("Please enter your name: ")
else:
  response = raw_input("Please enter your name: ")

templateVars = { "something" : response }

outputText = template.render( templateVars )

f = open(RENDER_FILE, 'w')
f.write(outputText)
f.close()
