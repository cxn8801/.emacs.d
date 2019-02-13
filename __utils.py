#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import json
import time
import os
from inspect import isfunction

#driver = None
#execute_result = {}

def get_working_dir():
    dirname = os.path.dirname(__file__)
    return dirname

'''
Browser activities
'''
def ChromeBrowser():
    '''
    Opens the Chrome/IE Browser in a Selenium instance.

    Returns:
        webdriver: Selenium Webdriver

    '''
    dirname = os.path.dirname(__file__)
    chrome_path = 'src/drivers/chromedriver.exe'
    filename = os.path.join(dirname, chrome_path)

    directory = get_working_dir() + "/tax_report/"
    options = webdriver.ChromeOptions() 
    prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': directory}
    options.add_experimental_option('prefs', prefs) 
    
    return webdriver.Chrome(executable_path=filename, chrome_options=options)

def IeBrowser():
    
    dirname = os.path.dirname(__file__)
    ie_path = 'src/drivers/IEDriverServer_32.exe'
    filename = os.path.join(dirname, ie_path)
    
    return webdriver.Ie(filename)


# def action_perform(action, driver):
#     global temp_data
#     global execute_result
#     #global driver
#     func_dict = {"find_element_by_id": driver.find_element_by_id,
#                  "find_element_by_name": driver.find_element_by_name,
#                  "find_element_by_xpath": driver.find_element_by_xpath,
#                  "find_element_by_link_text": driver.find_element_by_link_text,
#                  "find_element_by_partial_link_text": driver.find_element_by_partial_link_text,
#                  "find_element_by_tag_name": driver.find_element_by_tag_name,
#                  "find_element_by_class_name": driver.find_element_by_class_name,
#                  "find_element_by_css_selector": driver.find_element_by_css_selector,
#                  "return_elem": None,
#                  "change_url": driver.get
#     }

#     elem = None
#     if action["elem"] != None:
#         #print(action["elem"]["function"])
#         #driver.implicitly_wait(0)
#         #print("start: ", time.time())
#         find_elem_by_func = func_dict[ action["elem"]["function"] ]

#         param = None
#         if isfunction(action["elem"]["param"]):
#             param = action["elem"]["param"]()
#             if param == "out of range":
#                 return
#         else:
#             param = action["elem"]["param"]

#         try:
#             #print(param)
#             if find_elem_by_func is None:
#                 elem = param
#             else:
#                 elem = find_elem_by_func(param)
#            # print("end: ", time.time())
#         except Exception as e:
#             print(e)
#             #print("end: ", time.time())
#             if action["action"] == "print":
#                 return
#             raise
#         #finally:
#             #driver.implicitly_wait(1)

#     data = None
#     if isfunction(action["data"]):
#         data = action["data"]()
#     else:
#         data = action["data"]

#     #print(action["action"])
        
#     if action["action"] == "send_keys":
#         #print(action["elem"])
#         #print(type(elem))
#         elem.send_keys(data)
#     elif action["action"] == "change_url":
#         #print("url................")
#         #print(data)
#         driver.get(data)
#         #print("adfwefaga................")
#     elif action["action"] == "switch_window":
#         driver.switch_to_window(driver.window_handles[data])
#     elif action["action"] == "wait":
#         driver.implicitly_wait(data)
#     elif action["action"] == "clear":
#         elem.clear()
#     elif action["action"] == "sleep":
#         time.sleep(data)
#     elif action["action"] == "click":
#         #action_chains = ActionChains(driver)
#         #action.click(elem).perform()
#         webdriver.ActionChains(driver).move_to_element(elem).click(elem).perform()
#     elif action["action"] == "drag":
#         action_chains = ActionChains(driver)
#         action_chains.drag_and_drop_by_offset(elem, data, 0).perform()        
#     elif action["action"] == "print":
#          if data in executet_result:
#              #print(elem.get_attribute("innerText"))
#              execute_result[data] = execute_result[data] + elem.get_attribute("innerText")
#              #print(execute_result)
#          else:
#              #print(elem.get_attribute("innerText"))
#              execute_result[data] = elem.get_attribute("innerText")

#          # if data == "公司名称":
#          #     print(elem.get_attribute("innerText"), elem.text, elem.get_attribute("value"), elem.get_attribute("outerHtml"))
#          #     print(action["elem"]["function"], param)
#          # if data == "公司名称" and execute_result["公司名称"] == "":
#          #    print("asdfg")
#         #print(execute_result)
#     elif action['action'] == 'print_content':
#         content = action["content"]()
#         if content is None:
#             return
        
#         if data in execute_result:
#             execute_result[data].append(content)
#         else:
#             execute_result[data] = []
#             execute_result[data].append(content)

#     elif action["action"] == "set_data":
#         #print(data)
#         elem.send_keys(data)
#         #elem.send_keys("hello")
#     elif action["action"] == "save_as_json":
#         if execute_result["公司名称"] == "":
#             execute_result = {}
#             return
        
#         directory = get_working_dir() + data
#         #print(directory)
#         if os.path.isdir(directory):
#             pass
#         else:
#             os.mkdir(directory) 
            
#         file_name = directory + execute_result["公司名称"] + ".json"
#         #print(file_name)
#         fo = open(file_name, "w", encoding="utf-8")
#         json_result2 = json.dumps(execute_result, indent=2, ensure_ascii=False)
#         fo.write(json_result2)
#         fo.close()
#         execute_result = {}
#     elif action["action"] == "close_window":
#         driver.switch_to_window(driver.window_handles[data])
#         driver.close()
#     elif action["action"] == "switch_frame":
#         driver.switch_to.frame(elem)
#     elif action["action"] == "close":
#         driver.quit()
#         execute_result = {}
        
# def action_group_perform(action_group, driver):
#     #print(action_group["execute_times"])
#     if action_group["execute_times"] != -1:
#         for i in range(action_group["execute_times"]):
#             for action in action_group["actions"]:
#                 #print(action)
#                 if action["is_action_group"]:
#                     action_group_perform(action, driver)
#                 else:
#                     action_perform(action, driver)
#     else:
#         while action_group["execute_condition"]():
#             for action in action_group["actions"]:
#                 #print(action)
#                 if action["is_action_group"]:
#                     action_group_perform(action, driver)
#                 else:
#                     action_perform(action, driver)
    
    
# def selenium_executor(task):
#     global driver

#     directory = get_working_dir() + "/tax_report/"
#     #print(directory)
#     if os.path.isdir(directory):
#         pass
#     else:
#         os.mkdir(directory) 

    
#     options = webdriver.ChromeOptions() 
#     prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': directory}
#     options.add_experimental_option('prefs', prefs) 

#     if task["browser"] == "chrome":
#         driver = webdriver.Chrome(chrome_options=options)
#     elif task["browser"] == "ie":
#         driver = webdriver.Ie()

#     webpage = task["webpage"]

#     driver.get(webpage)
#     driver.maximize_window()
#     driver.implicitly_wait(10)

#     for action_group in task["action_groups"]:
#         action_group_perform(action_group, driver)
