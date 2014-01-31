import _mechanize as mechanize, _urllib2, base64, sys, time 
browser = mechanize.Browser()
browser.set_handle_robots(False)

def findClass(var):
    browser.open("https://banweb.banner.vt.edu/ssb/prod/HZSKVTSC.P_ProcRequest")
    get = browser.response().read()    #get = html of page
    #select form, form is 0
    browser.select_form(nr=0)
    browser["TERMYEAR"] = ["201401"]
    browser["open_only"] = ["on"] 
    browser["crn"] = var
    answer = browser.submit()
    newGet = browser.response().read()   
    if "There was a problem with your request:" in newGet: 
        print newGet
        time.sleep(5)
        findClass(var)
    else:
        add(var)

def add(var):
    browser.open("https://banweb.banner.vt.edu/ssomanager_prod/c/SSB")
    browser.select_form(nr=0)
    #INPUT USERNAME AND PASSWORD HERE
    browser["username"] = "USERNAME"
    browser["password"] = "PASSWORD"
    browser.submit()
    browser.open("https://banweb.banner.vt.edu/ssb/prod/twbkwbis.P_GenMenu?name=bmenu.P_StuMainMnu")
    browser.open("https://banweb.banner.vt.edu/ssb/prod/hzskstat.P_DispRegStatPage")
    print browser.geturl()
    if "/ssb/prod/bwskfreg.P_AddDropCrse?term_in=201401" in browser.response().read():
        browser.response().read()
        browser.follow_link(text='Drop/Add', nr=0)
        print browser.response().read() 
        print browser.geturl()
        browser.select_form(nr=1)
        c = browser.find_control(id = "crn_id1") 
        c.readonly = False
        c._value = var
        browser.submit()
        
    else:
        print "Cannot use Add-Drop at this time" 
    
    
do = raw_input("CRN you want? ")
findClass(do)
