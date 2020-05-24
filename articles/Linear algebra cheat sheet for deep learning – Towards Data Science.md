Linear algebra cheat sheet for deep learning – Towards Data Science

# Linear algebra cheat sheet for deep learning

## Beginner’s guide to commonly used operations

[![1*YgpqVXnXZApoBUTfYDCzvQ.png](../_resources/f51712fcbef877a81733f79bcd24d072.png)](https://towardsdatascience.com/@bfortuner?source=post_header_lockup)

[Brendan Fortuner](https://towardsdatascience.com/@bfortuner)
Mar 4, 2017·8 min read

![](../_resources/e248b2fa9aefa3e99620da54adb8e67c.png)![1*XlZoLDzJkT3PR-v969keXQ.png](../_resources/7a2378270f1cd866441fe923c7901d58.png)

During Jeremy Howard’s excellent [deep learning course](http://course.fast.ai/) I realized I was a little rusty on the prerequisites and my fuzziness was impacting my ability to understand concepts like backpropagation. I decided to put together a few wiki pages on these topics to improve my understanding. Here is a very basic intro to some of the more common linear algebra operations used in deep learning. **NEW**: check out [machine learning cheatsheet](http://ml-cheatsheet.readthedocs.io/) for more topics.

#### What is linear algebra?

In the context of deep learning, linear algebra is a mathematical toolbox that offers helpful techniques for manipulating groups of numbers simultaneously. It provides structures like vectors and matrices (spreadsheets) to hold these numbers and new rules for how to add, subtract, multiply, and divide them.

#### Why is it useful?

It turns complicated problems into simple, intuitive, efficiently calculated problems. Here is an example of how linear algebra can achieve greater speed and simplicity.

*# Multiply two arrays *
x = [1,2,3]
y = [2,3,4]
product = []
for i in range(len(x)):
product.append(x[i]*y[i])
*# Linear algebra version*
x = numpy.array([1,2,3])
y = numpy.array([2,3,4])
x * y
After initializing the arrays, the linear algebra approach was 3x faster.

#### **How is it used in deep learning?**

Neural networks store weights in matrices. Linear algebra makes matrix operations fast and easy, especially when training on GPUs. In fact, GPUs were created with vector and matrix operations in mind. Similar to how images can be represented as arrays of pixels, video games generate compelling gaming experiences using enormous, constantly evolving matrices. Instead of processing pixels one-by-one, GPUs manipulate entire matrices of pixels in parallel.

### Vectors

Vectors are 1-dimensional arrays of numbers or terms. In geometry, vectors store the magnitude and direction of a potential change to a point. The vector [3, -2] says go right 3 and down 2. A vector with more than one dimension is called a matrix.

#### Vector notation

There are a variety of ways to represent vectors. Here are a few you might come across in your reading.

![](../_resources/32944184cec3e6587341d8403bc601ee.png)![1*TKIHYegDrAPNowYwfSUIIA.png](../_resources/dad16cd4ce48d2a30bb0333ad7464e22.png)

#### Vectors in geometry

Vectors typically represent movement from a point. They store both the **magnitude** and **direction** of potential changes to a point. The vector [-2,5] says move left 2 units and up 5 units. [Source](http://mathinsight.org/vector_introduction).

![](../_resources/4d12d612233d809b54762055f1c90e49.png)![1*KvtcBmg81-SuT60g8VVckw.png](../_resources/7a778a8f2e51e3011c1f633a41b6537b.png)

v = [-2, 5]

A vector can be applied to any point in space. The vector’s direction equals the slope of the hypotenuse created moving up 5 and left 2. Its magnitude equals the length of the hypotenuse.

#### Scalar operations

Scalar operations involve a vector and a number. You modify the vector in-place by adding, subtracting, or multiplying the number from all the values in the vector.

![](../_resources/c00551255e5f56dfbda63612af062485.png)![1*g7cc0GkA7xrkhoh-__Ok3g.png](../_resources/b4089eb08a63a3f408b65daa52ebdc2b.png)

Scalar addition

#### Elementwise operations

In elementwise operations like addition, subtraction, and division, values that correspond positionally are combined to produce a new vector. The 1st value in vector A is paired with the 1st value in vector B. The 2nd value is paired with the 2nd, and so on. This means the vectors must have equal dimensions to complete the operation.*

![](../_resources/689dbb12a08463d9785f8306441eda89.png)![1*FOAYY9lvg1FPfiHIhm7z5Q.png](../_resources/5c46995e6380d411cadf7a184d703dde.png)

Vector addition
y = np.array([1,2,3])
x = np.array([2,3,4])
y + x = [3, 5, 7]
y - x = [-1, -1, -1]
y / x = [.5, .67, .75]

*See below for details on [broadcasting](https://docs.scipy.org/doc/numpy-1.10.0/user/basics.broadcasting.html) in numpy.

#### Vector multiplication

There are two types of vector multiplication: Dot product and Hadamard product.

#### Dot product

The dot product of two vectors is a scalar. Dot product of vectors and matrices (matrix multiplication) is one of the most important operations in deep learning.

![1*m5enBfhctMzed5ian-YDDQ.png](../_resources/c96a16c3bffb4edb0cd476a351f78a7d.png)
y = np.array([1,2,3])
x = np.array([2,3,4])
np.dot(y,x) = 20

#### Hadamard product

Hadamard Product is elementwise multiplication and it outputs a vector.

![1*pU5dS3VF0f6xvEhziE-x6A.png](../_resources/6b98149111c05c09ac6c0a66ab21c7fe.png)
y = np.array([1,2,3])
x = np.array([2,3,4])
y * x = [2, 6, 12]

#### Vector fields

A vector field shows how far the point *(x,y)* would hypothetically move if we applied a vector function to it like addition or multiplication. Given a point in space, a vector field shows the ***power*** and ***direction*** of our proposed change at a variety of points in a graph.

![](../_resources/4c82f5aa714a2c0274f187fb8fbab87f.png)![1*rAhajNrQkK9-rdt7gdt2hw.png](../_resources/9153a3cefb331eaba930f8adf5d6b315.png)

[Source](https://en.wikipedia.org/wiki/Vector_field)

This vector field is an interesting one since it moves in different directions depending the starting point. The reason is that the vector behind this field stores terms like *2x* or *x²* instead of scalar values like -2 and 5. For each point on the graph, we plug the x-coordinate into *2x* or *x² *and draw an arrow from the starting point to the new location. Vector fields are extremely useful for visualizing machine learning techniques like Gradient Descent.

### Matrices

A matrix is a rectangular grid of numbers or terms (like an Excel spreadsheet) with special rules for addition, subtraction, and multiplication.

#### Matrix dimensions

We describe the dimensions of a matrix in terms of *rows by columns*.

![](../_resources/a5fda8b058579ff5247c72eab2568046.png)![1*x3aV7Yi3kkxRdN6hakkEfA.png](../_resources/8443f2a3439b6c79c451769cbc4a77fe.png)

a = np.array([
[1,2,3],
[4,5,6]
])
a.shape == (2,3)
b = np.array([
[1,2,3]
])
b.shape == (1,3)

#### Matrix scalar operations

Scalar operations with matrices work the same way as they do for vectors. Simply apply the scalar to every element in the matrix — add, subtract, divide, multiply, etc.

![](../_resources/34daca15be3e6264661c2ce90c4add78.png)![1*vCxvsA9nqxwQw2PCk368-g.png](../_resources/075e30ee4eb6a9ee76d55a13c6f3221c.png)

Matrix scalar addition
a = np.array(
[[1,2],
[3,4]])
a + 1
[[2,3],
[4,5]]

#### Matrix elementwise operations

In order to add, subtract, or divide two matrices they must have equal dimensions.* We combine corresponding values in an elementwise fashion to produce a new matrix.

![1*C2_V94g-ePcO4oritMulIA.png](../_resources/02ceec38820b8af7da8debffb3adb676.png)
a = np.array([
[1,2],
[3,4]
])
b = np.array([
[1,2],
[3,4]
])
a + b
[[2, 4],
[6, 8]]
a — b
[[0, 0],
[0, 0]]

#### Numpy broadcasting*

I can’t escape talking about this, since it’s very relevant in practice. In numpy the dimension requirements for elementwise operations are relaxed via a mechanism called [broadcasting](https://docs.scipy.org/doc/numpy-1.10.0/user/basics.broadcasting.html). Two matrices are compatible if the corresponding dimensions in each matrix (rows vs rows, columns vs columns) meet the following requirements:

1. 1.The dimensions are equal, or
2. 2.One dimension is of size 1
a = np.array([
[1],
[2]
])
b = np.array([
[3,4],
[5,6]
])
c = np.array([
[1,2]
])

# Same no. of rows

# Different no. of columns

# but **a** has one column so this works

a * b
[[ 3, 4],
[10, 12]]

# Same no. of columns

# Different no. of rows

# but **c** has one row so this works

b * c
[[ 3, 8],
[5, 12]]

# Different no. of columns

# Different no. of rows

# but both **a** and **c** meet the

# size 1 requirement rule

a + c
[[2, 3],
[3, 4]]

Things get weirder in higher dimensions — 3D, 4D, but for now we won’t worry about that. Understanding 2D operations is a good start.

#### Matrix Hadamard product

Hadamard product of matrices is an elementwise operation. Values that correspond positionally are multiplied to produce a new matrix.

![1*mMMLhITl5GIPE036wwuWeQ.png](../_resources/0c2d84208c7a24df140fc14085add0e4.png)
a = np.array(
[[2,3],
[2,3]])
b = np.array(
[[3,4],
[5,6]])

# Uses python's multiply operator

a * b
[[ 6, 12],
[10, 18]]

In numpy you can take the Hadamard product of a matrix and vector as long as their dimensions meet the requirements of broadcasting.

![1*oUldHfVCEt9GCOUlcZS0Bg.png](../_resources/1a90523bf034241cce19b766db32222b.png)

#### Matrix transpose

Neural networks frequently process weights and inputs of different sizes where the dimensions do not meet the requirements of matrix multiplication. Matrix transpose provides a way to “rotate” one of the matrices so that the operation complies with multiplication requirements and can continue. There are two steps to transpose a matrix:

1. 1.Rotate the matrix right 90°
2. 2.Reverse the order of elements in each row (e.g. [a b c] becomes [c b a])
As an example, transpose matrix **M** into **T**:

![](../_resources/c758dd424c6eb84722b357a87a3cc3ae.png)![1*OAMY1Ih28NwKvjK8IeNjAg.png](../_resources/d4502ccaa468eb4904709c91d2d1ba1f.png)

a = np.array([
[1, 2],
[3, 4]])
a.T
[[1, 3],
[2, 4]]

### Matrix multiplication

Matrix multiplication specifies a set of rules for multiplying matrices together to produce a new matrix.

#### Rules

Not all matrices are eligible for multiplication. In addition, there is a requirement on the dimensions of the resulting matrix output. [Source](https://www.khanacademy.org/math/precalculus/precalc-matrices/properties-of-matrix-multiplication/a/properties-of-matrix-multiplication).

1. 1.The number of ***columns of the 1st*** matrix must equal the number of ***rows of the 2nd***

2. 2.The product of an M x N matrix and an N x K matrix is an M x K matrix. The new matrix takes the ***rows of the 1st*** and ***columns of the 2nd***

#### Steps

Matrix multiplication relies on dot product to multiply various combinations of rows and columns. In the image below, taken from Khan Academy’s excellent linear algebra course, each entry in Matrix C is the dot product of a row in matrix A and a column in matrix B.

![](../_resources/fb81ca6cd41012835ceb4f35e161c82d.png)![1*6VfYsZRssGbVVY88ap_wzA.png](../_resources/71fa82db6fd3fee80019bf8491f227ba.png)

[Source](https://www.khanacademy.org/math/precalculus/precalc-matrices/properties-of-matrix-multiplication/a/properties-of-matrix-multiplication)

The operation ***a1 *·* b1*** means we take the dot product of the 1st row in matrix *A (1, 7) *and the 1st column in matrix *B (3, 5).*

![1*SPSizSebvVRh8xQf9wsoew.png](../_resources/5f90ca3b5686a5284fc675f2307a0c11.png)
Here’s another way to look at it:

![](../_resources/0a5995687bf642789a45301c0086dbaa.png)![1*xu8Eqqn9Xx60Uz7DlZy14Q.png](../_resources/0127df2fa8d9156aaadff0a48dea6a25.png)

#### Test yourself with these examples

![](../_resources/7ad60ece8e23048bf414d7d0713f6353.png)![1*-P3n80ucmqXM6e0euVqOFQ.png](../_resources/fdc7e7212def21eaf8fb78b9168f2527.png)

#### Matrix multiplication with numpy

Numpy uses the function `np.dot(A,B)` for both vector and matrix multiplication. It has some other interesting features and gotchas so I encourage you to read the documentation [here](https://docs.scipy.org/doc/numpy/reference/generated/numpy.dot.html) before use.

a = np.array([
[1, 2]
])
a.shape == (1,2)
b = np.array([
[3, 4],
[5, 6]
])
b.shape == (2,2)

# Multiply

mm = np.dot(a,b)
mm == [13, 16]
mm.shape == (1,2)

### Tutorials

[Khan Academy Linear Algebra](https://www.khanacademy.org/math/linear-algebra)

[Deep Learning Book Math Section](http://www.deeplearningbook.org/contents/part_basics.html)

[Andrew Ng’s Course Notes](https://www.coursera.org/learn/machine-learning/resources/JXWWS)

[Explanation of Linear Algebra](https://betterexplained.com/articles/linear-algebra-guide/)

[Explanation of Matrices](http://blog.stata.com/2011/03/03/understanding-matrices-intuitively-part-1/)

[Intro To Linear Algebra](http://www.holehouse.org/mlclass/03_Linear_algebra_review.html)

[Mini Reference Linear Algebra in 4 pages](https://minireference.com/static/tutorials/linear_algebra_in_4_pages.pdf)