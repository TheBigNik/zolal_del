def find_good_numbers(zolalC):
    for n in zolalC:
        count_zolal_del = 0
        
        for x in range(n):
            valid = True
            
            for i in range(n):
                if i ^ x >= n:
                    valid = False
                    break
            
            if valid:
                count_zolal_del += 1

        print(count_zolal_del)


t = int(input())
zolalC = [int(input()) for _ in range(t)]

find_good_numbers(zolalC)
