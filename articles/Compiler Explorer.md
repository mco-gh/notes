Compiler Explorer

# Compiler Explorer

- C++ source #1

1
2
3
4
// Type your code here, or load an example.
int square(int num) {
return num * num;
}
No Results

- x86-64 gcc 7.2 (Editor #1, Compiler #1) C++

|     |     |
| --- | --- |
| x86-64 gcc 7.2 |     |

1
2
3
4
5
6
7
8
square(int):
pushrbp
movrbp, rsp
movDWORDPTR [rbp-4], edi
moveax, DWORDPTR [rbp-4]
imuleax, DWORDPTR [rbp-4]
poprbp
ret
No Results
g++ (GCC-Explorer-Build) 7.2.0 - cached