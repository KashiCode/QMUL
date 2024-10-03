# Extracts the required bits for 3 byte UTF-8 encoding.
li $t1, 0xF0           
li $t2, 0x80           
li $t3, 0x3F           

# Initial byte: Takes the first four bits shifts right by 12, and adds a frame.
srl $t4, $a3, 12       
andi $t4, $t4, 0x0F    
li $t1, 0xE0           
or $t4, $t4, $t1       

# Next byte: Takes the next six bits , shifts right by 6, adds a mask, and adds a frame.
srl $t5, $a3, 6        
andi $t5, $t5, 0x3F  
or $t5, $t5, $t2       

# Last byte: Take last six bits, masks them and adds a frame.
andi $t6, $a3, 0x3F  
or $t6, $t6, $t2       

# Combine the bytes into one register ($a2) and corrects endianess. 
sll $t4, $t4, 16       
sll $t5, $t5, 8        

or $a2, $t4, $t5       
or $a2, $a2, $t6   