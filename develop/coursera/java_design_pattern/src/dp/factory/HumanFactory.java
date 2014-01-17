package dp.factory;

public class HumanFactory {
	public static Human createHuman(String m){
		Human p = null;
		if (m.toLowerCase() == "boy"){
			p = new Boy();
		}else if (m.toLowerCase() == "girl"){
			p = new Girl();
		}
		return p;
	}
}
