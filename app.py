import jinja2
import sys

templateLoader = jinja2.FileSystemLoader( searchpath="./" )
templateEnv = jinja2.Environment( loader=templateLoader )
TEMPLATE_FILE = "template.tmp"
RENDER_FILE = "template_rendered.txt"
template = templateEnv.get_template( TEMPLATE_FILE )

templateVars = { "something" : sys.argv[1] }

outputText = template.render( templateVars )

f = open(RENDER_FILE, 'w')
f.write(outputText)
f.close()
