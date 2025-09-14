#include <iostream>
#include <fstream>
using namespace std;

int main() 
{
    ifstream infile("input.txt");
    int n;
    infile >> n;
    infile.close();

    for (int i = 1; i <= n; i++) 
    {
        string spaces(n - i, ' ');

        if (i == 1) 
        {
            cout << spaces << "*" << endl;
        } 
        else if (i == n) 
        {
            cout << string(2 * n - 1, '*') << endl;
        } 
        else 
        {
            string inner_spaces(2 * i - 3, ' ');
            cout << spaces << "*" << inner_spaces << "*" << endl;
        }
    }
    return 0;
}
