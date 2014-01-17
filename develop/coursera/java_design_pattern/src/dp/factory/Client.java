package dp.factory;

public class Client {
	public static void main(String[] args){
		Human boy = HumanFactory.createHuman("boy");
		boy.Talk();
		boy.Walk();
		Human girl = HumanFactory.createHuman("girl");
		girl.Talk();
		girl.Walk();
	}

}
