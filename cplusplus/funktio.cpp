#include <iostream>
using namespace std;

int a, b;
double avr, sum;

void average() {
    cout << "Annappa luku 1: \n";
    cin >> a;
    cout << "Annappa luku 2: \n";
    cin >> b;

    sum = a + b;
    avr = sum / 2;
    cout << "Lukujesi keskiarvo on: " << avr << "\n";
}

int main() {
    average();
    cout << "Muuttujan avr tavukoko:\n";
    cout << sizeof(avr) << "\n";
    return 0;
}