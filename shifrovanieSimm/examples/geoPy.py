def geolocation():
    import requests
    from bs4 import BeautifulSoup
    from selenium import webdriver
    import time
    import os
    from urllib.parse import urljoin

    fileN = 'geo.html'
    url = urljoin('file://', os.path.abspath(fileN))

    driver = webdriver.Chrome('../chromedriver.exe')
    driver.get(url)
    time.sleep(5)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    data = str(soup.p.text).split(' ')
    geoData = []

    try:
        datao = data[1].split('.')
        do = str(datao[0]) + "." + str(datao[1][:4])
        datat = data[3].split('.')
        dt = str(datat[0]) + "." + str(datat[1][:4])
        return do+' '+dt
    except:
        return 'error'