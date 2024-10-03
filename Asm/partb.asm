    
    
    #Initialize sum $t3 to zero and moves index into $t1.
    move $t3, $zero           
    move $t1, $a1             

#Loop to check the sum the elements a[i] for which i is odd.
loop:
    bge $t1, $a2, end_loop    
    sll $t2, $t1, 2           
    add $t2, $t2, $a3         
    lw $t0, 0($t2)            

#Checks if the index is odd. 
    andi $t4, $t1, 0x1        
    beq $t4, $zero, even_index 

    add $t3, $t3, $t0         

#Increments the index by 1 and resets the loop. 
even_index:
    addi $t1, $t1, 1          
    j loop                    

#Break statement to exit the loop. 
end_loop:
    move $a2, $t3             