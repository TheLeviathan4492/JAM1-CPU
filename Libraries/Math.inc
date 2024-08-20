;multiply function
;a LHS input
;b RHS input
;cd output

multiply:
  mov tx, multiply_loop

multiply_loop:
  dec b

  add c, a
  incc d

  test b
  jnz tx

  ret