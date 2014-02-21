minimum_diagonal_matrix
=======================

Minimum diagonal in a matrix - Python

Is a simple python script that allow you to rearrange a matrix in order to have the minimum diagonal calculate.

For example:

1) 10 97 96 64 41
2) 21 65 97 28 70
3) 27 36 18 74 47
4) 28 68 32 76 92
5) 12 62 54 93 66

If the order of columns is changed to (5, 3, 4, 2, 1), the
matrix will look like:

5) 12 62 54 93 66
3) 27 36 18 74 47
4) 28 68 32 76 92
2) 21 65 97 28 70
1) 10 97 96 64 41

The sum of the diagonal is 12 + 36 + 32 + 28 + 41 = 149,
which is also the lowest possible sum.

In order to launch the script you can pass the matrix from the command line as below:

python robocat.py  --l 1,200,3,4-2,3,4,5-2,400,5,6-3,5,6,100

=======================
The original matrix is:
=======================
0 => ['1', '200', '3', '4']
1 => ['2', '3', '4', '5']
2 => ['2', '400', '5', '6']
3 => ['3', '5', '6', '100']

===============================
The Minimum diagonal Matrix is:
===============================
2 => ['2', '400', '5', '6']
1 => ['2', '3', '4', '5']
3 => ['3', '5', '6', '100']
0 => ['1', '200', '3', '4']

The sum is: 15


The matrix is passed as a string where the "," separates the columns while "-" separates the rows.

