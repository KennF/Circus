package dp.abstractfactory;

public class Computer {
	CPU cpu = null;
	
	public Computer(CPUFactory factory){
		cpu = factory.produceCPU();
		
	}
	
	public void process(){
		cpu.process();
	}

}
