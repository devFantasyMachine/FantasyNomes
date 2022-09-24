"""

    LICENCE APACHE 2.0

@Author : Fantasy Machine

"""


class Polynome(object):

    def __init__(self, argv):
        """
        The object that represent polynome ( a*X^n)

        Parameters
        ----------
        argv :
            La liste des coefficients 
        """

        if isinstance(argv, list) : 

            self.__monomes = {}

            for i in range(len(argv)) :

                if argv[i] != 0 :

                    self.__monomes.setdefault(i, argv[i])

        elif isinstance(argv, dict ) :
            self.__monomes = argv

        else :
            raise TypeError()
        
        keys = list(self.__monomes.keys()) 
        for i in keys:
            if self.__monomes.get(i) == 0 or self.__monomes.get(i) == 0.0 :
                self.__monomes.pop(i)

    def deg(self) -> int:

        if len(self.__monomes.keys()) == 0 :

            return 0

        else :

            return max(self.__monomes.keys()) 

    def __len__(self) :
        return self.deg()

    def __str__(self) -> str:

        indices = sorted(self.__monomes.keys())

        if len(indices) == 0 :

            return "0"
        
        else :

            val = ""
            for i in indices:

                if i == 0 :

                    val = str(self.__monomes.get(i))

                else :

                    if  len(val) > 0 and val[0] != "-" : 

                        val =  str(self.__monomes.get(i)) + "*X^" + str(i) +  "+"   +  val
                    else :
                        val =  str(self.__monomes.get(i)) + "*X^" + str(i) +  val

            return val

    def __repr__(self) -> str:
        return self.__str__()

    def __gt__(self, other) -> bool:
        return self.deg() > other.deg()  

    def __lt__(self, other) -> bool:
        return self.deg() < other.deg() 

    def __eq__(self, other) -> bool:

        if isinstance(other, int) or isinstance(other, float) :

            if len(self.__monomes.keys()) == 1 : 

                if 0 in self.__monomes.keys() and self.__monomes.get(0) == other :
                    return True

            return False

        elif isinstance(other, Polynome) :

            if self > other or other > self :
                return False

            elif len(self.__monomes.keys()) == len(other.__monomes.keys()) :

                for i in other.__monomes.keys() :

                    if not i in self.__monomes.keys() :
                        return False
                    
                    elif self.__monomes.get(i) != other.__monomes.get(i) : 
                        return False

                return True

            else :

                return False
      
        else :
            raise TypeError("Second parameter must be integer, float or polynome") 

    def __neg__(self):

        new_argv = {}

        for i in self.__monomes.keys() : 
            new_argv.setdefault(i, -self.__monomes.get(i))

        return Polynome(new_argv)
    
    def __sub__(self, other):
        temp = -other 
        return self + temp

    def __add__(self, other):

        new_argv = self.__monomes.copy() 

        if isinstance(other, int) or isinstance(other, float) :

            if not 0 in new_argv.keys() :
                 new_argv.setdefault(0, other)
            
            else : 

                val = new_argv.pop(0)
                new_argv.setdefault(0, val + other)

        elif isinstance(other, Polynome) :

            for i in other.__monomes.keys() :

                val = 0
                
                if i in new_argv.keys() : 

                    val = new_argv.pop(i)
                    new_argv.setdefault(i, val + other.__monomes.get(i))  

                else :

                    new_argv.setdefault(i, other.__monomes.get(i))  
      
        else :
            raise TypeError("Second parameter must be integer, float or polynome") 

        return Polynome(new_argv)

    def __mul__(self, other):

        new_argv = {}

        if isinstance(other, int) or isinstance(other, float) :

            for i in self.__monomes.keys() : 
                new_argv.setdefault(i, self.__monomes.get(i) * other)

            return Polynome(argv=new_argv)

        elif isinstance(other, Polynome) :
        
            for i in self.__monomes.keys() :

                for j in other.__monomes.keys() :

                    val = 0
                    
                    if i+j in new_argv.keys() : 

                        val = new_argv.pop(i+j)
                        new_argv.setdefault(i+j, val + self.__monomes[i] * other.__monomes.get(j))  

                    else :

                        new_argv.setdefault(i+j, self.__monomes[i] * other.__monomes.get(j))  

            return Polynome(argv=new_argv)

        else :
            raise TypeError("Second param must be int, float or Polynome")

    def __truediv__(self, other):
        """first quotient, second reste"""

        if isinstance(other, int) or isinstance(other, float) :
            
            new_argv = {}

            for i in self.__monomes.keys() : 
                new_argv.setdefault(i, self.__monomes.get(i) / other)

            return Polynome(argv=new_argv), 0

        elif isinstance(other, Polynome) :

            indices_div = sorted(other.__monomes.keys())

            res = Polynome(self.__monomes.copy()) 
            div = Polynome({})  

            while res.deg() >= other.deg() :

                indices = sorted(res.__monomes.keys())

                fact = res.__monomes.get(indices[-1])/other.__monomes.get(indices_div[-1])

                res = res - other * Polynome({ indices[-1] - indices_div[-1] : fact}) 
                div = div + Polynome({ indices[-1] - indices_div[-1] : fact}) 

            return div, res
        
        else :
            raise TypeError("Second param must be int, float or Polynome")






