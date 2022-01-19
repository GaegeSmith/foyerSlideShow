# foyerSlideShow
## Java Gui swing
First you need to create a java file. Once you created it open the java file then import the following modules.
<br>
```
import javax.swing.*;
import java.awt.BorderLayout;
import java.awt.event.*;
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
Next you need to create a method that is called startProgram. Place this method after the right curly braces of the main method.<br>
```
public void startProgram(){
    
}
```
Then you need to create a frame, two button, set frame size, and setDefaultCloseOperation. setDefaultCloseOperation is setting what happen to the frame when you try to close the frame or screen.
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
}
```
You could have the JButton addImageButton and JButton removeImageButton where I place it or you could also place it in the startProgram() at the start. For now let's just keep it how I had it. Next you need to register your button listener and also set the button location. To do this type this
```
addImageButton.addActionListener(new addImage());//register your interest with the button.
removeImageButton.addActionListener(new removeImage());//register your interest with the button.
frame.getContentPane().add(BorderLayout.NORTH, addImageButton); //this add the button to the frame's content pane
frame.getContentPane().add(BorderLayout.SOUTH, removeImageButton);
```
If you run this right now it will popup an error that said error: cannot find symbol. What this is saying is that there is no class name removeImage and also addImage.
To fix the error you need to create class for both of the removeImage and also addImage. To make a class you could ether create an new java file or create the class in side of this java file. To make a class type class nameOfClass{}. But for the addImage class and removeImage class you need to implements ActionListener. Place the classes right after the last bracket of the startProgram() method. Then you need to make a actionPerformed method in both of the classes the removeImage and addImage.
```
class addImage implements ActionListener{
    public void actionPerformed(ActionEvent event){
        
    }
}
```
```
class removeImage implements ActionListener{
    public void actionPerformed(ActionEvent event){
        
    }
}
```
If you run this is what will be created.
<br>
![mainSrceen](https://user-images.githubusercontent.com/71509807/146052722-d078532c-7a41-4243-b7d9-ec9ced8bc1fe.png)
<br>
First lets start with implementing a JFileChooser in the addImage class. To start you need to type this inside the actionPerformed method
```
JFileChooser chooser = new JFileChooser();
int status = chooser.showOpenDialog(null);
```
If you run this and click on the Add Image button the file explorer will popup. then you need to type a if statement that check if status is == to JFileChooser.APPROVE_OPTION. The if statement will look like this
```
if (status == JFileChooser.APPROVE_OPTION) {

}
```
Then in side the if statement type in the following
```
String fileName = chooser.getSelectedFile().getAbsolutePath();
System.out.println(fileName);
TestFile gui = new TestFile();
```
Before you continue you need to make a method called runScript.
```
public void runScript(String fileName,String scriptName)throws IOException,InterruptedException{

}
```
The throws will throw out any IOException and InterruptedException errors. This will alow you to bypass these errors. Ceate this method after the removeImage class. Now lets go back the the addIImage class. You then need to type in a try and catch statement to catch the IOException and InterruptedException errors. This how the try and catch statement will look like
```
try{
    gui.runScript(fileName,"addImageToPiScript.ps1");
}
catch(IOException e){
    System.err.println("IOException");
}
catch(InterruptedException e){
    System.err.println("InterruptedException");
}
```
Now copy the code inside the actionPerformed method inside the addImage class and place it inside the actionPerformed method in the removeImage class. There is some things you need to change. The first change is to change the getAbsolutePath() on the chooser to getName(). The next change is to change the second parameter on the runSript() to "removeImageFromPiScript.ps1"
## powerScript(ps1) code
create a ps1 file called addImageToPiScript and a ps1 file called removeImageFromPiScript. In the addImageToPiScript.ps1 file type this
```
Write-host "fileName = $fileName"
Write-output "before scp"
scp.exe $fileName "pi@192.168.1.100:Documents/FoyerScreens/"
Write-output "finish scp"
```
Then in the removeImageFromPiScript.ps1 file type this
```
ssh.exe "pi@192.168.1.100" "cd Documents/FoyerScreens/; rm $fileName"
```
## Setup for allowing to not have to type in a password when ssh into the pie
Go to powershell and cd into ~/.ssh<br>
If you do not have the foldee then type in mkdir .ssh<br>
Then type in ssh-keygen -t rsa<br>
Then ssh into the pie. Then type in mkdir -p .ssh<br>
Then type in ls -a<br>
ls -a will ensure that its there with this command. Open another powershell window and cd into ~/.ssh<br>
Then type in scp .\id_rsa.pub pi:pbuttword@192.168.1.100:.ssh<br>
Then type in mv id_rsa.pub authorized_keys<br>
Link to website: http://guidetojava.com/sample_doc/mydoc_no_password_prompts_scp.html
