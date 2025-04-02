#include <iostream>

namespace first{
    int x = 1;
}
namespace second{
    int x = 2;
}
int main() {
    //using namespace first; 
    //using namespace std; 

    int x = 0;

    std::cout << x;
    std::cout << first::x;
    std::cout << second::x;

    return 0;
}