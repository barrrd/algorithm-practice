from itertools import product


def solution(users, emoticons):
    answer = []
    discounts = [10, 20, 30, 40]
    
    # print(len(list(product(discounts, repeat = len(emoticons)))))
    # 1. rates 정하기
    cand = []
    best = 0
    
    
    for rates in product(discounts, repeat = len(emoticons)):
        tbest = 0
        tmoney = 0
        
        for user in users:
            urate, umax = user
            money = 0
            
            
            for i, rate in enumerate(rates):
                # 구매
                if rate >= urate:
                    money += emoticons[i]*(100 - rate)*0.01
            
            # 1. 가입
            if money >= umax:
                tbest += 1
            # 2. not 가입
            else:
                tmoney += money
        
        # 3. 
        if tbest >= best:
            
            if tbest == best:
                cand.append((best, tmoney))
            else:
                best = tbest
                cand = [(best, tmoney)]
    cand.sort(key = lambda x: -x[1])
    
    num, money = cand[0]
    
    answer = [num, int(money)]
            
                    
        
        
    return answer

