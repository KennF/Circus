package chapter.one.strategy;

public class Quack implements QuackBehavior {

	@Override
	public void Quack() {
		System.out.println("Quack, Quack");
	}

}
