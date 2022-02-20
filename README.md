# Collatz Conjecture
The Collatz Conjecture is an unsolved problem in mathematics (number theoretical analysis) that is also commonly known by the *'3n+1 problem'*. I found the inspiration to work on visualising this problem from the following video https://www.youtube.com/watch?v=094y1Z2wpJg by Derek of _Veritasium_ and thereby led me to devise this code.
The basis of the problem lies within the following statement :
```Choose any number. If it is even in nature, then divide it by 2. Otherwise multiply it by 3 and add 1. Keep on doing this```
The conjecture states that the sequence reaches a ``4->2->1`` loop irrespective of the initial number chosen.
Here the ``matplotlib`` module is used for graphing the Collatz Sequence.
Thereafter the sequencing begins with the number the user inputs.
The code also provides the *Stopping Number* i.e. the number of steps after which the sequence reaches the ``4->2->1`` loop
Then the graphing is done using the module.
![image](https://user-images.githubusercontent.com/75131827/154831007-caff6d2d-4a8d-4f62-a83c-2008e9393ec6.png)
Hope you find it fun !!
