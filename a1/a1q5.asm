#Enhan Zhao enz889 11097118 ass1 q5

#input int N, input N ints. Output Difference between max and min.
#use t and s for anything for now
# $v0 instruction for syscall
#$a0 is value holder for syscall 


.data
s1: .asciiz "Please enter an integer that represent the number of ints that will be entered.\n"
s2: .asciiz "The difference between max and min is\n"
s3: .asciiz "Enter an integer.\n"
.text
main:
#read int N
li $s0, 1 #loop counter
la $a0, s1
li $v0, 4  #print string 
syscall   

li $v0, 5  #read N from user 
syscall 
move $s1, $v0

la $a0, s3
li $v0, 4  #read N from user 
syscall 


li $v0, 5 #read first int
syscall #first int

move $s2, $v0 #hold max
move $s3, $v0 #holds min 

#looooop N-1 times
loop:
	bge $s0, $s1, exitLoop  # if the counter is greater than or equal to the max, exit the loop
	la $a0, s3
	li $v0, 4  #print string 
        syscall   
        
	li $v0, 5 #read int
	syscall
	blt $v0, $s3, newmin
	bgt $v0, $s2, newmax
	addi $s0, $s0, 1        # increment the loop counter
	b loop 
	
	newmin:
	move $s3, $v0
	addi $s0, $s0, 1        # increment the loop counter
	b loop 
	
	newmax:
	move $s2, $v0
	addi $s0, $s0, 1        # increment the loop counter
	b loop 
	
	exitLoop:
	
	sub $s4, $s2, $s3
	la $a0, s2
	li $v0, 4
	syscall 
	
	move $a0, $s4
	li $v0, 1
	syscall
	
	li $v0, 10
	syscall







  
