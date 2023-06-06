# class-201
Tkinter


\

Tkinter provides us with a variety of common GUI elements which we can use to build our interface. Some of the few common widgets available are: \

● Button: When clicked, an operation can be triggered
● Label: to display something on-screen
● Entry: to get a single line user input
● List box: provides a list of options
● Label frame: Used for results to display in a frame.\

And there are many more available as per application design




to Develop a GUI application using tkinter we need steps and These steps remain the same for all the GUI applications. \

Import Tkinter module
\
Create your application window

5. Add widgets to the window


7. Create the widget


9. Place it on screen


11. Call main loop

\

We need to write a logic part for our application like what will happen when we click a button. All the user interactivity through buttons, etc. has a defined logic.

\

This third step can be done in two parts: ● Create Widget ● Place Widget


Create Widget: There are a number of widgets which you can put in your tkinter application. In our GUI-BMI calculator we need labels, entry box, button and label Frame.


Place widget: Set the geometric configuration of the widgets on the main window. We will use the place () method to organize the widgets by placing them on the main screen

To add a label, we need to create one variable which is equal to Label () widget. Now set your label inside the parent window, that’s why we are using the window inside the label and all other widget attributes inside the label. Now set different attributes for labels for your parent window. \

We are using label attributes like text which we want to show on your window, foreground color (fg), background color(bg), font, font size, border(bd).

\

Here app_label is variable = Label is widget () which we are creating for parent window, i.e. window inside Label () widget and then attributes foreground color (fg), background color(bg), font , font size, border(bd). Now it's time to place your widget on the screen that will use the place() method. Here x, y are coordinates according to your parent window

To show output, we need to create label frame, A LabelFrame () is different from a normal Label (), LabelFrame's primary purpose is to act as a spacer or container for output layouts. This LabelFrame () widget has the features of a frame, plus the ability to display a label result. So first we will create a result frame container. In the Label Frame () we are using pack () to pack the text on the window Now create Label () to display label inside your result frame label frame

Fourth step is to call the main loop () mainloop () that is used when your application is ready to run. mainloop () is an infinite loop used to run the application, wait for an event to occur and process the event as long as the window is not closed.
