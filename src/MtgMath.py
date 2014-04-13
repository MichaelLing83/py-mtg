
class MtgMath:
    '''
    Mathematics methods. 
    '''

    __n_factorial__ = dict()
    __n_factorial_max_key__ = 0
    __n_factorial__[__n_factorial_max_key__] = 1
    
    def __init__(self):
        pass
    
    @classmethod
    def C(cls, n, r):
        '''
        Number of possible solutions of "n choose r", i.e. Choose r items from total n items.
        '''
        if r > n or n < 0 or r < 0:
            raise ValueError("Invalid input for 'n choose r' calculation with n=%d, r=%d." % (n, r))
        return MtgMath.n_factorial(n) / ( MtgMath.n_factorial(r) * MtgMath.n_factorial(n-r) )
    
    @classmethod
    def n_factorial(cls, n):
        '''
        Return "n factorial".
        
        @return n! (int): note 0!=1
        '''
        if n < 0:
            raise ValueError("n=%d is not valid for factorial calculation!" % n)
        elif n == 0:
            return 1
        else:
            if n > MtgMath.__n_factorial_max_key__:
                for x in range(MtgMath.__n_factorial_max_key__+1, n+1):
                    MtgMath.__n_factorial__[x] = MtgMath.__n_factorial__[x-1] * x
            return MtgMath.__n_factorial__[n]