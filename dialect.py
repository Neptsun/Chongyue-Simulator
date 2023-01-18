import random
import sys

def gen(n:int) -> str:
    dic=['形不成形，意不在意，再去练一练吧','千招百式在一息','劲发江潮落，气收秋毫平','你们解决问题，还是只会争强斗狠是吧']
    s=''
    for i in range(n):
        tmp=random.choice(dic)
        s+=tmp[:-(int(random.random()*len(tmp)))]
    s+=random.choice(dic)
    return s



if __name__=="__main__":
    if len(sys.argv)==1:
        print('usage: python3 dialect.py (number)')
    else:
        print(gen(int(sys.argv[1])))
