/*km = int(input("Please input KM: "))
mil = km / 1.6
print(f"your km in miles is {mil}")*/

#include <iostream>

using namespace std;

double convert(int km){
    double miles;
    miles = km / 1.6;
    return miles;
}
int main()
{
    cout << convert(10)  << endl;
    return 0;
}
