
import java.io.*;

interface ui{
	void a_button();
	void b_button();
}

abstract class man{
	man(){ // Need not be "void man(void)" similarly to C++
		System.out.println("a man is born");
	}
	abstract protected void jump(); // to implement in sub class
	abstract protected void shot(); // to implement in sub class
}

class mario extends man implements ui{
	mario(){
		super();
		System.out.println("I am Mario");
	}
	// all the methods in the interface should be defined
	public void a_button(){
		this.jump();
	}
	public void b_button(){
		this.shot();
	}
	// all the abstract methods in the super class should be defined
	protected void jump(){
		System.out.println("Mario jumped");
	}
	protected void shot(){
		System.out.println("Mario fire");
	}
}

class rockman extends man implements ui{
	rockman(){
		super();
		System.out.println("I am Mega man");
	}
	// all the methods in the interface should be defined
	public void a_button(){
		this.jump();
	}
	public void b_button(){
		this.shot();
	}
	// all the abstract methods in the super class should be defined
	protected void jump(){
		System.out.println("rockman jumped");
	}
	protected void shot(){
		System.out.println("rockman shoot");
	}
}


public class _4_abstract_and_interface{
	public static void main(String args[]){ // returns error when it is written as "public static int"
		mario m = new mario();
		m.a_button();
		m.b_button();
		rockman r = new rockman();
		r.a_button();
		r.b_button();
	}
}


