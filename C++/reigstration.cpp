#include <iostream>
#include <map>
#include <fstream>
#include <string>

using namespace std;
// Declare global map to store user information
map<string, string> userlist;

// Function to handle user registration
void register_user()
{
    string username, password;
    
    // Prompt user for username
    cout << "Username: ";
    cin >> username;
    
    // Check if username is too short and ask for a new one if necessary
    int username_length = username.size();
    if (username_length < 4)
    {
        cout << "Your username should be at least 4 characters. Please enter a new one: ";
        cin >> username;
        if (username.size() < 4)
        {
            cout << "Wrong again, exiting program." << endl;
            return;
        }
    }
    
    // Prompt user for password
    cout << "Password: ";
    cin >> password;
    
    // Check if password is too short and ask for a new one if necessary
    int password_length = password.size();
    if (password_length < 6)
    {
        cout << "Your password should be at least 6 characters. Please enter a new one: ";
        cin >> password;
        if (password.size() < 6)
        {
            cout << "Wrong again, exiting program." << endl;
            return;
        }
    }
    
    // Add username and password to the userlist map
    userlist[username] = password;
}

int main()
{
    bool program_running = true;
    string user_operation;

    // Open file to store user information
    fstream myfile("users.json");

    // Loop until user quits program
    while (program_running)
    {
        // Prompt user for operation to perform
        cout << "Hello user, Please input what operation should be performed" << endl;
        cout << "1) Register\n2) Log in\n:";
        cin >> user_operation;

        // Perform the selected operation
        if (user_operation == "1")
        {
            register_user();
        }
        else if (user_operation == "2")
        {
            // Prompt user for username and password
            cout << "Username: ";
            string username;
            cin >> username;
            cout << "Password: ";
            string password;
            cin >> password;

            // Check if username and password are correct
            if (userlist.count(username) > 0 && userlist[username] == password)
            {
                cout << "You have successfully logged in." << endl;
            }
            else
            {
                cout << "Username or password is incorrect. Please try again." << endl;
            }
        }
        else
        {
            cout << "Invalid operation. Please try again." << endl;
        }

        // Ask user if they want to perform another operation
        cout << "Do you want to perform another operation? (y/n): ";
        string user_response;
        cin >> user_response;
        if (user_response == "n")
        {
            program_running = false;
        }
    }

    // Close file
    myfile.close();

    return 0;
}
