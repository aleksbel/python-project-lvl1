import prompt
def run(question):
  name = prompt.string(question)
  print('Hello, {}!'.format(name))
