tests = [ {'description': 'PINA: 0x0A => PORTC: 0x38',
    'steps': [ {'inputs': [('PINA',0x0A)], 'iterations': 2 } ],
    'expected': [('PORTC',0x38)],
    },

   {'description': 'PINA: 0x00 => PORTC: 0x3F',
    'steps': [ {'inputs': [('PINA',0x00)], 'iterations': 5 } ],
    'expected': [('PORTC',0x3F)],
    },

   {'description': 'PINA: 0x0E => PORTC: 0x60',
    'steps': [ {'inputs': [('PINA',0x0E)], 'iterations': 5 } ],
    'expected': [('PORTC',0x60)],
    },


   {'description': 'PINA: 0x06 => PORTC: 0x3C',
    'steps': [ {'inputs': [('PINA',0x06)], 'iterations': 5 } ],
    'expected': [('PORTC',0x3C)],
    },
   
   {'description': 'PINA: 0x8C => PORTC: 0x70',
    'steps': [ {'inputs': [('PINA',0x8C)], 'iterations': 5 } ],
    'expected': [('PORTC',0x70)],
    },
   
   ]

#watch = ['PORTC']
#watch = ['count'k]
