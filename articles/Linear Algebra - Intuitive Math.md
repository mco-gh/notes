Linear Algebra - Intuitive Math

# Eigenvalues

The topic of Eigenvalues and their sibling, Eigenvectors, is something that can be quite confusing for math students. It is not immediately obvious from the calculations what they are actually for and how we can think about them intuitively.

Briefly speaking, the Eigenvalues of a square matrix translates to own values. They are the special values which encode what happens to the Eigenvectors of the matrix when it is applied as a transformation. This description probably also does not help very much either if we do not have a clear understanding of what Eigenvectors are. But we also need to know about what we are doing when we compute Eigenvalues to talk about Eigenvectors, so for now you will just have to take my word for it that they are important.

Remember how some square matrices had a determinant of zero, and this meant that they flattened space from a higher dimension to a lower dimension? If we look at any linear transformation with a nonzero determinant, you might wonder what you could do to the transformation in order to make the determinant zero.

![](../_resources/cd827a9adf1fdf21ff33019032767c78.png)

![](../_resources/539ecc09413ac6202f57b5d466bada65.png)
x1=x1=  x2=1x2=1
y1=1y1=1  y1=y1=
det(x1x2y1y2)det(x1x2y1y2) = -0.99

Recalling that the determinant of an upper or lower triangular matrix is defined as multiplication along the diagonal, you might think about what value lambda, λλ can I subtract from each element on the diagonal to make the determinant zero?

det(x1−λx2y1y2−λ)=0det(x1−λx2y1y2−λ)=0

And remember that when you are doing this, you are essentially finding some value (of which they may be more than one) to add or subtract along the diagonal which make the determinant zero.

![](../_resources/539ecc09413ac6202f57b5d466bada65.png)
λ=λ=
x1−λ=x1−λ=1.00 x2=0x2=0
y1=2y1=2  y2−λ=y2−λ=1.00
det(x1−λx2y1y2−λ)det(x1−λx2y1y2−λ) = 1.00

Remember that there does not just have to be a single Eigenvalue. Sometimes a system could have multiple Eigenvalues. This system, which shears by 2 along the x-axis but scales by two along the y-axis has λ=1λ=1

![](../_resources/539ecc09413ac6202f57b5d466bada65.png)
λ=λ=
x1−λ=x1−λ=1.00 x2=0x2=0
y1=2y1=2  y2−λ=y2−λ=2.00
det(x1−λx2y1y2−λ)det(x1−λx2y1y2−λ) = 2.00
And it also has λ=2λ=2
![](../_resources/539ecc09413ac6202f57b5d466bada65.png)
λ=λ=
x1−λ=x1−λ=1.00 x2=0x2=0
y1=2y1=2  y2−λ=y2−λ=2.00
det(x1−λx2y1y2−λ)det(x1−λx2y1y2−λ) = 2.00

In order to compute these Eigenvalues, recall the equation for the determinant, but this time subtract an unknown value λλ from the diagonal and set the determinant to zero.

det(x1−λy1x2y2−λ)=0det(x1−λy1x2y2−λ)=0(x1−λ)(y2−λ)−y1⋅x1=0(x1−λ)(y2−λ)−y1⋅x1=0(−λ+x1)(−λ+y2)−y1⋅x1=0(−λ+x1)(−λ+y2)−y1⋅x1=0λ2−(x1+y2)⋅λ+x1⋅y2−y1⋅x1=0λ2−(x1+y2)⋅λ+x1⋅y2−y1⋅x1=0

This is a polynomial known as the characteristic equation that we can solve for λλ.

If we take the example of the transformation above, we will see that:

det(1−λ202−λ)=0det(1−λ202−λ)=0(1−λ)(2−λ)−2⋅0=0(1−λ)(2−λ)−2⋅0=0(−λ+1)(−λ+2)=0(−λ+1)(−λ+2)=0λ2−3λ+2=0λ2−3λ+2=0(λ−1)(λ−2)=0(λ−1)(λ−2)=0λ=1,λ=2λ=1,λ=2

Something to take note of here is that given that that the characteristic equation is a polynomial of degree nn, wherenn is the number of columns in the square matrix, it stands to reason that there can be up to nn real-valued solutions for λλ. Sometimes there might not be any real valued solutions.

If a single value appears as a solution more than once, in the sense that one of the critical points of the polynomial lies on the x-axis, then that Eigenvalue is said to have a higher algebraic multiplicity. For instance, above, we had the matrix:

[1201][1201]
If we were to take the eigenvalues of this matrix:

det(1−λ201−λ)=0det(1−λ201−λ)=0(1−λ)2−2⋅0=0(1−λ)2−2⋅0=0(−λ+1)2=0(−λ+1)2=0λ2−2λ+1=0λ2−2λ+1=0(λ−1)2=0(λ−1)2=0λ=1λ=1

λλ would have an algebraic multiplicity of 2, since it actually appears twice if we were to expand the equation out:

(λ−1)(λ−1)=0(λ−1)(λ−1)=0λ=1,λ=1λ=1,λ=1

Eigenvalues also have some other interesting properties, which is why we say that they are useful in encoding information about what matrices are doing.

Trace: The sum of all the diagonal elements in the matrix equals the sum of all the eigenvalues. For instance, with the matrix:

[1202][1202]

we found Eigenvalues λ=1,λ=2λ=1,λ=2, which happens to equal the sum of the diagonal: 1+2=1+21+2=1+2

Determinant: The determinant of a matrix is the product of its Eigenvalues: for instance, 1×2=1×2−2×01×2=1×2−2×0

Inverse: If a matrix is invertible, then the eigenvalues of the inverse are 1λ1λ. For example, the inverse of [1202][1202] is[1−1012][1−1012]. Setting the determinant of the inverse to zero allows us to find the Eigenvalues:

det(1−λ−1012−λ)=0det(1−λ−1012−λ)=0(1−λ)(12−λ)−2⋅0=0(1−λ)(12−λ)−2⋅0=0λ2−32λ+12=0λ2−32λ+12=0(λ−1)(λ−12)=0(λ−1)(λ−12)=0λ=1,λ=12λ=1,λ=12