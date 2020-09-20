#IMEIs are 14 digits + 1 check digit
#The check digit is calculated using the Luhn algorithm
#For the IMEI 12345678901234 the check digit would be 7 calculated using the following:
#First double every second digit making the following 1,4,3,8,5,12,7,16,9,0,1,4,3,8
#Break everything down into single digits (so 12 would become 1 and 2) and add it all together 1+4+3+8+5+1+2+7+1+6+9+0+1+4+3+8 = 63
#The check digit is the amount that needs to be added to make the number divisible by 10 in the above case it can be calculated by the following: 10-(63%10)
#For a better description of how to do this visit https://en.wikipedia.org/wiki/International_Mobile_Equipment_Identity#Check_digit_computation
#Rather than breaking 2-digit numbers down into 2 separate digits I am just subtracting 9 since these numbers will always be 18 or less



import os

def validate_checksum(IMEI):
    sum = 0
    for i in range(len(IMEI)):
        if i % 2 == 1: #if it is an even digit - double it and add the numbers together
            temp = IMEI[i] * 2
            if temp > 9:
                temp -= 9
            sum += temp
        else:
            sum += IMEI[i]
    
    return sum
    
def find_close_valids(IMEI,sum):
    vIMIE = []
    for i in range(0,len(IMEI),2):
        vIMEI = IMEI[:]
        vIMEI[i] -= sum
        if vIMEI[i] < 0:
            vIMEI[i] += 10
        print("".join(map(str,vIMEI)))
    for i in range(1,len(IMEI),2):
        vIMEI = IMEI[:]
        vIMEI[i] *= 2
        if vIMEI[i] > 9:
            vIMEI[i] -= 9
        vIMEI[i] -= sum
        if vIMEI[i] < 0:
            vIMEI[i] += 10
        if vIMEI[i] % 2 == 1:
            vIMEI[i] += 9
        vIMEI[i] = int(vIMEI[i] / 2)
        print("".join(map(str,vIMEI)))
        



if __name__ == '__main__':
    while True:
        strIMEI = str(input('Enter IMEI to be verified:'))
        if len(strIMEI) == 15:
            break
        print(f'{strIMEI} is not 15 digits long. IMEI must be 15 digits long.')
        
    #break IMEI down into a list
    IMEIlist = []
    for i in range(len(strIMEI)):
        IMEIlist.append(int(strIMEI[i]))
    
    sum = validate_checksum(IMEIlist) % 10
    
    if sum == 0:
        print(f'{strIMEI} is a valid IMEI')
    else:
        print(f'{strIMEI} is not valid')
        print('Press Enter to find valid combonations where one digit is changed')
        os.system("PAUSE")
        find_close_valids(IMEIlist,sum)
    
        
    
