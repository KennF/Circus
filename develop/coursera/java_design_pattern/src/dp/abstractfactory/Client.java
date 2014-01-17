package dp.abstractfactory;

public class Client {
	public static void main(String[] args){
		Computer computer = new Computer(createSpecificFactory());
		computer.process();
	}
	
	public static CPUFactory createSpecificFactory(){
		int sys = 1; // based on specific requirement
        if (sys == 0) 
        	return new AMDCPUFactory();
        else 
        	return new IntelCPUFactory();
	}
}
