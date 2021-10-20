import sys
def find(num, k):

    while(k%4 == 0):
        k = k//4
    if num%2 == 1:
        if (k%2 == 1):
            if k%6 == 1:
                print(1, 3,sep=' ')
            if k%6 == 3:
                print(3, 2,sep=' ')
            if k%6 == 5:
                print(2, 1,sep=' ')
        else:
            if k%12 == 2:
                print(1, 2,sep=' ')
            if k%12 == 6:
                print(2, 3,sep=' ')
            if k%12 == 10:
                print(3, 1,sep=' ')
    if num%2 == 0:

        if k%2 == 1:

            if k%6 == 1:
                print(1, 2,sep=' ')
            if k%6 == 3:
                print(2, 3,sep=' ')
            if k%6 == 5:
                print(3, 1,sep=' ')

        else:
            if k%12 == 2:
                print(1, 3,sep=' ')
            if k%12 == 6:
                print(3, 2,sep=' ')
            if k%12 == 10:
                print(2, 1,sep=' ')


#test_case = int(str(sys.stdin.readline().rstrip()))
#for i in range(0, test_case):
    #num_disks, confirm_count = map(int,sys.stdin.readline().split())
find(5,16)




