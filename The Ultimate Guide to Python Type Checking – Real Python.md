The Ultimate Guide to Python Type Checking – Real Python

# headlines.py 2  3 def  headline(text:  str,  align:  bool  =  True)  ->  str: 4   if  align: 5   return  f"{text.title()}\n{'-' * len(text)}" 6   else: 7   return  f" {text.title()} ".center(50,  "o") 8  9 print(headline("python type checking"))10 print(headline("use mypy",  align="center"))