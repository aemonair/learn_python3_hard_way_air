# learn_python_hard_way_air
About my way @ learn_python_the_hard_way

01. `print " "`
02. `#`
03. `+ - * / > < =`
04. variables
05. `print "%r %s %d" % (a ,b ,c)`
06. strings
07. `print "."*10`

    `print a+b+c`

08. `%r %r %r %r`

09. `"""`

10. `\n \t \\ \'`

11. `input = raw_input()`

12. `age = raw_input("Name ?")`

13. `from sys import argv`
    `script, first, second = argv`

14. 
    `prompt = '>'`
    `likes = raw_input(prompt)`
    `lives = raw_input(prompt)`
    

15. 
    `txt = open(filename)`
    `print txt.read()`
    

16. 
    `target = open(filename, "w")`
    `target.truncate()`
    `target.write(line1)`
    

17. 
    `in_file = open(from_file)`
    `indata = in_file.read()`

    `out_file = open(to_file, "w")`
    `out_file.write(indata)`

    `out_file.close()`
    `in_file.close()`
    

18. `def print_two(*args)`
    `    arg1, arg2 = args`
    `    print "%r %r" % (arg1, arg2)`
    

19. `def func(a, b)`
    `func(10, 20)`
    `func(10 + 1, 20 - 2)`
    `func(a + b, c - 2)`

20. Functions And Files
    
    `def print_all(f)`
    `    print f.read()`
    

    `def rewind(f)`
    `    f.seek(0)`    
    

21. Return
    `what = add(age, substract(weight, multiply(weight, divide(iq, 2))))`
