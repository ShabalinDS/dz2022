class Test:
    @staticmethod
    def assert_equals(a, b, *args, **kwargs):
        assert a == b
        print('Passed')


#Problem https://edabit.com/challenge/gzmFeaXwFv8X6pBGq (1 point)
def series_resistance(lst):
	s = 0
	for i in lst:
	 		s+= i
	if s > 1:
	 		 return str(s) + ' ohms'
	else:
	 		 return str(s) + ' ohm'

Test.assert_equals(series_resistance([1, 5, 6, 3]), "15 ohms")
Test.assert_equals(series_resistance([0.2, 0.3, 0.4]), "0.9 ohm")
Test.assert_equals(series_resistance([10,12, 1, 10]), "33 ohms")
Test.assert_equals(series_resistance([10,13, 3.8, 20, 10]), "56.8 ohms")
Test.assert_equals(series_resistance([0.5, 0.5]), "1.0 ohm")
Test.assert_equals(series_resistance([16, 30, 22.8, 4]), "72.8 ohms")
Test.assert_equals(series_resistance([20, 15, 32.5, 2]), "69.5 ohms")
Test.assert_equals(series_resistance([52, 22, 20, 30]), "124 ohms")
Test.assert_equals(series_resistance([10, 12, 32, 4.9, 5, 6, 71]), "140.9 ohms")


#Problem https://edabit.com/challenge/3DAkZHv2LZjgqWbvW (2 point)

def is_adjacent(matrix, node1, node2):
		if matrix[node1][node2] == 1:
				return True
		else:
		    return False

matrix = [[0,1,0,0],[1,0,1,1],[0,1,0,1],[0,1,1,0]]
Test.assert_equals(is_adjacent(matrix, 0, 1), True)
Test.assert_equals(is_adjacent(matrix, 0, 2), False)
Test.assert_equals(is_adjacent(matrix, 2, 1), True)

matrix = [[0,1,0,1,1], [1,0,1,0,0],[0,1,0,1,0],[1,0,1,0,1],[1,0,0,1,0]]
Test.assert_equals(is_adjacent(matrix, 0, 3), True)
Test.assert_equals(is_adjacent(matrix, 1, 4), False)
Test.assert_equals(is_adjacent(matrix, 3, 2), True)


#Problem https://edabit.com/challenge/guR6aa2zytfZvywMS (2 point)

def total_overs(balls):
	q = (balls%6)/10
	w = (balls-q)//6
	return w + q

Test.assert_equals(total_overs(2400), 400)
Test.assert_equals(total_overs(164), 27.2)
Test.assert_equals(total_overs(945), 157.3)
Test.assert_equals(total_overs(5), 0.5)
Test.assert_equals(total_overs(7), 1.1)
Test.assert_equals(total_overs(15), 2.3)
Test.assert_equals(total_overs(0), 0)

#Problem https://edabit.com/challenge/cXnkmRdxqJrwdsP4n (1 point)

def dis(price, discount):
	return price*(100-discount)/100

Test.assert_equals(dis(100, 75), 25)
Test.assert_equals(dis(211, 50), 105.5)
Test.assert_equals(dis(593, 61), 231.27)
Test.assert_equals(dis(1693, 80), 338.6)
Test.assert_equals(dis(700, 10), 630)

#Problem https://edabit.com/challenge/4me7LifXBwj5rhL4n (1 point)

import math
def circle_or_square(rad, area):
	if (2*3.14*rad > 4*math.sqrt(area)):
	    return True
	else:
	    return False

Test.assert_equals(circle_or_square(16, 625), True)
Test.assert_equals(circle_or_square(8, 144), True)
Test.assert_equals(circle_or_square(15, 400), True)
Test.assert_equals(circle_or_square(5, 100), False)
Test.assert_equals(circle_or_square(18, 900), False)
Test.assert_equals(circle_or_square(1, 4), False)

#Problem https://edabit.com/challenge/pfn6QRn6eiTHEPpSs (2 point)

def int_to_str(num):
	return int(num)

def str_to_int(num):
	return str(num)

str, int = int, str

if str(4) == '4' and int('4') == 4:
	print('**EXTRA POINTS**')
	print('You have successfully de-drunken Python')

Test.assert_equals(int_to_str(4), '4')
Test.assert_equals(int_to_str(65), '65')
Test.assert_equals(int_to_str(29348), '29348')
Test.assert_equals(int_to_str(49583908545), '49583908545')

Test.assert_equals(str_to_int('4'), 4)
Test.assert_equals(str_to_int('65'), 65)
Test.assert_equals(str_to_int('29348'), 29348)
Test.assert_equals(str_to_int('49583908545'), 49583908545)

#Problem https://edabit.com/challenge/Ns4Sjh7KK58ofAph8 (1 point)

import math
def is_triplet(n1, n2, n3):
		q = min(n1,n2, n3)
		w = max(n1,n2,n3)
		e = math.sqrt(w*w - q*q)
		if (e == n1) or (e == n2) or (e == n3):
				return True
		else:
				return False

Test.assert_equals(is_triplet(3, 4, 5), True)
Test.assert_equals(is_triplet(1, 2, 3), False)
Test.assert_equals(is_triplet(3, 18, 8), False)
Test.assert_equals(is_triplet(7, 12, 7), False)
Test.assert_equals(is_triplet(13, 5, 12), True)
Test.assert_equals(is_triplet(12, 20, 18), False)
Test.assert_equals(is_triplet(17, 14, 2), False)
Test.assert_equals(is_triplet(6, 15, 12), False)
Test.assert_equals(is_triplet(60, 61, 11), True)
Test.assert_equals(is_triplet(7, 13, 15), False)
Test.assert_equals(is_triplet(12, 18, 7), False)
Test.assert_equals(is_triplet(8, 17, 15), True)
Test.assert_equals(is_triplet(3120, 79, 3121), True)

#Problem https://edabit.com/challenge/o2AKq4xy3nfZabKXL (2 point)

Test.assert_equals(solutions(1, 0, -1), 2)
Test.assert_equals(solutions(1, 0, 0), 1)
Test.assert_equals(solutions(1, 0, 1), 0)
Test.assert_equals(solutions(200, 420, 800), 0)
Test.assert_equals(solutions(200, 420, -800), 2)
Test.assert_equals(solutions(1000, 1000, 0), 2)
Test.assert_equals(solutions(10000, 400, 4), 1)

def solutions(a, b, c):
	d = b*b - 4*a*c
	if d > 0 :
			return 2
	elif d == 0:
	    return 1
	else:
	    return 0

#Problem https://edabit.com/challenge/x6McEkHer8A3Hke2q (2 point)

def factorial(num):
	if num > 1:
	    return num*factorial(num-1)
	else:
	    return 1

Test.assert_equals(factorial(7), 5040)
Test.assert_equals(factorial(1), 1)
Test.assert_equals(factorial(9), 362880)
Test.assert_equals(factorial(2), 2)


#Problem https://edabit.com/challenge/TiqTew3PcofZgdbR4 (1 point)

def bitwise_and(n1, n2):
	return n1&n2

def bitwise_or(n1, n2):
	return n1|n2

def bitwise_xor(n1, n2):
	return n1^n2

Test.assert_equals(bitwise_and(7, 12), 4)
Test.assert_equals(bitwise_or(7, 12), 15)
Test.assert_equals(bitwise_xor(7, 12), 11)

Test.assert_equals(bitwise_and(32, 17), 0)
Test.assert_equals(bitwise_or(32, 17), 49)
Test.assert_equals(bitwise_xor(32, 17), 49)

Test.assert_equals(bitwise_and(13, 19), 1)
Test.assert_equals(bitwise_or(13, 19), 31)
Test.assert_equals(bitwise_xor(13, 19), 30)

