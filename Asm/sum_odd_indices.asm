
.data
A: .word 0:100   # Placeholder for array of words (size 100, initialized to 0)

.text
.globl main
main:
    # Assume $a1 contains the start index and $a2 contains the end index (one past the last element)
    # $a3 contains the base address of the array A
    # Initialize sum register $a2 to 0
    move $a2, $zero
    
    # Loop setup
    move $t1, $a1      # Move start index into $t1
    sll $t1, $t1, 2    # Multiply index by 4 to get the correct byte offset (since it's a word array)
    add $t1, $t1, $a3  # Add base address of array to start index to get actual memory address
    move $t2, $a2      # Move end index into $t2
    sll $t2, $t2, 2    # Multiply index by 4 to get the byte offset for the end index

loop:
    # Check if the current index $t1 is less than the end index $t2
    bge $t1, $t2, end_loop  # If $t1 >= $t2, exit loop
    
    # Load the current element into $t0
    lw $t0, 0($t1)
    
    # Check if the index is odd, we do this by checking the last bit of the address
    andi $t3, $t1, 0x3      # Mask all but the last 2 bits to check word alignment
    beq $t3, $zero, even_index  # If the result is 0, the index is even (since we are checking the byte offset)
    
    # If index is odd, add the element to the sum
    add $a2, $a2, $t0
    
even_index:
    # Increment the index by the size of a word (4 bytes)
    addi $t1, $t1, 4
    
    # Jump back to the start of the loop
    j loop

end_loop:
    # Exit the program (in a real MIPS environment you would call a system service to exit)
    # Here we simply halt the program
    nop  # No operation (placeholder for exit syscall)

