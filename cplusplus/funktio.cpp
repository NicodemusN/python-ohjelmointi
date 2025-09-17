#include <iostream>
using namespace std;

int a, b;

void average() {
    cout << "Annappa luku 1: \n";
    cin >> a;
    cout << "Annappa luku 2: \n";
    cin >> b;

    int sum = a + b;
    float avr = sum / 2;
    cout << "Lukujesi keskiarvo on: " << avr << "\n";
}

int main() {
    average();

    return 0;
}