# title : ALternating Charecters
#given a string containing characters A nad B only
# we have to change it into a string such that there 
# are no matching adjacent characters. we are allowed
# to delete zero or more characters in the string.

def alternating(a):
    previous = a[0]
    delete = 0
    for i in a[1:]:

        if previous == i:
            delete += 1

        previous = i
    print(f'Answer is : {delete}')

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a = input()
        alternating(a)