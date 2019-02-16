#include <iostream> 
using namespace std; 
  
namespace ns 
{ 
    // Only declaring class here 
    class geek; 
    void f();
} 
  
// Defining class outside 
class ns::geek 
{ 
public: 
    void display() 
    { 
        cout << "ns::geek::display()\n"; 
    } 
}; 
void ns::f() {};
  
int main() 
{ 
    //Creating Object of student Class 
    ns::geek obj; 
    obj.display(); 
    return 0; 
} 