#ifndef MEMORY_H
#define MEMORY_H

#include <stdlib.h>

typedef void* Memory;

Memory __init__memory(void);

Memory __del__memory(Memory* dat);

char  get_address_WORD (Memory a, unsigned short address);
short get_address_DWORD(Memory a, unsigned short address);

Memory set_address_WORD (Memory a, unsigned short address, char  v);
Memory set_address_DWORD(Memory a, unsigned short address, short v);

char* reference_WORD(Memory a, unsigned short address);
short* reference_DWROD(Memory a, unsigned short address);

#endif
