#include <iostream>

int main() {
    
    int x ; // Declaration of a variable
    x = 5; // Assignment of a variable

    int y = 10; // Declaration and assignment of a variable
    
    int sum = x + y; 
    std::cout << x << '\n'; // Output: 5
    std::cout << y << '\n'; // Output: 10
    std::cout << sum << '\n'; // Output: 15

    //integer (whole number)
    int age = 5;
    int year = 2021;
    int days = 36;

    //double (decimal number)
    double price = 5.99;
    double gpa = 3.9;
    double weight = 2.5;

    //char (single character)
    char letter = 'A';
    char symbol = '$';
    char grade = 'B';
 
    //bool (boolean)
    bool isTrue = true;
    bool isFalse = false;
    bool forSale = true;

    //string (sequence of characters)
    std::string name = "John";
    std::string city = "New York";
    std::string country = "USA";
    
    std::cout << "Hello " << name << '\n';
    std::cout << "You are " << age << " years old" << '\n';

    return 0;
}

