#all of the assmebly instructions in order of opcode
instructions = [
  'nop',                             #00
  
  'mov_a_const',                     #01
  'mov_b_const',                     #02
  'mov_c_const',                     #03
  'mov_d_const',                     #04
  'mov_tl_const',                    #05
  'mov_th_const',                    #06
  
  'mov_a_b',                         #07
  'mov_a_c',                         #08
  'mov_a_d',                         #09
  'mov_b_a',                         #0A
  'mov_b_c',                         #0B
  'mov_b_d',                         #0C
  'mov_c_a',                         #0D
  'mov_c_b',                         #0E
  'mov_c_d',                         #0F
  'mov_d_a',                         #10
  'mov_d_b',                         #11
  'mov_d_c',                         #12

  'mov_tl_a',                        #13
  'mov_tl_b',                        #14
  'mov_tl_c',                        #15
  'mov_tl_d',                        #16
  'mov_th_a',                        #17
  'mov_th_b',                        #18
  'mov_th_c',                        #19
  'mov_th_d',                        #1A
  'mov_a_tl',                        #1B
  'mov_b_tl',                        #1C
  'mov_c_tl',                        #1D
  'mov_d_tl',                        #1E
  'mov_a_th',                        #1F
  'mov_b_th',                        #20
  'mov_c_th',                        #21
  'mov_d_th',                        #22

  'mov_ra_tx',                       #23
  'mov_tx_ra',                       #24
  'mov_sp_tx',                       #25
  'mov_tx_sp',                       #26
  'mov_si_tx',                       #27
  'mov_tx_si',                       #28
  'mov_di_tx',                       #29
  'mov_tx_di',                       #2A
  'mov_di_si',                       #2B
  'mov_si_di',                       #2C

  '', '', '',                        #2D-2F

  'dec_ra',                          #30
  'dec_sp',                          #31
  'dec_si',                          #32
  'dec_di',                          #33
  'inc_sp',                          #34
  'inc_si',                          #35
  'inc_di',                          #36

  'out_lcd_a',                       #37

  '', '', '', '', '', '', '', '',    #38-3F

  'mov_a_[si]',                      #40
  'mov_b_[si]',                      #41
  'mov_c_[si]',                      #42
  'mov_d_[si]',                      #43
  'mov_a_[di]',                      #44
  'mov_b_[di]',                      #45
  'mov_c_[di]',                      #46
  'mov_d_[di]',                      #47
  'mov_a_[tx]',                      #48
  'mov_b_[tx]',                      #49
  'mov_c_[tx]',                      #4A
  'mov_d_[tx]',                      #4B
  'mov_[si]_a',                      #4C
  'mov_[si]_b',                      #4D
  'mov_[si]_c',                      #4E
  'mov_[si]_d',                      #4F
  'mov_[di]_a',                      #50
  'mov_[di]_b',                      #51
  'mov_[di]_c',                      #52
  'mov_[di]_d',                      #53
  'mov_[tx]_a',                      #54
  'mov_[tx]_b',                      #55
  'mov_[tx]_c',                      #56
  'mov_[tx]_d',                      #57

  'call_tx',                         #58
  'ret',                             #59

  '', '', '', '', '',                #5A-5E

  'prebranch',                       #5F
  'jmp_tx',                          #60
  'jo_tx',                           #61
  'jno_tx',                          #62
  'js_tx',                           #63
  'jns_tx',                          #64
  'jz_tx',                           #65
  'jnz_tx',                          #66
  'jc_tx',                           #67
  'jnc_tx',                          #68
  'jbe_tx',                          #69
  'ja_tx',                           #6A
  'jl_tx',                           #6B
  'jge_tx',                          #6C
  'jle_tx',                          #6D
  'jg_tx',                           #6E
  'jlc_tx',                          #6F
  'jnlc_tx',                         #70
  'jmp_di',                          #71

  'push_a',                          #72
  'push_b',                          #73
  'push_c',                          #74
  'push_d',                          #75
  'push_tl',                         #76
  'push_th',                         #77
  'pop_a',                           #78
  'pop_b',                           #79
  'pop_c',                           #7A
  'pop_d',                           #7B
  'pop_tl',                          #7C
  'pop_th',                          #7D

  '',                                #7E

  'clc',                             #7F

  'shl_a',                           #80
  'shl_b',                           #81
  'shl_c',                           #82
  'shl_d',                           #83
  'shr_a',                           #84
  'shr_b',                           #85
  'shr_c',                           #86
  'shr_d',                           #87

  'add_a_b',                         #88
  'add_a_c',                         #89
  'add_a_d',                         #8A
  'add_b_a',                         #8B
  'add_b_c',                         #8C
  'add_b_d',                         #8D
  'add_c_a',                         #8E
  'add_c_b',                         #8F
  'add_c_d',                         #90
  'add_d_a',                         #91
  'add_d_b',                         #92
  'add_d_c',                         #93

  'addc_a_b',                        #94
  'addc_a_c',                        #95
  'addc_a_d',                        #96
  'addc_b_a',                        #97
  'addc_b_c',                        #98
  'addc_b_d',                        #99
  'addc_c_a',                        #9A
  'addc_c_b',                        #9B
  'addc_c_d',                        #9C
  'addc_d_a',                        #9D
  'addc_d_b',                        #9E
  'addc_d_c',                        #9F

  'sub_a_b',                         #A0
  'sub_a_c',                         #A1
  'sub_a_d',                         #A2
  'sub_b_a',                         #A3
  'sub_b_c',                         #A4
  'sub_b_d',                         #A5
  'sub_c_a',                         #A6
  'sub_c_b',                         #A7
  'sub_c_d',                         #A8
  'sub_d_a',                         #A9
  'sub_d_b',                         #AA
  'sub_d_c',                         #AB

  'subb_a_b',                        #AC
  'subb_a_c',                        #AD
  'subb_a_d',                        #AE
  'subb_b_a',                        #AF
  'subb_b_c',                        #B0
  'subb_b_d',                        #B1
  'subb_c_a',                        #B2
  'subb_c_b',                        #B3
  'subb_c_d',                        #B4
  'subb_d_a',                        #B5
  'subb_d_b',                        #B6
  'subb_d_c',                        #B7

  'inc_a',                           #B8
  'inc_b',                           #B9
  'inc_c',                           #BA
  'inc_d',                           #BB

  'incc_a',                          #BC
  'incc_b',                          #BD
  'incc_c',                          #BE
  'incc_d',                          #BF

  'dec_a',                           #C0
  'dec_b',                           #C1
  'dec_c',                           #C2
  'dec_d',                           #C3

  'and_a_b',                         #C4
  'and_a_c',                         #C5
  'and_a_d',                         #C6
  'and_b_a',                         #C7
  'and_b_c',                         #C8
  'and_b_d',                         #C9
  'and_c_a',                         #CA
  'and_c_b',                         #CB
  'and_c_d',                         #CC
  'and_d_a',                         #CD
  'and_d_b',                         #CE
  'and_d_c',                         #CF

  'or_a_b',                          #D0
  'or_a_c',                          #D1
  'or_a_d',                          #D2
  'or_b_a',                          #D3
  'or_b_c',                          #D4
  'or_b_d',                          #D5
  'or_c_a',                          #D6
  'or_c_b',                          #D7
  'or_c_d',                          #D8
  'or_d_a',                          #D9
  'or_d_b',                          #DA
  'or_d_c',                          #DB

  'xor_a_a',                         #DC
  'xor_a_b',                         #DD
  'xor_a_c',                         #DE
  'xor_a_d',                         #DF
  'xor_b_a',                         #E0
  'xor_b_b',                         #E1
  'xor_b_c',                         #E2
  'xor_b_d',                         #E3
  'xor_c_a',                         #E4
  'xor_c_b',                         #E5
  'xor_c_c',                         #E6
  'xor_c_d',                         #E7
  'xor_d_a',                         #E8
  'xor_d_b',                         #E9
  'xor_d_c',                         #EA
  'xor_d_d',                         #EB

  'not_a',                           #EC
  'not_b',                           #ED
  'not_c',                           #EE
  'not_d',                           #EF

  'cmp_a_b',                         #F0
  'cmp_a_c',                         #F1
  'cmp_a_d',                         #F2
  'cmp_b_a',                         #F3
  'cmp_b_c',                         #F4
  'cmp_b_d',                         #F5
  'cmp_c_a',                         #F6
  'cmp_c_b',                         #F7
  'cmp_c_d',                         #F8
  'cmp_d_a',                         #F9
  'cmp_d_b',                         #FA
  'cmp_d_c',                         #FB

  'test_a',                          #FC
  'test_b',                          #FD
  'test_c',                          #FE
  'test_d'                           #FF
]


#How many current flags
flag_count = 6


#Control Lines
Bus_Request = 1<<31

PCRA0_Addr_Assert = 1<<28
PCRA1_Addr_Assert = 2<<28
SP_Addr_Assert = 3<<28
SI_Addr_Assert = 4<<28
DI_Addr_Assert = 5<<28
TX_Addr_Assert = 6<<28

PCRA_Flip = 1<<26

SP_Inc = 1<<24
SI_Inc = 2<<24
DI_Inc = 3<<24

A_Load = 1<<20
B_Load = 2<<20
C_Load = 3<<20
D_Load = 4<<20
Const_Data_Load = 5<<20
TL_Load = 6<<20
TH_Load = 7<<20
LCD_Load = 14<<20
MemBridge_Load = 15<<20

A_Assert = 1<<16
B_Assert = 2<<16
C_Assert = 3<<16
D_Assert = 4<<16
Const_Assert = 5<<16
TL_Assert = 6<<16
TH_Assert = 7<<16
ALU_Assert = 8<<16
MemBridge_Assert = 15<<16

No_Fetch = 1<<15

PCRA0_Xfer_Assert = 1<<12
PCRA1_Xfer_Assert = 2<<12
SP_Xfer_Assert = 3<<12
SI_Xfer_Assert = 4<<12
DI_Xfer_Assert = 5<<12
TX_Xfer_Assert = 6<<12

PCRA0_Xfer_Load = 1<<8
PCRA1_Xfer_Load = 2<<8
SP_Xfer_Load = 3<<8
SI_Xfer_Load = 4<<8
DI_Xfer_Load = 5<<8
TX_Xfer_Load = 6<<8

Const_Mem_Load = 8<<8
PCRA0_Dec = 9<<8
PCRA1_Dec = 10<<8
SP_Dec = 11<<8
SI_Dec = 12<<8
DI_Dec = 13<<8

ALU_SHL = 1<<4
ALU_SHR = 2<<4
ALU_ADD = 3<<4
ALU_ADDC = 4<<4
ALU_INC = 5<<4
ALU_INCC = 6<<4
ALU_SUB = 7<<4
ALU_SUBB = 8<<4
ALU_DEC = 9<<4
ALU_AND = 10<<4
ALU_OR = 11<<4
ALU_XOR = 12<<4
ALU_NOT = 13<<4
ALU_CLC = 14<<4

A_LHS_Assert = 0<<2
B_LHS_Assert = 1<<2
C_LHS_Assert = 2<<2
D_LHS_Assert = 3<<2

A_RHS_Assert = 0
B_RHS_Assert = 1
C_RHS_Assert = 2
D_RHS_Assert = 3


#Generates control lines for each instruction
def return_control_lines(opcode, flags):

  PCRA_Flip_Flag = (flags>>5)&1
  Logic_Carry_Flag = (flags>>4)&1
  Carry_Flag = (flags>>3)&1
  Zero_Flag = (flags>>2)&1
  Sign_Flag = (flags>>1)&1
  Overflow_Flag = flags&1
  if PCRA_Flip_Flag:
    out = PCRA1_Addr_Assert | PCRA_Flip
    addr_mask = PCRA1_Addr_Assert
    call_mask = PCRA1_Addr_Assert - PCRA0_Addr_Assert + PCRA_Flip

  else:
    out = PCRA0_Addr_Assert
    addr_mask = PCRA0_Addr_Assert
    call_mask = PCRA0_Addr_Assert - PCRA1_Addr_Assert - PCRA_Flip
   

  match opcode:

    case 'nop':             return out
  
    case 'mov_a_const':     return out | No_Fetch | Const_Mem_Load | Const_Assert | A_Load
    case 'mov_b_const':     return out | No_Fetch | Const_Mem_Load | Const_Assert | B_Load
    case 'mov_c_const':     return out | No_Fetch | Const_Mem_Load | Const_Assert | C_Load
    case 'mov_d_const':     return out | No_Fetch | Const_Mem_Load | Const_Assert | D_Load
    case 'mov_tl_const':    return out | No_Fetch | Const_Mem_Load | Const_Assert | TL_Load
    case 'mov_th_const':    return out | No_Fetch | Const_Mem_Load | Const_Assert | TH_Load

    case 'mov_a_b':         return out | A_Load | B_Assert
    case 'mov_a_c':         return out | A_Load | C_Assert
    case 'mov_a_d':         return out | A_Load | D_Assert
    case 'mov_b_a':         return out | B_Load | A_Assert
    case 'mov_b_c':         return out | B_Load | C_Assert
    case 'mov_b_d':         return out | B_Load | D_Assert
    case 'mov_c_a':         return out | C_Load | A_Assert
    case 'mov_c_b':         return out | C_Load | B_Assert
    case 'mov_c_d':         return out | C_Load | D_Assert
    case 'mov_d_a':         return out | D_Load | A_Assert
    case 'mov_d_b':         return out | D_Load | B_Assert
    case 'mov_d_c':         return out | D_Load | C_Assert

    case 'mov_tl_a':        return out | TL_Load | A_Assert
    case 'mov_tl_b':        return out | TL_Load | B_Assert
    case 'mov_tl_c':        return out | TL_Load | C_Assert
    case 'mov_tl_d':        return out | TL_Load | D_Assert
    case 'mov_th_a':        return out | TH_Load | A_Assert
    case 'mov_th_b':        return out | TH_Load | B_Assert
    case 'mov_th_c':        return out | TH_Load | C_Assert
    case 'mov_th_d':        return out | TH_Load | D_Assert
    case 'mov_a_tl':        return out | A_Load  | TL_Assert
    case 'mov_b_tl':        return out | B_Load  | TL_Assert
    case 'mov_c_tl':        return out | C_Load  | TL_Assert
    case 'mov_d_tl':        return out | D_Load  | TL_Assert
    case 'mov_a_th':        return out | A_Load  | TH_Assert
    case 'mov_b_th':        return out | B_Load  | TH_Assert
    case 'mov_c_th':        return out | C_Load  | TH_Assert
    case 'mov_d_th':        return out | D_Load  | TH_Assert

    case 'mov_ra_tx':       return out | (PCRA0_Xfer_Load if PCRA_Flip_Flag else PCRA1_Xfer_Load) | TX_Xfer_Assert
    case 'mov_tx_ra':       return out | TX_Xfer_Load | (PCRA0_Xfer_Assert if PCRA_Flip_Flag else PCRA1_Xfer_Assert)
    case 'mov_sp_tx':       return out | SP_Xfer_Load | TX_Xfer_Assert
    case 'mov_tx_sp':       return out | TX_Xfer_Load | SP_Xfer_Assert
    case 'mov_si_tx':       return out | SI_Xfer_Load | TX_Xfer_Assert
    case 'mov_tx_si':       return out | TX_Xfer_Load | SI_Xfer_Assert
    case 'mov_di_tx':       return out | DI_Xfer_Load | TX_Xfer_Assert
    case 'mov_tx_di':       return out | TX_Xfer_Load | DI_Xfer_Assert
    case 'mov_di_si':       return out | DI_Xfer_Load | SI_Xfer_Assert
    case 'mov_si_di':       return out | SI_Xfer_Load | DI_Xfer_Assert

    case 'dec ra':          return out | (PCRA0_Dec if PCRA_Flip_Flag else PCRA1_Dec)
    case 'dec_sp':          return out | SP_Dec
    case 'dec_si':          return out | SI_Dec
    case 'dec_di':          return out | DI_Dec
    case 'inc_sp':          return out | SP_Inc
    case 'inc_si':          return out | SI_Inc
    case 'inc_di':          return out | DI_Inc

    case 'out_lcd_a':       return out | LCD_Load | A_Assert
  
    case 'mov_a_[si]':      return (out - addr_mask) | Bus_Request | SI_Addr_Assert | A_Load | MemBridge_Assert
    case 'mov_b_[si]':      return (out - addr_mask) | Bus_Request | SI_Addr_Assert | B_Load | MemBridge_Assert
    case 'mov_c_[si]':      return (out - addr_mask) | Bus_Request | SI_Addr_Assert | C_Load | MemBridge_Assert
    case 'mov_d_[si]':      return (out - addr_mask) | Bus_Request | SI_Addr_Assert | D_Load | MemBridge_Assert
    case 'mov_a_[di]':      return (out - addr_mask) | Bus_Request | DI_Addr_Assert | A_Load | MemBridge_Assert
    case 'mov_b_[di]':      return (out - addr_mask) | Bus_Request | DI_Addr_Assert | B_Load | MemBridge_Assert
    case 'mov_c_[di]':      return (out - addr_mask) | Bus_Request | DI_Addr_Assert | C_Load | MemBridge_Assert
    case 'mov_d_[di]':      return (out - addr_mask) | Bus_Request | DI_Addr_Assert | D_Load | MemBridge_Assert
    case 'mov_a_[tx]':      return (out - addr_mask) | Bus_Request | TX_Addr_Assert | A_Load | MemBridge_Assert
    case 'mov_b_[tx]':      return (out - addr_mask) | Bus_Request | TX_Addr_Assert | B_Load | MemBridge_Assert
    case 'mov_c_[tx]':      return (out - addr_mask) | Bus_Request | TX_Addr_Assert | C_Load | MemBridge_Assert
    case 'mov_d_[tx]':      return (out - addr_mask) | Bus_Request | TX_Addr_Assert | D_Load | MemBridge_Assert
    case 'mov_[si]_a':      return (out - addr_mask) | Bus_Request | SI_Addr_Assert | MemBridge_Load | A_Assert
    case 'mov_[si]_b':      return (out - addr_mask) | Bus_Request | SI_Addr_Assert | MemBridge_Load | B_Assert
    case 'mov_[si]_c':      return (out - addr_mask) | Bus_Request | SI_Addr_Assert | MemBridge_Load | C_Assert
    case 'mov_[si]_d':      return (out - addr_mask) | Bus_Request | SI_Addr_Assert | MemBridge_Load | D_Assert
    case 'mov_[di]_a':      return (out - addr_mask) | Bus_Request | DI_Addr_Assert | MemBridge_Load | A_Assert
    case 'mov_[di]_b':      return (out - addr_mask) | Bus_Request | DI_Addr_Assert | MemBridge_Load | B_Assert
    case 'mov_[di]_c':      return (out - addr_mask) | Bus_Request | DI_Addr_Assert | MemBridge_Load | C_Assert
    case 'mov_[di]_d':      return (out - addr_mask) | Bus_Request | DI_Addr_Assert | MemBridge_Load | D_Assert
    case 'mov_[tx]_a':      return (out - addr_mask) | Bus_Request | TX_Addr_Assert | MemBridge_Load | A_Assert
    case 'mov_[tx]_b':      return (out - addr_mask) | Bus_Request | TX_Addr_Assert | MemBridge_Load | B_Assert
    case 'mov_[tx]_c':      return (out - addr_mask) | Bus_Request | TX_Addr_Assert | MemBridge_Load | C_Assert
    case 'mov_[tx]_d':      return (out - addr_mask) | Bus_Request | TX_Addr_Assert | MemBridge_Load | D_Assert

    case 'call_tx':         return (out - call_mask) | (PCRA0_Xfer_Load if PCRA_Flip_Flag else PCRA1_Xfer_Load) | TX_Xfer_Assert
    case 'ret':             return (out - call_mask)

    case 'prebranch':       return out | Bus_Request 
    case 'jmp_tx':          return out | (PCRA1_Xfer_Load   if PCRA_Flip_Flag else PCRA0_Xfer_Load) | TX_Xfer_Assert
    case 'jo_tx':           return out | (((PCRA1_Xfer_Load if PCRA_Flip_Flag else PCRA0_Xfer_Load) | TX_Xfer_Assert) if Overflow_Flag else 0)
    case 'jno_tx':          return out | (((PCRA1_Xfer_Load if PCRA_Flip_Flag else PCRA0_Xfer_Load) | TX_Xfer_Assert) if not Overflow_Flag else 0)
    case 'js_tx':           return out | (((PCRA1_Xfer_Load if PCRA_Flip_Flag else PCRA0_Xfer_Load) | TX_Xfer_Assert) if Sign_Flag else 0)
    case 'jns_tx':          return out | (((PCRA1_Xfer_Load if PCRA_Flip_Flag else PCRA0_Xfer_Load) | TX_Xfer_Assert) if not Sign_Flag else 0)
    case 'jz_tx':           return out | (((PCRA1_Xfer_Load if PCRA_Flip_Flag else PCRA0_Xfer_Load) | TX_Xfer_Assert) if Zero_Flag else 0)
    case 'jnz_tx':          return out | (((PCRA1_Xfer_Load if PCRA_Flip_Flag else PCRA0_Xfer_Load) | TX_Xfer_Assert) if not Zero_Flag else 0)
    case 'jc_tx':           return out | (((PCRA1_Xfer_Load if PCRA_Flip_Flag else PCRA0_Xfer_Load) | TX_Xfer_Assert) if Carry_Flag else 0)
    case 'jnc_tx':          return out | (((PCRA1_Xfer_Load if PCRA_Flip_Flag else PCRA0_Xfer_Load) | TX_Xfer_Assert) if not Carry_Flag else 0)
    case 'jbe_tx':          return out | (((PCRA1_Xfer_Load if PCRA_Flip_Flag else PCRA0_Xfer_Load) | TX_Xfer_Assert) if (Zero_Flag | Carry_Flag) else 0)
    case 'ja_tx':           return out | (((PCRA1_Xfer_Load if PCRA_Flip_Flag else PCRA0_Xfer_Load) | TX_Xfer_Assert) if ((not Carry_Flag) & (not Zero_Flag)) else 0)
    case 'jl_tx':           return out | (((PCRA1_Xfer_Load if PCRA_Flip_Flag else PCRA0_Xfer_Load) | TX_Xfer_Assert) if (Overflow_Flag == 0) != (Sign_Flag == 0) else 0)
    case 'jge_tx':          return out | (((PCRA1_Xfer_Load if PCRA_Flip_Flag else PCRA0_Xfer_Load) | TX_Xfer_Assert) if (Overflow_Flag == 0) == (Sign_Flag == 0) else 0)
    case 'jle_tx':          return out | (((PCRA1_Xfer_Load if PCRA_Flip_Flag else PCRA0_Xfer_Load) | TX_Xfer_Assert) if (Zero_Flag | (Overflow_Flag == 0) != (Sign_Flag == 0)) else 0)
    case 'jg_tx':           return out | (((PCRA1_Xfer_Load if PCRA_Flip_Flag else PCRA0_Xfer_Load) | TX_Xfer_Assert) if ((not Zero_Flag) & (not Sign_Flag)) else 0)
    case 'jlc_tx':          return out | (((PCRA1_Xfer_Load if PCRA_Flip_Flag else PCRA0_Xfer_Load) | TX_Xfer_Assert) if Logic_Carry_Flag else 0)
    case 'jnlc_tx':         return out | (((PCRA1_Xfer_Load if PCRA_Flip_Flag else PCRA0_Xfer_Load) | TX_Xfer_Assert) if not Logic_Carry_Flag else 0)
    case 'jmp_di':          return out | (PCRA1_Xfer_Load   if PCRA_Flip_Flag else PCRA0_Xfer_Load) | DI_Xfer_Assert

    case 'push_a':          return (out - addr_mask) | Bus_Request | SP_Addr_Assert | SP_Dec | MemBridge_Load |  A_Assert
    case 'push_b':          return (out - addr_mask) | Bus_Request | SP_Addr_Assert | SP_Dec | MemBridge_Load |  B_Assert
    case 'push_c':          return (out - addr_mask) | Bus_Request | SP_Addr_Assert | SP_Dec | MemBridge_Load |  C_Assert
    case 'push_d':          return (out - addr_mask) | Bus_Request | SP_Addr_Assert | SP_Dec | MemBridge_Load |  D_Assert
    case 'push_tl':         return (out - addr_mask) | Bus_Request | SP_Addr_Assert | SP_Dec | MemBridge_Load | TL_Assert
    case 'push_th':         return (out - addr_mask) | Bus_Request | SP_Addr_Assert | SP_Dec | MemBridge_Load | TH_Assert
    case 'pop_a':           return (out - addr_mask) | Bus_Request | SP_Addr_Assert | SP_Inc | A_Load  | MemBridge_Assert
    case 'pop_b':           return (out - addr_mask) | Bus_Request | SP_Addr_Assert | SP_Inc | B_Load  | MemBridge_Assert
    case 'pop_c':           return (out - addr_mask) | Bus_Request | SP_Addr_Assert | SP_Inc | C_Load  | MemBridge_Assert
    case 'pop_d':           return (out - addr_mask) | Bus_Request | SP_Addr_Assert | SP_Inc | D_Load  | MemBridge_Assert
    case 'pop_tl':          return (out - addr_mask) | Bus_Request | SP_Addr_Assert | SP_Inc | TL_Load | MemBridge_Assert
    case 'pop_th':          return (out - addr_mask) | Bus_Request | SP_Addr_Assert | SP_Inc | TH_Load | MemBridge_Assert

    case 'clc':             return out | ALU_CLC
  
    case 'shl_a':           return out | ALU_SHL | A_LHS_Assert | A_Load | ALU_Assert
    case 'shl_b':           return out | ALU_SHL | B_LHS_Assert | B_Load | ALU_Assert
    case 'shl_c':           return out | ALU_SHL | C_LHS_Assert | C_Load | ALU_Assert
    case 'shl_d':           return out | ALU_SHL | D_LHS_Assert | D_Load | ALU_Assert
    case 'shr_a':           return out | ALU_SHR | A_LHS_Assert | A_Load | ALU_Assert
    case 'shr_b':           return out | ALU_SHR | B_LHS_Assert | B_Load | ALU_Assert
    case 'shr_c':           return out | ALU_SHR | C_LHS_Assert | C_Load | ALU_Assert
    case 'shr_d':           return out | ALU_SHR | D_LHS_Assert | D_Load | ALU_Assert

    case 'add_a_b':         return out | ALU_ADD | A_LHS_Assert | B_RHS_Assert | A_Load | ALU_Assert
    case 'add_a_c':         return out | ALU_ADD | A_LHS_Assert | C_RHS_Assert | A_Load | ALU_Assert
    case 'add_a_d':         return out | ALU_ADD | A_LHS_Assert | D_RHS_Assert | A_Load | ALU_Assert
    case 'add_b_a':         return out | ALU_ADD | B_LHS_Assert | A_RHS_Assert | B_Load | ALU_Assert
    case 'add_b_c':         return out | ALU_ADD | B_LHS_Assert | C_RHS_Assert | B_Load | ALU_Assert
    case 'add_b_d':         return out | ALU_ADD | B_LHS_Assert | D_RHS_Assert | B_Load | ALU_Assert
    case 'add_c_a':         return out | ALU_ADD | C_LHS_Assert | A_RHS_Assert | C_Load | ALU_Assert
    case 'add_c_b':         return out | ALU_ADD | C_LHS_Assert | B_RHS_Assert | C_Load | ALU_Assert
    case 'add_c_d':         return out | ALU_ADD | C_LHS_Assert | D_RHS_Assert | C_Load | ALU_Assert
    case 'add_d_a':         return out | ALU_ADD | D_LHS_Assert | A_RHS_Assert | D_Load | ALU_Assert
    case 'add_d_b':         return out | ALU_ADD | D_LHS_Assert | B_RHS_Assert | D_Load | ALU_Assert
    case 'add_d_c':         return out | ALU_ADD | D_LHS_Assert | C_RHS_Assert | D_Load | ALU_Assert

    case 'addc_a_b':        return out | ALU_ADDC | A_LHS_Assert | B_RHS_Assert | A_Load | ALU_Assert
    case 'addc_a_c':        return out | ALU_ADDC | A_LHS_Assert | C_RHS_Assert | A_Load | ALU_Assert
    case 'addc_a_d':        return out | ALU_ADDC | A_LHS_Assert | D_RHS_Assert | A_Load | ALU_Assert
    case 'addc_b_a':        return out | ALU_ADDC | B_LHS_Assert | A_RHS_Assert | B_Load | ALU_Assert
    case 'addc_b_c':        return out | ALU_ADDC | B_LHS_Assert | C_RHS_Assert | B_Load | ALU_Assert
    case 'addc_b_d':        return out | ALU_ADDC | B_LHS_Assert | D_RHS_Assert | B_Load | ALU_Assert
    case 'addc_c_a':        return out | ALU_ADDC | C_LHS_Assert | A_RHS_Assert | C_Load | ALU_Assert
    case 'addc_c_b':        return out | ALU_ADDC | C_LHS_Assert | B_RHS_Assert | C_Load | ALU_Assert
    case 'addc_c_d':        return out | ALU_ADDC | C_LHS_Assert | D_RHS_Assert | C_Load | ALU_Assert
    case 'addc_d_a':        return out | ALU_ADDC | D_LHS_Assert | A_RHS_Assert | D_Load | ALU_Assert
    case 'addc_d_b':        return out | ALU_ADDC | D_LHS_Assert | B_RHS_Assert | D_Load | ALU_Assert
    case 'addc_d_c':        return out | ALU_ADDC | D_LHS_Assert | C_RHS_Assert | D_Load | ALU_Assert
    
    case 'sub_a_b':         return out | ALU_SUB | A_LHS_Assert | B_RHS_Assert | A_Load | ALU_Assert
    case 'sub_a_c':         return out | ALU_SUB | A_LHS_Assert | C_RHS_Assert | A_Load | ALU_Assert
    case 'sub_a_d':         return out | ALU_SUB | A_LHS_Assert | D_RHS_Assert | A_Load | ALU_Assert
    case 'sub_b_a':         return out | ALU_SUB | B_LHS_Assert | A_RHS_Assert | B_Load | ALU_Assert
    case 'sub_b_c':         return out | ALU_SUB | B_LHS_Assert | C_RHS_Assert | B_Load | ALU_Assert
    case 'sub_b_d':         return out | ALU_SUB | B_LHS_Assert | D_RHS_Assert | B_Load | ALU_Assert
    case 'sub_c_a':         return out | ALU_SUB | C_LHS_Assert | A_RHS_Assert | C_Load | ALU_Assert
    case 'sub_c_b':         return out | ALU_SUB | C_LHS_Assert | B_RHS_Assert | C_Load | ALU_Assert
    case 'sub_c_d':         return out | ALU_SUB | C_LHS_Assert | D_RHS_Assert | C_Load | ALU_Assert
    case 'sub_d_a':         return out | ALU_SUB | D_LHS_Assert | A_RHS_Assert | D_Load | ALU_Assert
    case 'sub_d_b':         return out | ALU_SUB | D_LHS_Assert | B_RHS_Assert | D_Load | ALU_Assert
    case 'sub_d_c':         return out | ALU_SUB | D_LHS_Assert | C_RHS_Assert | D_Load | ALU_Assert

    case 'subb_a_b':        return out | ALU_SUBB | A_LHS_Assert | B_RHS_Assert | A_Load | ALU_Assert
    case 'subb_a_c':        return out | ALU_SUBB | A_LHS_Assert | C_RHS_Assert | A_Load | ALU_Assert
    case 'subb_a_d':        return out | ALU_SUBB | A_LHS_Assert | D_RHS_Assert | A_Load | ALU_Assert
    case 'subb_b_a':        return out | ALU_SUBB | B_LHS_Assert | A_RHS_Assert | B_Load | ALU_Assert
    case 'subb_b_c':        return out | ALU_SUBB | B_LHS_Assert | C_RHS_Assert | B_Load | ALU_Assert
    case 'subb_b_d':        return out | ALU_SUBB | B_LHS_Assert | D_RHS_Assert | B_Load | ALU_Assert
    case 'subb_c_a':        return out | ALU_SUBB | C_LHS_Assert | A_RHS_Assert | C_Load | ALU_Assert
    case 'subb_c_b':        return out | ALU_SUBB | C_LHS_Assert | B_RHS_Assert | C_Load | ALU_Assert
    case 'subb_c_d':        return out | ALU_SUBB | C_LHS_Assert | D_RHS_Assert | C_Load | ALU_Assert
    case 'subb_d_a':        return out | ALU_SUBB | D_LHS_Assert | A_RHS_Assert | D_Load | ALU_Assert
    case 'subb_d_b':        return out | ALU_SUBB | D_LHS_Assert | B_RHS_Assert | D_Load | ALU_Assert
    case 'subb_d_c':        return out | ALU_SUBB | D_LHS_Assert | C_RHS_Assert | D_Load | ALU_Assert

    case 'inc_a':           return out | ALU_INC | A_LHS_Assert | A_Load | ALU_Assert
    case 'inc_b':           return out | ALU_INC | B_LHS_Assert | B_Load | ALU_Assert
    case 'inc_c':           return out | ALU_INC | C_LHS_Assert | C_Load | ALU_Assert
    case 'inc_d':           return out | ALU_INC | D_LHS_Assert | D_Load | ALU_Assert
      
    case 'incc_a':          return out | ALU_INCC | A_LHS_Assert | A_Load | ALU_Assert
    case 'incc_b':          return out | ALU_INCC | B_LHS_Assert | B_Load | ALU_Assert
    case 'incc_c':          return out | ALU_INCC | C_LHS_Assert | C_Load | ALU_Assert
    case 'incc_d':          return out | ALU_INCC | D_LHS_Assert | D_Load | ALU_Assert

    case 'dec_a':           return out | ALU_DEC | A_LHS_Assert | A_Load | ALU_Assert
    case 'dec_b':           return out | ALU_DEC | B_LHS_Assert | B_Load | ALU_Assert
    case 'dec_c':           return out | ALU_DEC | C_LHS_Assert | C_Load | ALU_Assert
    case 'dec_d':           return out | ALU_DEC | D_LHS_Assert | D_Load | ALU_Assert

    case 'and_a_b':         return out | ALU_AND | A_LHS_Assert | B_RHS_Assert | A_Load | ALU_Assert
    case 'and_a_c':         return out | ALU_AND | A_LHS_Assert | C_RHS_Assert | A_Load | ALU_Assert
    case 'and_a_d':         return out | ALU_AND | A_LHS_Assert | D_RHS_Assert | A_Load | ALU_Assert
    case 'and_b_a':         return out | ALU_AND | B_LHS_Assert | A_RHS_Assert | B_Load | ALU_Assert
    case 'and_b_c':         return out | ALU_AND | B_LHS_Assert | C_RHS_Assert | B_Load | ALU_Assert
    case 'and_b_d':         return out | ALU_AND | B_LHS_Assert | D_RHS_Assert | B_Load | ALU_Assert
    case 'and_c_a':         return out | ALU_AND | C_LHS_Assert | A_RHS_Assert | C_Load | ALU_Assert
    case 'and_c_b':         return out | ALU_AND | C_LHS_Assert | B_RHS_Assert | C_Load | ALU_Assert
    case 'and_c_d':         return out | ALU_AND | C_LHS_Assert | D_RHS_Assert | C_Load | ALU_Assert
    case 'and_d_a':         return out | ALU_AND | D_LHS_Assert | A_RHS_Assert | D_Load | ALU_Assert
    case 'and_d_b':         return out | ALU_AND | D_LHS_Assert | B_RHS_Assert | D_Load | ALU_Assert
    case 'and_d_c':         return out | ALU_AND | D_LHS_Assert | C_RHS_Assert | D_Load | ALU_Assert

    case 'or_a_b':          return out | ALU_OR | A_LHS_Assert | B_RHS_Assert | A_Load | ALU_Assert
    case 'or_a_c':          return out | ALU_OR | A_LHS_Assert | C_RHS_Assert | A_Load | ALU_Assert
    case 'or_a_d':          return out | ALU_OR | A_LHS_Assert | D_RHS_Assert | A_Load | ALU_Assert
    case 'or_b_a':          return out | ALU_OR | B_LHS_Assert | A_RHS_Assert | B_Load | ALU_Assert
    case 'or_b_c':          return out | ALU_OR | B_LHS_Assert | C_RHS_Assert | B_Load | ALU_Assert
    case 'or_b_d':          return out | ALU_OR | B_LHS_Assert | D_RHS_Assert | B_Load | ALU_Assert
    case 'or_c_a':          return out | ALU_OR | C_LHS_Assert | A_RHS_Assert | C_Load | ALU_Assert
    case 'or_c_b':          return out | ALU_OR | C_LHS_Assert | B_RHS_Assert | C_Load | ALU_Assert
    case 'or_c_d':          return out | ALU_OR | C_LHS_Assert | D_RHS_Assert | C_Load | ALU_Assert
    case 'or_d_a':          return out | ALU_OR | D_LHS_Assert | A_RHS_Assert | D_Load | ALU_Assert
    case 'or_d_b':          return out | ALU_OR | D_LHS_Assert | B_RHS_Assert | D_Load | ALU_Assert
    case 'or_d_c':          return out | ALU_OR | D_LHS_Assert | C_RHS_Assert | D_Load | ALU_Assert

    case 'xor_a_a':         return out | ALU_XOR | A_LHS_Assert | A_RHS_Assert | A_Load | ALU_Assert
    case 'xor_a_b':         return out | ALU_XOR | A_LHS_Assert | B_RHS_Assert | A_Load | ALU_Assert
    case 'xor_a_c':         return out | ALU_XOR | A_LHS_Assert | C_RHS_Assert | A_Load | ALU_Assert
    case 'xor_a_d':         return out | ALU_XOR | A_LHS_Assert | D_RHS_Assert | A_Load | ALU_Assert
    case 'xor_b_a':         return out | ALU_XOR | B_LHS_Assert | A_RHS_Assert | B_Load | ALU_Assert
    case 'xor_b_b':         return out | ALU_XOR | B_LHS_Assert | B_RHS_Assert | B_Load | ALU_Assert
    case 'xor_b_c':         return out | ALU_XOR | B_LHS_Assert | C_RHS_Assert | B_Load | ALU_Assert
    case 'xor_b_d':         return out | ALU_XOR | B_LHS_Assert | D_RHS_Assert | B_Load | ALU_Assert
    case 'xor_c_a':         return out | ALU_XOR | C_LHS_Assert | A_RHS_Assert | C_Load | ALU_Assert
    case 'xor_c_b':         return out | ALU_XOR | C_LHS_Assert | B_RHS_Assert | C_Load | ALU_Assert
    case 'xor_c_c':         return out | ALU_XOR | C_LHS_Assert | C_RHS_Assert | C_Load | ALU_Assert
    case 'xor_c_d':         return out | ALU_XOR | C_LHS_Assert | D_RHS_Assert | C_Load | ALU_Assert
    case 'xor_d_a':         return out | ALU_XOR | D_LHS_Assert | A_RHS_Assert | D_Load | ALU_Assert
    case 'xor_d_b':         return out | ALU_XOR | D_LHS_Assert | B_RHS_Assert | D_Load | ALU_Assert
    case 'xor_d_c':         return out | ALU_XOR | D_LHS_Assert | C_RHS_Assert | D_Load | ALU_Assert
    case 'xor_d_d':         return out | ALU_XOR | D_LHS_Assert | D_RHS_Assert | D_Load | ALU_Assert

    case 'not_a':           return out | ALU_NOT | A_RHS_Assert | A_Load | ALU_Assert
    case 'not_b':           return out | ALU_NOT | B_RHS_Assert | B_Load | ALU_Assert
    case 'not_c':           return out | ALU_NOT | C_RHS_Assert | C_Load | ALU_Assert
    case 'not_d':           return out | ALU_NOT | D_RHS_Assert | D_Load | ALU_Assert

    case 'cmp_a_b':         return out | ALU_SUB | A_LHS_Assert | B_RHS_Assert
    case 'cmp_a_c':         return out | ALU_SUB | A_LHS_Assert | C_RHS_Assert
    case 'cmp_a_d':         return out | ALU_SUB | A_LHS_Assert | D_RHS_Assert
    case 'cmp_b_a':         return out | ALU_SUB | B_LHS_Assert | A_RHS_Assert
    case 'cmp_b_c':         return out | ALU_SUB | B_LHS_Assert | C_RHS_Assert
    case 'cmp_b_d':         return out | ALU_SUB | B_LHS_Assert | D_RHS_Assert
    case 'cmp_c_a':         return out | ALU_SUB | C_LHS_Assert | A_RHS_Assert
    case 'cmp_c_b':         return out | ALU_SUB | C_LHS_Assert | B_RHS_Assert
    case 'cmp_c_d':         return out | ALU_SUB | C_LHS_Assert | D_RHS_Assert
    case 'cmp_d_a':         return out | ALU_SUB | D_LHS_Assert | A_RHS_Assert
    case 'cmp_d_b':         return out | ALU_SUB | D_LHS_Assert | B_RHS_Assert
    case 'cmp_d_c':         return out | ALU_SUB | D_LHS_Assert | C_RHS_Assert

    case 'test_a':          return out | ALU_AND | A_LHS_Assert | A_RHS_Assert
    case 'test_b':          return out | ALU_AND | B_LHS_Assert | B_RHS_Assert
    case 'test_c':          return out | ALU_AND | C_LHS_Assert | C_RHS_Assert
    case 'test_d':          return out | ALU_AND | D_LHS_Assert | D_RHS_Assert
    
    case _:                 return out



#Fills up the list with the control rom data
def fill_data_list(list, stage, instructions):
  for index, item in enumerate(list):
    flags = index>>8
    opcode = instructions[index&255]
    control_word = return_control_lines(opcode, flags)
    control_data = (control_word>>((stage-1)*8))&255
    hex_control_data = hex(control_data)[2:].upper().zfill(2)
    list[index] = hex_control_data
  return list


  #Writes control rom data list to the output file
def write_rom_file(file, data):
  line_counter = 0
  program_file = open(file, "w")

  program_file.write('v3.0 hex words addressed' + '\n')
  program_file.write('0000: ')
  for n in range(len(data)):

    if (((n + 1) % 16) == 0):
      line_counter += 1
      hex_line_counter = hex(line_counter)[2:]
      hex_line_counter = hex_line_counter.zfill(3) + '0: '

      program_file.write(data[n] + '\n')
      if hex_line_counter != '4000: ':
        program_file.write(hex_line_counter)

    else:
      program_file.write(data[n] + ' ')

  program_file.close()


#Creates and initializes the rom data lists
Control_ROM_1A = [0]*(2**(flag_count+8))
Control_ROM_1B = [0]*(2**(flag_count+8))
Control_ROM_2A = [0]*(2**(flag_count+8))
Control_ROM_2B = [0]*(2**(flag_count+8))

#Fills roms data lists with rom data
Control_ROM_1A = fill_data_list(Control_ROM_1A, 1, instructions)
Control_ROM_1B = fill_data_list(Control_ROM_1B, 2, instructions)
Control_ROM_2A = fill_data_list(Control_ROM_2A, 3, instructions)
Control_ROM_2B = fill_data_list(Control_ROM_2B, 4, instructions)

#Writes each rom data list to it's respective data list for it's stage
write_rom_file(r'C:\JAM-1 Files\Control ROM Data\Control ROM 1A.txt', Control_ROM_1A)
write_rom_file(r'C:\JAM-1 Files\Control ROM Data\Control ROM 1B.txt', Control_ROM_1B)
write_rom_file(r'C:\JAM-1 Files\Control ROM Data\Control ROM 2A.txt', Control_ROM_2A)
write_rom_file(r'C:\JAM-1 Files\Control ROM Data\Control ROM 2B.txt', Control_ROM_2B)