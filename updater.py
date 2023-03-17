from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re
import os as linux_command
import fileinput

##############################Settings#######################################################################################

options = webdriver.ChromeOptions()

#options for parser user, for more info visit  
options.add_argument("user-agent=Mozilla/10.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/108.0")
options.add_argument('--no-sandbox')
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("headless")#disables Chrome GUI
options.add_argument('--disable-gpu')

#Directory for backups
directory= linux_command.path.isdir("docker-backups")
if directory == False:
    print("Creating docker backups directory \n")
    linux_command.mkdir("docker-backups")
else:
    print("Directory already exists \n")
    pass


#links for scraping
links = [

    ]

driver = webdriver.Chrome(options=options)
############################################################################################################################

linux_command.system("cat docker-compose.yml>docker-compose_new.txt")

create_pull = open ("pull.txt", 'w')
create_pull.close

####################################### Full XPATH #########################################################################
# CHANGE XPATH IN CASE OF FAILURE

button_xpath = '/html/body/div[2]/div/div[1]/div/div/div/main/div/div/div/div[3]/div/div[1]/ul/li[3]/button'
image_name_xpath='/html/body/div[2]/div/div[1]/div/div/div/main/div/div/div/div[2]/div/div[2]/div/div/div[1]/div[1]/h1'
version_xpath='/html/body/div[2]/div/div[1]/div/div/div/main/div/div/div/div[3]/div/div[2]/div[3]/div/div[2]/div[1]/table/tbody/tr[{que}]/td[1]'
###########################################################################################################################

for url in links:
    driver.get(url=url)
    time.sleep(3.5)
    button = driver.find_element(by=By.XPATH, value=button_xpath)
    driver.execute_script("arguments[0].click();",button)
    image_name = driver.find_element(by=By.XPATH, value=image_name_xpath).text
    repeat = range(0,1)
    tag_number= 0

    for x in repeat:  #getting version
        tag_number +=1
        tag_version = driver.find_element(by=By.XPATH,value=version_xpath.format(que=tag_number)).text
        new_version=image_name +":"+ tag_version
        old_version=r".*"
        read_pull = open ("pull.txt", 'a')
        read_pull.writelines("sudo docker pull "+new_version +"\n")
        read_pull.close

        with open('docker-compose_new.txt', 'r') as f1 :#reading current docker-compose file 
            lines = f1.readlines()
            for line in lines:
                line = line.strip()
                find= re.findall(image_name+old_version,line)
                if find:
                    for found in find:
                        print(found,"-",new_version)
                        
                        with fileinput.FileInput("docker-compose_new.txt", inplace=True) as file:
                            for line in file:
                                print(line.replace(found, new_version), end='')#replacing old version with new one


linux_command.system("cat docker-compose.yml>docker-backups/{time}.yml".format(time=time.strftime("%d-%m-%Y-%H:%M")))
linux_command.system("cat docker-compose_new.txt>docker-compose.yml")
linux_command.system("rm -r docker-compose_new.txt")


driver.close()
driver.quit()
