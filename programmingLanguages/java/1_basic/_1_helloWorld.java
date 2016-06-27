
import java.io.*;

class helloWorld{
	// java className calles the main function of the class
	public static void main(String args[]){
		System.out.println("Hello World!");
	}
}

// we can define more than two classes in a single file
// javac generates the .class file for each class.
class fizzBuzz{
	public static void main(String args[]){
		for(int i = 0; i < 100; i++)
			System.out.println(i % 15 == 0 ? "fizzbuzz " :
			                   i %  3 == 0 ? "fizz " : 
			                   i %  5 == 0 ? "buzz " : 
			                   i );
	}
}

// -- Memo
// Some online documents claim that the filename of the source code 
// and the name of class should be identical but the code above works.
// My question is whetehr it is the grammatical rule or just a coding convention, 
// or it depends on the version.

// A source can contain only one "public class" in a single file.
public class _1_helloWorld{ // The name of class shoud not be start with [0-9]. It should be alphabets or _ or $. 
	public static void main(String args[]){
		System.out.println("Number of public class is restricted to 1 in a single file");
	}
}

