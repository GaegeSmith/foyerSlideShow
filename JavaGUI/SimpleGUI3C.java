import javax.swing.*;
import java.awt.*;
import java.awt.event.*; //a new import statement for the package that ActionListener and ActionEvent are in
public class SimpleGUI3C implements ActionListener{
    JFrame frame;
    public static void main(String[] args) {
        SimpleGUI3C gui = new SimpleGUI3C();
        gui.go();
    }
    class MyDrawPanel extends JPanel {
        public void paintComponent(Graphics g){
            Graphics2D g2d = (Graphics2D) g;

            int red = (int) (Math.random() * 256);
            int green = (int) (Math.random() * 256);
            int blue = (int) (Math.random() * 256);
            Color starColor = new Color(red, green, blue);

            red = (int) (Math.random() * 256);
            green = (int) (Math.random() * 256);
            blue = (int) (Math.random() * 256);
            Color endColor = new Color(red, green, blue);

            GradientPaint gradient = new GradientPaint(70,70,starColor,150,150,endColor);
            g2d.setPaint(gradient);
            g2d.fillOval(70,70,100,100);
        }
    }
    public void go() {
        frame = new JFrame(); //to make a frame
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); // this line makes the program quit as soon as you close the window (if you leave this out it will just sit there on the screen forever)
        JButton button = new JButton("change colors"); //to make a button. You can pass the button constructor the text you want on the button
        button.addActionListener(this);//register your interest with the button.
        MyDrawPanel drawPanel = new MyDrawPanel();
        frame.getContentPane().add(BorderLayout.SOUTH, button);
        frame.getContentPane().add(BorderLayout.CENTER, drawPanel);
        frame.setSize(300,300); //gives the frame a size, in pixels
        frame.setVisible(true); // this makes the frame visible. if you forget this step, you won't see anything when you run this code
    }
    //actionPerformed() is actual the event handling method
    public void actionPerformed(ActionEvent event){
        frame.repaint();
    }
}