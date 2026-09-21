seed=1
def set_seed(value):
    global seed
    seed=value
def uniform_random(low,high):
    global seed
    M=2147483648
    A=1103515245
    C=12345
    seed=(A*seed+C)%M
    r=seed/M
    return low+(high-low)*r
def my_sqrt(x):
    if x==0:return 0
    guess=x/2
    while True:
        error=guess*guess-x
        if error<0:error=-error
        if error<0.000001:break
        guess=(guess+x/guess)/2
    return guess
def my_log(x):
    y=(x-1)/(x+1)
    result=0
    term=y
    n=1
    while True:
        temp=term
        if temp<0:temp=-temp
        if temp<0.000001:break
        result=result+term/n
        term=term*y*y
        n=n+2
    return 2*result
def generate_gaussian(mu,sigma,N):
    gaussian_values=[]
    while len(gaussian_values)<N:
        u1=uniform_random(-1,1)
        u2=uniform_random(-1,1)
        s=u1*u1+u2*u2
        if s>0 and s<1:
            k=my_sqrt((-2*my_log(s))/s)
            x=mu+sigma*(u1*k)
            y=mu+sigma*(u2*k)
            gaussian_values.append(x)
            if len(gaussian_values)<N:
                gaussian_values.append(y)
    return gaussian_values