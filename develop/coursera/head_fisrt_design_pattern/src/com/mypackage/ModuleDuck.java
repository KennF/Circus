package com.mypackage;

public class ModuleDuck extends Duck {
	public ModuleDuck(){
		flyBehavior = new FlyWithWings();
		quackBehavior = new MuteQuack();
	}
	
	public void display() {
		System.out.println("I am Module Duck");
	}
	
	public static void main(String [] args){
		ModuleDuck moduleDuck = new ModuleDuck();
		moduleDuck.performFly();
		moduleDuck.performQuack();
		moduleDuck.display();
	}

}
