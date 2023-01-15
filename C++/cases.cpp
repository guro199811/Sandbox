#include <iostream>

using namespace std;


string getDayOfWeek(int dayNum){
    string dayname;
    switch(dayNum){
        case 0:
            dayname ="sunday";
            break;
        case 1:
            dayname ="monday";
            break;
        case 2:
            dayname ="tuesday";
            break;
        case 3:
            dayname ="wednessday";
            break;
        case 4:
            dayname ="thurstday";
            break;
        case 5:
            dayname ="friday";
            break;
        case 6:
            dayname ="saturday";
            break;
        default:
            dayname = "invalid day num";
        
        
    }
    return dayname;
}
int main()
{   
    cout << getDayOfWeek(4);
    return 0;
}