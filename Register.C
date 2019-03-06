#include "register.h"

struct reg{
	short af, bc, de, hl;
	short fp, sp;
	char* a, f, b, c, d, e, h, l;
};
typedef struct reg reg;

Register __init__Register(void){

	reg* init = malloc(sizeof(reg));
	if(reg != NULL){
		for(int i = 0;i<6;i++)
			((short*)(init))[i] = 0;
		reg->a = ((char*)(&(reg->af)))+1;
		reg->f = ((char*)(&(reg->af)));
		reg->b = ((char*)(&(reg->bc)))+1;
		reg->c = ((char*)(&(reg->bc)));
		reg->d = ((char*)(&(reg->de)))+1;
		reg->e = ((char*)(&(reg->de)));
		reg->h = ((char*)(&(reg->hl)))+1;
		reg->l = ((char*)(&(reg->hl)));
	}
	return (Register)(init);

}

