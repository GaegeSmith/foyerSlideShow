import javax.swing.*;
import java.awt.event.*; //a new import statement for the package that ActionListener and ActionEvent are in
public class SimpleGUI1 implements ActionListener{
    JButton button;
    public static void main(String[] args) {
        SimpleGUI1 gui = new SimpleGUI1();
        gui.go();
    }
    public void go() {
        JFrame frame = new JFrame(); //to make a frame
        button = new JButton("click me"); //to make a button. You can pass the button constructor the text you want on the button
        button.addActionListener(this);//register your interest with the button.
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); // this line makes the program quit as soon as you close the window (if you leave this out it will just sit there on the screen forever)
        frame.getContentPane().add(button); //this add the button to the frame's content pane
        frame.setSize(300,300); //gives the frame a size, in pixels
        frame.setVisible(true); // this makes the frame visible. if you forget this step, you won't see anything when you run this code
    }
    //actionPerformed() is actual the event handling method
    public void actionPerformed(ActionEvent event){
        button.setText("I've been clicked!");
    }
}