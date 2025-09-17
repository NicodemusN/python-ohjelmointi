#include <iostream>
using namespace std;

// kopioitu esimerkkikoodi w3schoolsista

class MyClass {             //luokka
    public:                 //"access" taso
        int myNum;          //attribuutti (kokonaisluku)
        string myString;    //attribuutti (merkkijono)
};

int main() {
    MyClass myObj;                  // luodaan olio luokasta MyClass
    
    // Käytetään pääsyä attribuutteihin ja arvoihin
    myObj.myNum = 15;               
    myObj.myString = "Some text";

    // printataan attribuuttien arvot
    cout << myObj.myNum << "\n";
    cout << myObj.myString;
    return 0;
}

// lopputuloksena muuttujien myNum ja myString arvot itsessään
// luokassa myClass eivät muutu (pysyvät nollassa), mutta
// main-funktiossa voidaan hyödyntää niitä arvojen syöttämiseen
// muita tarkoituksia varten.