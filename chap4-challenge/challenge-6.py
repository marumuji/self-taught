def squared(x=2):
  """ return multiplied by 2.
  Return x ** 2
  :param x: int.
  :return: x multiplied by 2.
  """
  return x ** 2

def print_string(str):
    """ print passed string 
    :param x: string.
    """
    print(str)

def multi_arg(arg1, arg2, arg3, arg4=10, arg5=20):
    """ print passed multiple arguments
    :param x, y, z: string.
    """
    print(arg1, arg2, arg3, arg4, arg5)

def divide(num):
    """ divide passed argument by 2.
    :param num: int.
    :return int divided by 2
    """
    return (int(num / 2))

def multiply(num):
    """ print mutiply passed argument by 4.
    :param num: int.
    """
    print(int(num * 4))

def convertFloat(num):
    """ convert passed argument to float.
    :param num: int.
    :return: converted float value. 
    """
    try:
        num = float(num)
        return num
    except (TypeError, ValueError, ArithmeticError):
       print("num cannot convert float")
