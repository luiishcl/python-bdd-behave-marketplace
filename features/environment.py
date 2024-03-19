from selenium import webdriver
 
def before_scenario(context, scenario):
  if 'web' in context.tags:
    context.web = webdriver.Firefox()
    context.web.implicitly_wait(10)

def after_step(context, step):
  print()
 
def after_scenario(context, scenario):
  if 'web' in context.tags:
    context.web.quit()