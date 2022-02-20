one=int(input('enter temperature:'))
two=str(input('F or C:')).lower()
if two == 'c':
    result_f =  one * 9/5 + 32 
    rsf=str(result_f)
    print('temperature in F = '+ rsf)
elif two=='f':
    result_c=(one - 32) * 5/9 
    rsc=str(result_c)
    print('temperature in C = ' + rsc)
else:
    print('wrong input')

