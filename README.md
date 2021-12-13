# foyerSlideShow
## Java Gui swing
First you need to create a java file. Once you created it open the java file then import the following modules.
<br>
```
import javax.swing.*;
import java.awt.BorderLayout;
import java.awt.event.*;
import java.io.File;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.InputStream;
import java.lang.InterruptedException;
```
After you import all of the modules above type in public class insertFileNameHere {}<br>Then type inside the {} public static void main(String[] args){}<br>This is how it should look like.<br>
```
public class TestFile {
    public static void main(String[] args){
        
    }
}
```
Next you need to create a method that is called startProgram. Place this methid after the right curly braces of the main method.<br>
```
public void startProgram(){
    
}
```
Then you need to create a frame, two button, set frame size, and setDefaultCloseOperation.
```
public class TestFile {
    JButton addImageButton;
    JButton removeImageButton;
    public static void main(String[] args){
        TestFile gui = new TestFile();
        gui.startProgram();
    }
    public void startProgram(){
        JFrame frame = new JFrame();
        addImageButton = new JButton("Add Image");//to make a button. You can pass the button constructor the text you want on the button
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); // this line makes the program quit as soon as you close the window (if you leave this out it will just sit there on the screen forever)
        frame.setSize(300,300); //gives the frame a size, in pixels
        frame.setVisible(true); // this makes the frame visible. if you forget this step, you won't see anything when you run this code
        removeImageButton = new JButton("Remove Image");//to make a button. You can pass the button constructor the text you want on the button
    }
```
you could have the JButton addImageButton and JButton removeImageButton where I place it but you could also place it in the startProgram() at the start. for now let just keep it how I had it. Next you need to register your button listener and also set the button location. to do the type this
```
addImageButton.addActionListener(new addImage());//register your interest with the button.
removeImageButton.addActionListener(new removeImage());//register your interest with the button.
frame.getContentPane().add(BorderLayout.NORTH, addImageButton); //this add the button to the frame's content pane
frame.getContentPane().add(BorderLayout.SOUTH, removeImageButton);
```

