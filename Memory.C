#include "Memory.H"

struct memory{
	char* memory;
}
typedef struct memory mem;

Memory __init__Memory(void){
	
	mem* instance = malloc(65535);
	if(instance != NULL)
		for(int i = 0;i<8*1024;i++)
			instance[i] = 0;
	return (Memory)(instance);
	
}

char get_address_WORD(Memory a, unsigned short address){
	
	return ((mem*)(a))->memory[address];
	
}

short get_address_DWORD(Memory a, unsigned short address){
	
	short* a = (short*)(((mem*)(a))->memory+address);
	
	return a[0];
}

Memory set_address_WORD(Memory a, unsigned short address, char v){
	
	((mem*)(a))->memory[address] = v;
	
	return a;
}

Memory set_address_DWORD(Memory a, unsigned short address, short v){
	
	((short*)(((mem*)(a))->memory+addres))[0] = v;
	
	return a;
}

Memory __del__memory(Memory* dat){
	
	free(*dat);
	
	return *dat = NULL;
}

char* reference_WORD(Memory dat, unsigned short address){
	
	char* d = (char*)(dat);
	
	return d+address;
}

short* reference_DWORD(Memory dat, unsigned short address){
	
	char* d = (char*)(dat);
	
	d += address;
	
	return (short*)(d);
}
