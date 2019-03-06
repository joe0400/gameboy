#include "Register.h"
#include "Memory.h"
#include <stdlib.h>
#include <time.h>

struct cpu{
	Register 	reg;
	Memory		mem;
}
typedef struct cpu cpu;

const struct timespec CYCLES;

void* doVoid(void){
	return;
}

Cpu __init__Cpu(){
	struct timespec cpucycles;
	cpucycles.seconds = 0;
	cpucycles.nanoseconds = 238;
	CYCLES = cpucycles;
	cpu* init = malloc(sizeof(cpu));
	if(init == NULL)
		return NULL;
	cpu->reg = __init__Register();
	cpu->mem = __init__Memory();
	
	if(init->reg == NULL){
		free(cpu->mem);
	}
	if(init->mem == NULL){
		free(cpu->reg);
	}
	if(init->mem == NULL || init->reg == NULL){
		free(init);
		return NULL;
	}
	return (Cpu)(init);
}

void nop(Cpu cp){
	for(int i = 0;i<4;i++)
		usleep(&CYCLES,NULL);
}

void load_16(Cpu cp, reg r){
	
	cpu* c = ((cpu*)(cp));
	
