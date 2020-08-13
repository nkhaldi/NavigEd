#include "head.hpp"

void    printMenu() {
	cout << "\e[1;1H\e[2J";
    cout << "~~~ Menu ~~~" << endl;
    cout << "Choose subject to study:" << endl;
    cout << "1.\tMath" << endl;
    cout << "2.\tProgramming" << endl;
    cout << "3.\tEnglish" << endl;
    cout << "4.\tRobotics" << endl;
}

int     readSubj() {
    cout << endl << ">> ";
    int subj = 0;
    cin >> subj;
    return subj;
}

void    printSubj(int subj) {
    cout << "You chose ";
    
    switch (subj) {
	case 1:
        cout << "Math" << endl;
		break;
	case 2:
        cout << "Programming" << endl;
		break;
	case 3:
        cout << "English" << endl;
		break;
	case 4:
        cout << "Robotics" << endl;
		break;
	default:
		cout << "Unknown";
		break;
	}
}

int     main() {
    printMenu();
    int subj = readSubj();
    printSubj(subj);
    return 0;
}
