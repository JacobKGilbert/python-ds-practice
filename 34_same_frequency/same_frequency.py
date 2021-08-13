from collections import Counter

def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    count_num1 = Counter(str(num1))
    count_num2 = Counter(str(num2))

    if sorted(count_num1.items()) == sorted(count_num2.items()):
        return True
    
    return False