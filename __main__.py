import sys, getopt
import json
from jinja2 import Environment, BaseLoader

def main(argv):
  helpstr = 'jinja.py -hdt'
  template = ''
  for line in sys.stdin:
    template += line
  
  try:
    opts, args = getopt.getopt(argv, 'd:h', ["help", "data", "template"])
  except getopt.GetoptError:
    print(helpstr)
    sys.exit(2)
  
  data = None
  for opt, arg in opts:
    if opt in ('-h', '--help'):
      print(helpstr)
      sys.exit()
    elif opt in ('-d', '--data'):
      data = json.loads(arg)
      
  jinja(template, data)

def jinja(template, data):
  env = Environment(
    loader=BaseLoader()
  )
  rtemplate = env.from_string(template)
  output = rtemplate.render(**data)
  sys.stdout.write(output)

if __name__ == "__main__":
  main(sys.argv[1:])
else:
  sys.exit(1)