import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

void setup() {
  fullScreen();
}

void runCommand(String command) throws IOException, InterruptedException {

  Process proc = Runtime.getRuntime().exec(command);

  // Read the output

  BufferedReader reader =  
      new BufferedReader(new InputStreamReader(proc.getInputStream()));

  String line = "";
  while((line = reader.readLine()) != null) {
      System.out.print(line + "\n");
  }

  proc.waitFor();   

}



void draw() {
  background(255);
}
