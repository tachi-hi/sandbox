import java.io.*;
//import java.util.*;

public class _2_types{
	public static void main(String args[]){
		System.out.println("Difference from C++");

		System.out.println("int, long, float, and double may besically be identical to C++.");

		// ----------------------------------------------------------------------------------------
		System.out.println("\"char\" is not 1 byte. it is 2 bytes. char is positive (0 -- 65535).");

		for(int i = 0; i < java.lang.Character.MAX_VALUE; i++) // There are many useful constants defined in "java.lang.Something."
		{
			char c = (char)i;
			if (c % 100 == 0)
				System.out.print( c );
		}


		// ----------------------------------------------------------------------------------------
		System.out.println("\n \"short\" is also 2 bytes. \"short int\" is invalid in Java.");
		for(int i = -32768; i < 32768; i++)
		{
			short s = (short) i;
			if (s != 0 && s % 10000 == 0 || s == -32768 || s == 32767)
				System.out.println( s );
		}

		// ----------------------------------------------------------------------------------------
		System.out.println("\"byte\" is 1 byte. (-128 -- 127)");
		for(int i = -128; i < 128; i++)
		{
			byte b = (byte) i;
			if (b != 0 && b % 30 == 0 || b == -128 || b == 127)
				System.out.println( b );
		}

		// ----------------------------------------------------------------------------------------
		System.out.println(" Array");
		int array[] = new int [10]; // This is similar to "int *array = new int [100];" in C++
		// int array[100]; // This style is invalid.
		for(int i = 0; i < array.length; i++) array[i] = i * i;

		// Following works similarly to the pointer of C++ "int *array_tmp = array".
		// That is, "array_tmp" refers to "array". See below (*)
		int array_tmp[] = array;

		// Then how can we copy an array to another (create another instance) as easily as std::vector?
		// This is achieved by ".clone()" method.
		int array_copied[] = array.clone();

		// There is a class similar to "std::vector" in java.util.
		java.util.Vector<Integer> vec = new java.util.Vector<Integer>(0);
		java.util.Vector<Integer> vec_copied;

		for(int i = 0; i < array.length; i++)
		{
			vec.add(i * i * i);
			System.out.print( i + "^2 = " + array[i] + ", "+ i + "^3 = " + vec.get(i) + ", " );
			array[i] = 0;
		}
		
		// (*)
		System.out.println("\n Reference");
		for(int i = 0; i < array_tmp.length; i++)
		{
			System.out.print( i + "^2 = " + array_tmp[i] + ", ");
		}

		vec_copied = vec;
		System.out.println("\n Reference");
		for(int i = 0; i < array_tmp.length; i++)
		{
			System.out.print( i + "^2 = " + array_copied[i] + ", " + i + "^3 = " + vec_copied.get(i) + ", ");
		}
		
	}
}

