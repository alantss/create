import os.path
import json
import sys

from classes.Logger import Logger
from selenium import webdriver
from time import sleep

log = Logger().log

if not os.path.exists('config/config.json'):
    log("Configuration file not found! Exiting...", 'red')
    exit()

with open('config/config.json') as config_file:
    log("Configuration file loaded.", 'green')
    config = json.load(config_file)

def create(project_name):

    log("Project Name: %s" % project_name, 'cyan')
    project_path = "{}\{}".format(config['defaults']['project_path'], project_name)
    try:
        os.mkdir(project_path)
        log("Project folder created at path: %s" % project_path, 'green')
    except Exception as e:
        log(e, 'red')
        exit()

    log("Launching browser for GitHub access...")
    browser = webdriver.Chrome()
    browser.get("https://github.com/login")
    browser.find_elements_by_xpath("//*[@id='login_field']")[0].send_keys(config['github']['username'])
    browser.find_elements_by_xpath("//*[@id='password']")[0].send_keys(config['github']['password'])
    browser.find_elements_by_xpath("//*[@id='login']/form/div[3]/input[4]")[0].click()
    
    # 2FA handling...
    if "two-factor" in browser.current_url:
        while browser.current_url != "https://github.com":
            pass

    browser.get("https://github.com/new")
    browser.find_elements_by_xpath("//*[@id='repository_name']")[0].send_keys(project_name)

    if config['defaults']['private_repo']:
        browser.find_elements_by_xpath("//*[@id='repository_visibility_private']")[0].click()

    browser.find_elements_by_class_name("first-in-line")[0].submit()
    log("Repository created: %s" % browser.current_url, 'green')
    browser.quit()

if len(sys.argv) < 2:
    log("Argument not passed! Try: 'create project_name'", 'red')
    exit()

if __name__ == "__main__":
    create(sys.argv[1])
