.data

MYARRAY: .word 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
INPUT_A1_START: .word 3
INPUT_A2_END: .word 8

Prompt: .asciiz "\n$a2 contains: "
Return: .asciiz "\n"

.text
main:
la $a3 MYARRAY
la $a1 INPUT_A1_START
lw $a1 0($a1)
la $a2 INPUT_A2_END
lw $a2 0($a2)

# Paste your code here

# Your code ends

# Printout
la $a0,Prompt
li $v0 4
syscall

li $v0 1
move $a0 $a2
syscall # print $a2

la $a0, Return
li $v0 4
syscall 

li $v0 10
syscall # exit
# End of program
