Plus Minus
==========

Problem Statement
-----------------

You're given an array containing integer values. You need to print the fraction of the count of positive numbers, negative numbers and zeroes to the total numbers. Print the value of the fractions in decimal form corrected to 3 decimal places.

Input Format
------------

The first line contains ***N***: the size of the array. 
The next line contains ***N*** space separated integers ***A<sup>1</sup>, A<sup>2</sup>, A<sup>3</sup>, ⋯, A<sup>N</sup>***.

Constraints
-----------

***1 ≤ N ≤ 100*** 
***−100 ≤ A<sub>i</sub> ≤ 100***

Output Format
-------------

Output the three values each on a different line equal to the fraction of the count of positive numbers, negative numbers and zeroes to the total numbers respectively. Correct the fraction to 3 decimal places.

Sample Input
------------

	6
	-4 3 -9 0 4 1          

Sample Output
-------------

	0.500
	0.333
	0.167

Explanation
-----------

There are 3 positive numbers, 2 negative numbers and 1 zero in the array. 
The fraction of the positive numbers, negative numbers and zeroes are 3/6=0.500, 2/6=0.333 and 1/6=0.167 respectively.

Note: This challenge introduces precision problems. You can even print the output to 4 decimal places and above, but only the difference at the 3rd decimal digit is noted. That is the reason you'll notice testcases have much higher precision (more decimal places) than required. 
Answers with absolute error up to ***10<sup>−4</sup>*** will be accepted.