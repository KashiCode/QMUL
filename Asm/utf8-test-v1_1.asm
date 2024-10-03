.data

# Some test values 
# Task 0: code point to 3-byte UTF-8: INPUT 0x8a9e OUTPUT 0xe8aa9e


INPUT: .word 0x8a9e 
TARGET: .word 0xe8aa9e

SUCCESS_MSG: .asciiz "Test successful\n"
FAIL_MSG: .asciiz "Test failed\n"
.text
main:
la $a3 INPUT
lw $a3 0($a3)

# your code here 

# your code ends
la $a3 TARGET
lw $a3 0($a3)

beq $a2 $a3 SUCCESS
la $a0, FAIL_MSG
li $v0 4
syscall
b END

SUCCESS:
la $a0, SUCCESS_MSG
li $v0 4
syscall

END:
li $v0 10
syscall # exit
# End of program