package dp.abstractfactory;

public class IntelCPUFactory implements CPUFactory {

	@Override
	public CPU produceCPU() {
		return new IntelCPU();

	}

}
