#Not very secure
def alphanumeric(password):
    if len(password) > 0 :
        for elem in password :
            if elem.isalpha() or elem.isnumeric() : 
                continue
            else:
                return False
        return True
    else:
        return False
    
print(alphanumeric('sjdfi'))
print(alphanumeric('sjdf01i'))
print(alphanumeric('sjdf__2'))