#  Recurrencia
#
# t(n,w) = 0                            : if n <= 0 or w = 0
#        = t(n-1,w)                     : if w(n) > w
#        = max(t(n-1,w),t(n-1,w-w(n))+B(n))
#
import ks_utils


# Modify this code to incorporate your implementation.
# Tests installed in this demo will allow you to check
# your implementation of the Knapsack 0/1 problem using
# memoization or tabulation.

def solve_exam(items, capacity):


    cache={}

    def getKey(n,w):
        return str(n) + '|' + str(w)


    def t(n,w):
        key=getKey(n,w)

        if key in cache:
            return cache[key]

        elif n<0 or w==0:
            cache[key]=0
            result=0

        else:
            item=items[n]
            wi=item.weight
            vi=item.value

            if wi > w:
                result=t(n-1,w)
            else:
                result=max(t(n-1,w),t(n-1,w-wi)+vi)

            cache[key]=result

        return result


    def getTaken(n,w):

        taken = [0]*len(items)

        i=n
        k=w

        while k>0 and i>=0:
            key_i = getKey(i,k)
            key_i1 = getKey(i-1,k)

            assert key_i  in cache
            assert key_i1 in cache



            if cache[key_i]!=cache[key_i1] :

                taken[ items[i].index ] = 1
                k = k-items[i].weight

            i=i-1

        return taken


    n=len(items)-1

    value = t(n,capacity)

    taken = getTaken(n,capacity)

    return value,taken