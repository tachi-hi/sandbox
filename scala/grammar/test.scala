

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

	}
}

