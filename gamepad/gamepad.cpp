// sample program of gamepad

#include<GL/glfw.h>
#include<iostream>

using namespace std;

void KeyFunc(int key, int action){ // keyboard
	cout << "keyfunction" << endl;
	cout << (char)key << " " << action << endl;
}

void CharFunc(int char_, int action){ // character input
	cout << "charfunction" << endl;
	cout << (char)char_ << " " << action << endl;
	cout << glfwGetTime() << endl;
}

void MouseButtonFunc(int button, int action){ // mouse action
	cout << "buttonfunction" << endl;
	cout << button << " " << action << endl;

}

int main(){
	glfwSetTime(0);

	glfwInit();
	if(!glfwOpenWindow(640, 480, 8, 8, 8, 8, 24, 0, GLFW_WINDOW)){
		glfwTerminate();
		return 0;
	}

	glfwSetKeyCallback(KeyFunc);
	glfwSetCharCallback(CharFunc);
	glfwSetMouseButtonCallback(MouseButtonFunc);

	const int joystick_index = GLFW_JOYSTICK_2;
	// joystick
	if(glfwGetJoystickParam(joystick_index, GLFW_PRESENT) == GL_TRUE ){
		cout << "JoyStick 1 is active" << endl;
	}else{
		cout << "ccc" << endl;
	}

	int n_button = glfwGetJoystickParam(joystick_index, GLFW_BUTTONS);
	int n_axes = glfwGetJoystickParam(joystick_index, GLFW_AXES);

	unsigned char buttons[n_button];
	float axes[n_button];

	glfwSetWindowTitle("test");
	do{
		glfwGetJoystickPos(joystick_index, axes, n_axes);
		for(int i = 0; i < n_axes; i++){
			 cout << axes[i] << " ";
		}

		glfwGetJoystickButtons(joystick_index, buttons, n_button);
		for(int i = 0; i < n_button; i++){
			 cout << (buttons[i] == GLFW_PRESS ? "1 " : "0 ");
		}
		cout << endl;
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
		glfwSwapBuffers();
	}while(!glfwGetKey(GLFW_KEY_ESC) && glfwGetWindowParam (GLFW_OPENED));

	glfwTerminate();
	return 0;
}

