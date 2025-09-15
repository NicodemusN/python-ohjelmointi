#include <iostream>
using namespace std;

int main() {
    string nameList[3] = {"Alice", "Bob", "Charlie"};
    string myInput;
    //int n = 0;
    int s = sizeof(nameList);

    cout << "Anna nimi. ";
    cin >> myInput;

    for (int i = 0; i < 3; i++) {
        if (myInput == nameList[i]){
            cout << "Nimesi oli listalla.\n";
            break;
        }
    }

    return 0;
}