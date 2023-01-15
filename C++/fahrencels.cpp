#include <iostream>

using namespace std;

int convert(int cels)
{   int fahren;
    fahren = cels * 9 / 5 + 32;
    return fahren;
}


int main()
{
    cout << convert(100)  << endl;
    return 0;
}
