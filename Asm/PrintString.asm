
.data
CDATA: .ascii "Hello, World!"
BDATA: .byte 42, '*'
CDATA2: .asciiz "Another String"

.text
.globl main
main:
    la $a0, CDATA       # Load address of CDATA into $a0
    li $v0, 4           # Load syscall print_string into $v0
    syscall             # System call to print the string in $a0

    la $a0, CDATA2      # Load address of CDATA2 into $a0
    syscall             # System call to print the string in $a0

    lw $a0, 4($sp)      # Load word from address at $sp + 4 into $a0
    syscall             # System call to print the string in $a0

    jr $ra              # Jump to the address in register $ra
    nop                 # No operation
