.segment DisplayDataRO

Display_Hex_Table:
  db '0123456789ABCDEF'


.segment LibCode

; Parameters: None
; Overwrites: a
; Returns:    None
Display_Clear:
  mov a, 128
  out lcd, a
  ret

; Parameters: None
; Overwrites: a
; Returns:    None
Display_NewLine:
  mov a, 10
  out lcd, a
  ret


; Parameters: si = address of string
; Overwrites: a, tl, th
; Returns:    None 
Display_Write:
  mov tx, di
  push tl
  push th
  nop

  mov tx, Display_Write_loop
  mov di, tx
  mov tx, Display_Write_end

Display_Write_loop:
  
  mov a, [si]
  inc si
  test a
  jz tx

  out lcd, a
  jmp di

Display_Write_end:
  pop th
  pop tl
  mov di, tx

  ret



; Parameters: a = value to output
; Overwrites: tl, th
; Returns:    None 
Display_Write_4Hex:
  push a
  push b
  push c
  push d

  mov cd, Display_Hex_Table
  mov b, 15
  and a, b
  xor b, b
  add a, c
  addc b, d
  mov tl, a
  mov th, b

  pop d
  pop c
  pop b

  mov a, [tx]
  out lcd, a

  pop a
  ret


; Parameters: a = value to output
; Overwrites: tl, th
; Returns:    None 
Display_Write_8Hex:
  push a
  push b
  push c 
  push d 

  push a

  nop
  mov cd, Display_Hex_Table
  mov b, 15

  shr a
  shr a
  shr a
  shr a
  and a, b
  add cd, a
  mov tx, cd
  mov a, [tx]
  out lcd, a 

  pop a

  and a, b
  add cd, a
  mov tx, cd
  mov a, [tx]
  out lcd, a

  pop d
  pop c
  pop b
  pop a 
  ret


; Parameters: ab = value to output
; Overwrites: tl, th
; Returns:    None 
Display_Write_16Hex:
  mov tx, ra
  push tx
  push a
  nop
  mov tx, Display_Write_8Hex
  mov a, b 
  call tx
  pop a
  nop
  mov tx, Display_Write_8Hex
  call tx
  pop tx
  mov ra, tx
  ret