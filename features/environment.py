from selenium.webdriver import Firefox, Chrome, Edge
from ipdb import post_mortem
from selenium.webdriver.support.ui import WebDriverWait

def before_all(context):
    browser =  context.config.userdata.get('browser')

    browsers = {
        'chrome': Chrome,
        'firefox': Firefox,
        'edge': Edge
    }
    context.browser = browsers[browser]()

def before_scenario(context, scenario):
    context.browser.implicitly_wait(10)
    

def after_step(context, step):
    if context.config.userdata.getbool("debug") and step.status == 'failed':
       post_mortem(step.exc_traceback)
    

def after_scenario(context, scenario):
    context.browser.quit()