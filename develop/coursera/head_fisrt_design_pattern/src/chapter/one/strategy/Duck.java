package chapter.one.strategy;

public class Duck {
	FlyBehavior flyBehavior;
	QuackBehavior quackBehavior;

	public Duck() {

	}

	public void display() {
		System.out.print("I'm Duck");
	}

	public void performFly() {
		flyBehavior.Fly();
	}

	public void performQuack() {
		quackBehavior.Quack();
	}

}
