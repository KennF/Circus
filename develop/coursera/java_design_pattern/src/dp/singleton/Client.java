package dp.singleton;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Client {
	public static void main(String[] args){
		AmericanPresident president = AmericanPresident.getPresident();
		System.out.println(president.name);
		
		//
		try {
			String[] command ={"/sbin/ping", "programcreek.com"};		
			Process p = Runtime.getRuntime().exec(command);
//			Process p = Runtime.getRuntime().exec("C:/windows/system32/ping.exe programcreek.com");
			//get process input stream and put it to buffered reader
			BufferedReader input = new BufferedReader(new InputStreamReader(p.getInputStream()));
			 
			String line;
			while ((line = input.readLine()) != null) {
				System.out.println(line);
			}
			 
			input.close();
		} 
		catch(IOException e)  
	    {  
		    e.printStackTrace();  
		    return;  
		}
		
	}
}
