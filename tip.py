while(1):
    import random
    n=int(input("請投入50元: "))
    if n%50==0 :
        k=n/50
        z=0
        while z<k: 
            
            data=int(random.uniform(0,8))
            print("你擲出的數字是 ",data)
            if data==0:
                print("提示是生日")
            elif data==1:
                print("提示是紀念日")
            elif data==2:
                print("提示是生日總和")
            elif data==3:
                print("提示是總共幾天")
            elif data==4:
                print("提示是電話末四碼")
            elif data==5:
                print("提示是身分證末四碼")
            elif data==6:
                print("提示是我愛你")
            else :
                print("哈哈!恭喜沒有中獎")
            z+=1
    else :
        print("請投入50元或者50元的倍數")
