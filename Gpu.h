#ifndef GPU_H
#define GPU_H

#include <gtk/gtk.h>
#include "Memory.h"

const short WIDTH_X = 160;
const short HEIGHT_Y = 144;

typedef void* gpu;

gpu __init__gpu(Memory a);

gpu __del__gpu(gpu* a);

#endif
