#include "Gpu.h"

struct GPU{
	char* ScrollY;
	char* ScrollX;
	char* WindowX;
	char* WindowY;
	char* enabled;
	char* scanlin;
};

gpu __init__gpu(Memory a){
	
	struct GPU* ret = malloc(sizeof(struct GPU));
	
	
	ret->ScrollY = reference_WORD(a,65346);
	ret->ScrollX = reference_WORD(a,65347);
	
	ret->WindowY = reference_WORD(a,65354);
	ret->WindowX = reference_WORD(a,65355);

	ret->scanlin = reference_WORD(a,65348);
	ret->enabled = reference_WORD(a,65344);
	
}
