def F(x):

    if x <= 0:
    #make sure the input number is greatter than 0
        print("Your number is too small.")

        return None
        # if x < = 0 it should not print any number
    
    elif x==1:
    # if x = 1 it should stop
        
        return 1

    else:
        
        x=x*F(x-1)
        #calculate
        
        return x
print(F(1))
