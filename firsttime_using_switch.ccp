#include <iostream>
using namespace std;

int main() {
    int choice = 2;

    switch (choice) {
        case 1:
            cout << "Coffee";
            break;

        case 2:
            cout << "Tea";
            break;

        case 3:
            cout << "Water";
            break;

        default:
            cout << "Invalid choice";
    }

    return 0;
}