from selenium.webdriver import Firefox, Chrome, Edge
from ipdb import post_mortem
from selenium.webdriver.support.ui import WebDriverWait


def before_scenario(context, scenario):
    browser =  context.config.userdata.get('browser')

    browsers = {
        'chrome': Chrome,
        'firefox': Firefox,
        'edge': Edge
    }
    context.browser = browsers[browser]()
    context.browser.implicitly_wait(10)
    

def after_step(context, step):
    context.browser.implicitly_wait(10)
    if context.config.userdata.getbool("debug") and step.status == 'failed':
       post_mortem(step.exc_traceback)
    
    print()

#def after_scenario(context, scenario):
    #context.browser.quit()