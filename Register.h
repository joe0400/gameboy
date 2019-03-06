#ifndef REGISTER_H
#define REGISTER_H

typedef void* Register;


enum Reg{A,F,B,C,D,E,H,L,AF,BC,DE,HL,SP,PC};

typedef enum Reg Reg;

typedef char jumpflag;

#define Z 1<<7
#define C 1<<4

Register __init__Register(void);

short get(Register r, Reg reg);


#endif
