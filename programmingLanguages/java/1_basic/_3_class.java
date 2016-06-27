import java.io.*;

class robot{
	protected int weight;
	protected String name;

	robot(){
		this(0, "Prototype"); // this calles the constructor below (*)
	}
	// constructors can be defined polymorphously
	robot(int i, String s){ // (*)
		weight = i;		
		name = s;
	}
	robot(robot p){
		weight = p.weight;
		name = "Copied " + p.name;
	}
	String selfIntro(){
		return "My name is " + name + ".";
	}
}

class workingMachine extends robot{
	private String job;

	workingMachine(){
		super(); // execute the constructor of the super class
	}
	workingMachine(int i, String s){
		super(i, s);
	}
	workingMachine(workingMachine p){
		super(p);
	}

	void set_job(String job){
		this.job = job;
	}
	String get_job(){
		return job;
	}
	String selfIntro(){
		return "My name is " + name + ". My job is " + job + ".";
	}

	boolean equals(workingMachine p){ // overloaded. 
		return this.weight == p.weight && this.name == p.name && this.job == p.job;
	}

}

public class _3_class{
	public static void main(String args[]){
		robot p1;
		p1 = new robot ();
		System.out.println( "p1: " + p1.selfIntro() );

		robot p2 = new robot (30, "Alice");
		// robot p3 (30, "David"); // Invalid
	
		System.out.println( "p2: " + p2.selfIntro() );

		robot p3 = p2; // This does not call copy constructor
		System.out.println( "p3: " + p3.selfIntro() );
		
		robot p4 = new robot (p2); // Copy constructor is called
		System.out.println( "p4: " + p4.selfIntro() );
		

		
		workingMachine e1 = new workingMachine(25, "Bob");	
		e1.set_job("cleaning a room");
		System.out.println( "e1: " + e1.selfIntro() );

		workingMachine e2 = e1;
		System.out.println( "e2: " + e2.selfIntro() );

		workingMachine e3 = new workingMachine(e1);
		System.out.println( "e3: " + e3.selfIntro() );

		workingMachine e4 = new workingMachine(25, "Bob");	
		e4.set_job("cleaning a room");
		System.out.println( "e4: " + e4.selfIntro() );

		if(e1 == e2)
			System.out.println( "robots 1 and 2 are identical" );
		if(e1 != e3)
			System.out.println( "robots 1 and 3 are not identical" );
		if(e1 != e4)
			System.out.println( "robots 1 and 4 are not identical in terms of ==, even though they have identical parameters" );
		if(e1.equals( e4 ) )
			System.out.println( "robots 1 and 4 are identical in terms of .equals method" );
		
		robot p5 = new robot(e3);
		System.out.println( "p5: " + p5.selfIntro() );

		System.out.println("p1 is an instance of robot:          " + (p1 instanceof robot) );
		System.out.println("p1 is an instance of workingMachine: " + (p1 instanceof workingMachine) ); // not instance of a sub class
		System.out.println("e1 is an instance of robot:          " + (e1 instanceof robot) ); // instance of the super class
		System.out.println("e1 is an instance of workingMachine: " + (e1 instanceof workingMachine) );
		System.out.println("p5 is an instance of robot:          " + (p5 instanceof robot) ); // instance of the super class
		System.out.println("p5 is an instance of workingMachine: " + (p5 instanceof workingMachine) );
	}
}

