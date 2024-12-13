from typing import List

def gpa_award(gpa: float, major: str, 
                             req_gpa: float, req_major: str) -> bool:
     """
    Return True if and only if gpa is greater than or equal to req_gpa and 
    major is equal to req_major.

    >>> gpa_award(4.0, 'CS', 3.5, 'CS')
    True
    >>> gpa_award(4.0, 'Econ', 3.5, 'CS')
    False
    >>> gpa_award(3.3, 'CS', 3.5, 'CS')
    False
    """
    if gpa >= req_gpa and major == req_major:
        return True
    return False

def get_list(board: List[List[str]], row_num: int) -> List[str]:
    
    """
    Return row <row_num> of <board>
    
    >>> b = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
    >>> get_list(b, 0)
    ['a', 'b', 'c']
    >>> get_list(b, 2)
    ['g', 'h', 'i']
    """
    return board[row_num]

def contain_names(string: list[str]) -> bool:
    """
    
    Return Ture if the char in string contains "Alice" , "Daniel" , "Anthony", or "Minsoo"

    >>> x = ["Test", "Chemistry", "Math"]
    >>> contain_names(x)
    False
    >>> x = ["Test", "Math", "Alice"]
    >>> contain_names(x)
    True

    """
    for char in string:
        if name in ["Alice", "Daniel", "Anthony", "Minsoo"]:
            return True
    return False