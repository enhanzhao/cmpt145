#Enhan Zhao 11097118 enz889 ass1 question 7

#reads a string, convert each letter to upper case. output the new string. 

.data
stringArray: .space 20
s1: .asciiz "Please enter a string.\n"
.text 
main:
	li $v0, 4
	la $a0, s1
	syscall #prompt for string input
	li $v0, 8 
	la $a0, stringArray
	li $a1, 20
	syscall
	
#check each character, if lower, convert to upper. Else do nothing. Use s registry
	
loop:
    lb $s1, stringArray($s0)
    beq $s1, '\n', print #null byte means exit, go to print
    beq $s1, ' ', ignore #ignore space characters
    blt $s1, 'a', bigger #if bigger, subtract 32 
    bge $s1, 'a', smaller #if smaller, add 32
        

bigger: 
    addi $s1, $s1, 32
    sb $s1, stringArray($s0)
    addi $s0, $s0, 1
    j loop
    
smaller:
    subi $s1, $s1, 32
    sb $s1, stringArray($s0)
    addi $s0, $s0, 1
    j loop
   
ignore:
    addi $s0, $s0, 1
    j loop
	
print:
	li $v0, 4
	la $a0, stringArray
	syscall
	
exit:
li $v0 10
syscall
