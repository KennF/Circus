package chapter.one.strategy;

public class MuteQuack implements QuackBehavior {

	@Override
	public void Quack() {
		System.out.println("<<silent>> quack");
	}

}
