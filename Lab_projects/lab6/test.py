import time,random
user={'user':None,'login_time':None,'timeout':0.000003,}

def timmer(func):
    def wrapper(*args,**kwargs):
        s1=time.time()
        res=func(*args,**kwargs)
        s2=time.time()
        print('%s' %(s2-s1))
        return res
    return wrapper


def auth(func):
    def wrapper(*args,**kwargs):
        if user['user']:
            timeout=time.time()-user['login_time']
            if timeout < user['timeout']:
                return func(*args,**kwargs)
        name=input('name>>: ').strip()
        password=input('password>>: ').strip()
        if name == 'egon' and password == '123':
            user['user']=name
            user['login_time']=time.time()
            res=func(*args,**kwargs)
            return res
    return wrapper

@auth
def index():
    time.sleep(random.randrange(3))
    print('welcome to index')

@auth
def home(name):
    time.sleep(random.randrange(3))
    print('welcome %s to home ' %name)

index()
home('egon')
