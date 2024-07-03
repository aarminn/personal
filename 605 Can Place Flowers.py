class Solution(object):
    def canPlaceFlowers(flowerbed, n):    

        r = 0
        lfb = len(flowerbed)
        pfb = [0] * lfb
        s = 1
        if flowerbed[0] == 0:
            if lfb > 2 and flowerbed[1] == 0:
                pfb[0] = 1
                r += 1
                s = 2
            elif lfb == 1:
                return True
            elif lfb == 2:
                if (flowerbed[0]+flowerbed[1] == 0) and n <=1 :
                    return True
                else:
                    return False
        elif lfb == 1 & n >= 1:
            return False


        for i in range(s,lfb-2):
            if flowerbed[i] + flowerbed[i-1] + flowerbed[i+1] + pfb[i-1] == 0 :
                pfb[i] = 1
                r += 1
        if  flowerbed[lfb-2] + flowerbed[lfb-1] + pfb[lfb-1] == 0 :
            pfb[lfb-1] = 1
            r += 1
        if n <= r:
            print("True")
            return True
        else :
            print("False")
            return False
            
flowerbed=[0,0]
n=2
Solution.canPlaceFlowers(flowerbed,n)

  
        

            
