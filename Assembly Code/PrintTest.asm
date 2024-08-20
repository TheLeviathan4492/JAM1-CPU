.segment LibCode
.include display.inc

.segment Code

start:
  mov tx, string
  mov si, tx
  mov tx, Display_Clear
  call tx
  mov tx, Display_Write
  call tx
  mov tx, start
  jmp tx

string:
  db 'Hi Ethan!', 0