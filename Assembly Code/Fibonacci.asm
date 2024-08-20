.include Display.inc

.segment DataRO
fibonacci_Title:
  db 'Fibonacci Sequence', 0

fibonacci_Prefix:
  db 'Value '

.segment Code

start:
  mov tx, Display_Clear
  call tx    

  mov tx, fibonacci_Title
  mov si, tx
  mov tx, Display_Write
  call tx
  
  mov tx, Display_NewLine
  call tx
  call tx

; f(x) = f(x-1) + f(x-2)
  mov a, 1  ;ab = f(x)
  xor b, b 
  xor c, c  ;cd = f(x-1)
  xor d, d 

loop:

  push a
  
  nop
  mov tx, fibonacci_Prefix
  mov si, tx
  mov tx, Display_Write
  call tx

  mov tx, di
  mov a, tl
  mov tx, Display_Write_8Hex
  call tx
  inc di

  mov a, 61
  out lcd, a

  pop a

  nop
  mov tx, Display_Write_16Hex
  call tx

  push a

  nop
  mov tx, Display_NewLine
  call tx

  pop a

  ; AB + CD
  mov tx, ab
  add ab, cd
  mov cd, tx

  mov tx, loop
  jnc tx

  mov tx, halt

halt:
  jmp tx