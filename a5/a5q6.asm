#Enhan Zhao 11097118 enz889 ass1 question 6

#store 10 int input into array size 10.
#prompt for i and j. If valid, exchange. If not, output current array and end. 

.data
s1: .asciiz "Please enter an integer:\n"
s2: .asciiz "Please enter integer for i:\n"
s3: .asciiz "Please enter integer for j:\n"
s4: .asciiz "The current array consists of:\n"
s5: .asciiz "Swapping ith and jth element.\n"
.align 4
intArray: .space 40
.text

main:
li $s0, 0   # $s0 = 0
li $s1, 10  # $s1 = 10

la $t0, intArray # $t0 = intArray

loop:
	bge $s0, $s1, swap
	
	li $v0, 4
	la $a0, s1
	syscall #print promt 
	
	li $v0, 5
	syscall #read input
	
	sw $v0, 0($t0)
	addi $t0, $t0, 4 #increment by size of int (4)
	addi $s0, $s0, 1 #increment counter by 1
	j loop
		
swap:
	li $v0, 4
	la $a0, s2
	syscall #print prompt for i
	li $v0, 5
	syscall #input for i
	move $t4, $v0 #store i in t4
	
	li $v0, 4
	la $a0, s3
	syscall #print prompt for j
	li $v0, 5
	syscall #input for j
	move $t5, $v0 #store j in t5
	
	bgt $t4, 10, term
	blt $t4, 1, term
	bgt $t5, 10, term
	blt $t5, 1, term
	
	addi $t4, $t4, -1 #turn into index
	addi $t5, $t5, -1
	
	li $v0, 4
	la $a0, s3
	syscall #print "swapping i j"
	#swap 
	la $t0, intArray #reset array address
	mul $t4, $t4, 4 #offset of i
	mul $t5, $t5, 4 #offset of j
	
	add $t4, $t4, $t0 #address for i
	add $t5, $t5, $t0 #address for j
	
	lw $t6, 0($t4) #t6 has value of i th element
	lw $t7, 0($t5) #t7 has value of j th element
	sw $t6, 0($t5)
	sw $t7, 0($t4)
	j swap

term:
li $v0, 4
la $a0, s4
syscall #print "the current..."
li $s0, 0   # $s0 = 0
li $s1, 10  # $s1 = 10
la $t0, intArray # $t0 = intArray
j printloop

printloop:
	bge $s0, $s1, exit
	li $v0, 1
	la $a0, s1
	lw $a0, ($t0)
	syscall
	addi $t0, $t0, 4
	addi $s0, $s0, 1
	j printloop

exit:
li $v0, 10
syscall
