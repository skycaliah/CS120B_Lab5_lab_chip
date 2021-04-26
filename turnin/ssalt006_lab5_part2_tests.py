# Test sequence from waitA0: A0, !A0, A1 => PORTB: 0xF0
tests = [ {'description': 'PINA: 0x0D, 0x0D, 0x0F => PORTC: 6, state:SM2_ReadyButton ',
    'steps': [{'inputs': [('PINA', 0x0D)], 'iterations': 2},
        {'inputs': [('PINA', 0x0D)], 'iterations': 2},
        {'inputs': [('PINA', 0x0F)], 'iterations': 2}],
    'expected': [('PORTC',0x06)],
    },
    

    {'description': 'PINA: 0x0E, 0x0F, 0x0E => PORTC: 8, state:SM2_wait_plus ',
    'steps': [{'inputs': [('PINA', 0x0E)], 'iterations': 5},
        {'inputs': [('PINA', 0x0F)], 'iterations': 5},
        {'inputs': [('PINA', 0x0E)], 'iterations': 5}],
    'expected': [('PORTC',0x08)],
    }
  ,
 {'description': 'PINA: 0x0F, 0x0C, 0x0C => PORTC: 0, state:SM2_Reset ',
    'steps': [{'inputs': [('PINA', 0x0F)], 'iterations': 2},
        {'inputs': [('PINA', 0x0C)], 'iterations': 2},
        {'inputs': [('PINA', 0x0C)], 'iterations': 2}],
    'expected': [('PORTC',0x00)],
    },




    ]
watch = ['SM2_State']
