#include <iostream>
#include <fstream>
#include <cstdlib>
#include <ctime>
using namespace std;



string randpas()
{   string pass;
    const char alphanum[] = "0123456789!@#$%^&*abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    int string_length = sizeof(alphanum)-1;
    int n = 6;
    srand(time(0));
    for(int i = 0; i < n; i++)
    pass = alphanum[rand() % string_length];
    return pass;
}



int main() {
    for (int i = 1; 1<=100; i++) {
        string file;
        ofstream file(randpas()+".txt");
    }
  return 0;
}