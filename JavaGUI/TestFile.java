import javax.swing.*;
import java.awt.BorderLayout;
import java.awt.event.*;
import java.io.File;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.InputStream;
import java.lang.InterruptedException;
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
        addImageButton.addActionListener(new addImage());//register your interest with the button.
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); // this line makes the program quit as soon as you close the window (if you leave this out it will just sit there on the screen forever)
        frame.getContentPane().add(BorderLayout.NORTH, addImageButton); //this add the button to the frame's content pane
        frame.setSize(300,300); //gives the frame a size, in pixels
        frame.setVisible(true); // this makes the frame visible. if you forget this step, you won't see anything when you run this code
        
        removeImageButton = new JButton("Remove Image");//to make a button. You can pass the button constructor the text you want on the button
        removeImageButton.addActionListener(new removeImage());//register your interest with the button.
        frame.getContentPane().add(BorderLayout.SOUTH, removeImageButton);
    }
    class addImage implements ActionListener{
        public void actionPerformed(ActionEvent event){
            JFileChooser chooser = new JFileChooser();
            int status = chooser.showOpenDialog(null);
            if (status == JFileChooser.APPROVE_OPTION) {
                File file = chooser.getSelectedFile();
                if (file == null) {
                }
                String fileName = chooser.getSelectedFile().getAbsolutePath();
                System.out.println(fileName);
                TestFile gui = new TestFile();
                try{
                    gui.runScript(fileName,"testScript.ps1");
                }
                catch(IOException e){
                    System.err.println("IOException");
                }
                catch(InterruptedException e){
                    System.err.println("InterruptedException");
                }
            }
        }
    }
    class removeImage implements ActionListener{
        public static void main(String[] args) {
            
        }
        TestFile gui = new TestFile();
        public void actionPerformed(ActionEvent event) {
            
            JFileChooser chooser = new JFileChooser();
            int status = chooser.showOpenDialog(null);
            if (status == JFileChooser.APPROVE_OPTION) {
                File file = chooser.getSelectedFile();
                if (file == null) {
                    return;
                }
                String fileName = chooser.getSelectedFile().getAbsolutePath();
                System.out.println(fileName);
                try{
                    gui.runScript(fileName,"removeImagePiScript.ps1");
                }
                catch(IOException e){
                    System.err.println("IOException");
                }
                catch(InterruptedException e){
                    System.err.println("InterruptedException");
                }
            }
        }
    }
    public void runScript(String fileName,String scriptName)throws IOException,InterruptedException{
        String[] commands = {"powershell.exe", "Set-Variable", "-Name \"fileName\" -Value \""+fileName+"\";", "C:\\Users\\padawan\\Documents\\foyerSlideShow\\JavaGUI\\"+scriptName};
        Runtime runtime = Runtime.getRuntime();
        //Process proc = runtime.exec("powershell C:\\Users\\padawan\\Documents\\foyerSlideShow\\JavaGUI\\testScript.ps1");
        Process proc = runtime.exec(commands);
        InputStream is = proc.getInputStream();
        InputStreamReader isr = new InputStreamReader(is);
        BufferedReader reader = new BufferedReader(isr);
        String line;
        while ((line = reader.readLine()) != null){
            System.out.println(line);
        }
        reader.close();
        proc.getOutputStream().close();
    }
}