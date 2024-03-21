from selenium.webdriver import Firefox, Chrome, Edge
from ipdb import post_mortem

def before_all(context):
    browser =  context.config.userdata.get('browser')

    browsers = {
        'chrome': Chrome,
        'firefox': Firefox,
        'edge': Edge
    }
    context.browser = browsers[browser]()

def after_all(context):
    context.browser.quit()

def after_step(context, step):
    if step.status == 'failed':
       post_mortem(step.exc_traceback)