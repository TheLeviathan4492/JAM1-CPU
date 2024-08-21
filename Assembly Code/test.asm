.include Display.inc
.segment Code

start:
  mov tx, Display_Clear
  call tx
  xor a, a
  mov tx, loop
  mov di, tx

loop:
  mov cd, Display_Hex_Table
  add cd, a
  inc a
  push a
  mov tx, cd
  mov a, [tx]
  out lcd, a
  pop a
  jmp di