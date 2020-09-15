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
    
        
    
