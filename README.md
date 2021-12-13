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
Then you need to create a frame and two button.
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
        removeImageButton = new JButton("Remove Image");//to make a button. You can pass the button constructor the text you want on the button
    }
```
you could have the JButton addImageButton and JButton removeImageButton where I place it but you could also place it in the startProgram() at the start. for now let just keep it how I had it.<br>
Next you need to register your button listener. to do the type this
```

```
