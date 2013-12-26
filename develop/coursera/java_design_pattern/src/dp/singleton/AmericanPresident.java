package dp.singleton;

public class AmericanPresident {
	private AmericanPresident() {
		this.name =  "B. Obama";
	}
	
	public String name;
	private static AmericanPresident president;
	
	public static AmericanPresident getPresident(){
		if(president == null) {
			president = new AmericanPresident();
		}
		return president;
	}
	

}
