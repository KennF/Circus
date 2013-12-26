package dp.abstractfactory;

public class AMDCPUFactory implements CPUFactory {

	@Override
	public CPU produceCPU() {
		return new AMDCPU();
	}

}
