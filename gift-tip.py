while(1):
    n=int(input("請投入30元: "))
    if n%30==0:
        y=n/30
        z=0
        while z<y:
            c=int(input("請輸入一個1到10000的數字: "))
            if c==618:
                print("a,b是金屬製品")
            elif c==416:
                print("b,c和手有關")
            elif c==1221:
                print("a,c可以變漂亮")
            elif c==600:
                print("ac其中一個是aznacav")
            elif c==6499:
                print("bc其中一個是eerfsinni")
            elif c==2398:
                print("a,b是飾品")
            elif c==520:
                print("c是護手霜")
            else :
                print("答錯!!在猜一次")
            z+=1
            print("可猜次數剩下 ",y-z)
        print("餘額不足")
    else :
        print("請投入30元或者30元的倍數")
