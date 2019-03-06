#include <X11/Xlib.h>
#include <stdio.h>
#include <stdlib.h>
int main(int argc, char* argv[]){
	
	Display *disp = XOpenDisplay(NULL);
	
	int b = BlackPixel(disp,DefaultScreen(disp));
	int w = WhitePixel(disp,DefaultScreen(disp));
	
	Window win = XCreateSimpleWindow(disp,DefaultRootWindow(disp),0,0,200,100,0,b,b);
	
	XSelectInput(disp,win,StructureNotifyMask);
	XMapWindow(disp,win);
	GC context = XCreateGC(disp,win,0,NULL);

	XSetForeground(disp,context,w);

	for(;;){
		XEvent e;
		XNextEvent(disp,&e);
		if(e.type != MapNotify)
			break;
		XFlush(disp);
	}
	return 0;
}
