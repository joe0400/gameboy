#include <gtk/gtk.h>
#include <stdio.h>

void callback(GtkWidget* widget, gpointer data){
	
	printf("GOT HERE\n");

}

void greeting(GtkWidget *widget, gpointer data){
	
	g_print("thi is the thing\n");
	
}

void destroy(GtkWidget* widget, gpointer data){
	
	gtk_main_quit();
}

int main(int argc, char** argv){
	
	GtkWidget *window;
	GtkWidget *button;
	
	gtk_init(&argc, &argv);
	
	window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
	button = gtk_button_new_with_label("click here");
	g_signal_connect(window, "destroy", G_CALLBACK(destroy),NULL);
	g_signal_connect(GTK_OBJECT(button),"clicked",G_CALLBACK(callback),"button");
	
	gtk_container_add(GTK_CONTAINER(window),button);

	gtk_widget_show_all(window);
	gtk_main();
	
	return 0;
}
	
