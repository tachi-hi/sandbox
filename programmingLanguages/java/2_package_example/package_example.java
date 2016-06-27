
// import java.io.*; // This is not required indeed

import myPackageExample.*; // This does not indicate that all the sub packages are imported. 
import myPackageExample.mySub.*; // Instead, we need to explicitly import the subpackage. <*>

public class package_example{
	public static void main (String args[]){
		myClass1 a = new myClass1();
		myClass2 b = new myClass2();



		// How to load a subpackage

		// Following is invalid even the myPackageExample is imported.
		// 		mySub.classInSubDirectory c = new mySub.classInSubDirectory(); 

		// We should write the path completely.
		myPackageExample.mySub.classInSubDirectory c = new myPackageExample.mySub.classInSubDirectory();

		// Following works if we have imported the corresponding subpackage (see <*> above)
		classInSubDirectory d = new classInSubDirectory();

		// Then, what should I do when the name of subclasses conflicted ?
	}
}

