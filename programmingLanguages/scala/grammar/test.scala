


object test{
	def main(args: Array[String]){

		// Hello world
		println("Hello World!");

		// Variables and constants
		// --------------------------------------------------------------------
		// Variables
		var a = 1 // variable
		println(a)

		var b:Int = 1 // We may specify the type
		var c:Double = 1 // variable
		println(b + c) // Int + Double is not type error


		// We may call the method even if it is as if a primitive type (scala has no primitive type)
		println( 30.toString ) 
		println( "1".toInt + 1 )
		
		// Constants
		val d = 100 // constant
		val finalString = "Constnat" // constant
		println(d)
		println(finalString)

		// If
		// --------------------------------------------------------------------
		if (true){
			println( "True" )	
		}


		// Array and for
		// --------------------------------------------------------------------
		val myArray = Array(1,2,3,4,5,6)
		var sizedArray = new Array[Double](5)

		
		for(i <- 0 until myArray.length){
			println(i, myArray(i) )
		}

		// also written as
		for(elem <- myArray){
			println( elem )
		}

		// foreach
		myArray.foreach{ e => println(e * 100) }
		var myArrayDouble = myArray.foreach{e => e * 2} // This does not return the doubled array.
		println(myArrayDouble)
		//myArrayDouble.foreach{ e => println(e)}
		
		// This is achieved by "for ... yield" as follows
		var myArrayTriple = for( e <- myArray ) yield e * 3
		myArrayTriple.foreach{ e => println(e) }
		
		// Function (method of a class)
		//-----------------------------------------------------------------------
		println( myFunction(1,2) )
		printMessage()

		// Function (function object)
		//-----------------------------------------------------------------------
		var myFuncObj = (x:Int, y:Int) => (x + y)
		// var myFuncObj : (Int, Int) => Int = (x:Int, y:Int) => (x + y) 
		// ": (Int, Int) => Int" is the type of this function
		println( myFuncObj(1,2) )

		// Recursion requires the infomation on the type
		// Recursive function cannot be defined as var nor val (?)
		def Fibonacci : Int => BigInt = 
		n => n match {
				case i:Int if i < 1 => 0
				case 1 | 2 => 1
				case _:Int => Fibonacci( n - 1) + Fibonacci( n - 2 )
			}

		println( Fibonacci(1) )
		println( Fibonacci(2) )
		println( Fibonacci(3) )
		println( Fibonacci(4) )
		println( Fibonacci(5) )
		println( Fibonacci(6) )
	}

	def myFunction(x:Int, y:Int):Int = 
	{
		return x + y // return is not necessary; scala automatically returns the last value
	}
	def printMessage():Unit =  
	{
		println("void")
	}
}

