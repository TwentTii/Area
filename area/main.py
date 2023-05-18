#A+ Computer Science
#www.apluscompsci.com
import math

def TrapArea( b1, b2, h ):
    # Your code here
    # area = ½ ( base1 + base2 ) x height

    return  0.5*(b1 + b2)*h

print( "{0:.1f}".format(  TrapArea( 3, 3, 3 )  ) )
print( "{0:.1f}".format(  TrapArea( 5, 6, 7 )  ) )
print( "{0:.1f}".format(  TrapArea( 7, 10, 6 )  ) )
print( "{0:.1f}".format(  TrapArea( 13, 9, 3 )  ) )
print( "{0:.1f}".format(  TrapArea( 6, 11, 4 )  ) )
print( "{0:.1f}".format(  TrapArea( 11, 8, 5 )  ) )
print()

def CircArea( r ):
    # Your code here
    r = pow(r, 2)
    return r*math.pi

print( "{0:.1f}".format(  CircArea( 7.5 )  ) )
print( "{0:.1f}".format(  CircArea( 10 )  ) )
print( "{0:.1f}".format(  CircArea( 72.534 )  ) )
print( "{0:.1f}".format(  CircArea( 55 )  ) )
print( "{0:.1f}".format(  CircArea( 101 )  ) )
print( "{0:.1f}".format(  CircArea( 99.952 )  ) )
print( "{0:.1f}".format(  CircArea( 100 )  ) )
print()

def CubeArea( s ):
    # Your code here
    s = pow(s, 2)
    return s*6
print( "{0:.1f}".format(  CubeArea( 112 )  ) )
print( "{0:.1f}".format(  CubeArea( 4 )  ) )
print( "{0:.1f}".format(  CubeArea( 33 )  ) )
print( "{0:.1f}".format(  CubeArea( 50 )  ) )
print( "{0:.1f}".format(  CubeArea( 5 )  ) )
print( "{0:.1f}".format(  CubeArea( 19 )  ) )
print( "{0:.1f}".format(  CubeArea( 111 )  ) )
