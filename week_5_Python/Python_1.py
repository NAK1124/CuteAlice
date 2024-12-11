def grading_system(grade,req_grade: float) -> bool:
    """
    Return True if and only if grade is greater than or equal to req_grade.
    
    >>> grading_system(95, 80)
    True
    >>> grading_system(30, 90)
    False
    >>> grading_system(80, 80)
    True
    """    
    if grade >= req_grade:
        return True
    return False

def yesping(yyy: str) -> bool :
    """
    Return True if the string begins with y or Y and follows by "aeiouAEIOU".
      
    For this function, a and A are the same
      
    >>> yesping("YUP!!!")
    True
    >>> yesping("cat eyes")
    False
    >>> yesping("yluo")
    False
    """    
    if yyy[0] in "yY" and yyy[1] in "aeiouAEIOU":
        return True
    return False

def x_checker(x:str) -> bool:
    '''
    Return True is the string contains x. In this case, x and X are not the same.
    >>> x_checker("xlo")
    True
    >>> x_checker("dde")
    False
    >>> x_checker("dxd")
    True
    '''
    for char in x:
        if char in "x":
            return True
    return False