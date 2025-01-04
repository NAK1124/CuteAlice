def zigzagzip(s1:str, s2:str) -> str:
    """
    PreconditionL len(s1) == len(s2)
    
    Return a string made up of alternating letters from s1 and s2,
    starting with s1[0], then s2[1], s1[2], and so on.
    
    >>> zigzagzip("abc", "123")
    "a2c"
    >>> zigzagzip("abcd","1234")
    "a2c4"
    
    """
    answer = ""
    for letter in range(len(s1)):
        if letter % 2 == 0:
            answer += s1[letter]
        else:
            answer += s2[letter]
    return answer
        
def is_palindrome(s: str) -> bool:
    """Return True if and only if s is a palindrome.
    >>> is_palindrome('noon')
    True
    >>> is_palindrome('racecar')
    True
    >>> is_palindrome('dented')
    False
    """
    if s == s[::-1]:
        return True
    else:
        return False

from typing import Dict, List

def get_num_orders(meal_to_tables: Dict[str, List[int]], meal: str) -> int:
    """
    Return the number of orders for meal in meal_to_tables. 
    The values in the dictionary represents table numbers. 
    For example, {'stew': [4, 1], 'eggs': [6]} means table 4 and 1 ordered stew
    while table 6 ordered eggs.
    
    >>> m_to_t = {'stew': [4, 1], 'eggs': [6]}
    >>> get_num_orders(m_to_t, 'stew')
    2
    >>> get_num_orders(m_to_t, 'eggs')
    1
    >>> get_num_orders(m_to_t, 'brussel sprouts')
    0
    """
    return len(meal_to_tables.get(meal,[]))

from typing import List

def count_duplicates_v1(lst: List[int]) -> int:
    """Return the number of duplicates in lst.
    
    Precondition: each item in lst occurs either once or twice.
    
    >>> count_duplicates_v1([1, 2, 3, 4])
    0
    >>> count_duplicates_v1([2, 4, 3, 3, 1, 4])
    2
    """
    count = 0
    for num in set(lst):
        if lst.count(num) == 2:
            count += 1
    return count
