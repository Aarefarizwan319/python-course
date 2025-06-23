#include<iostream>
using namespace std;
int main()
{
    int number;
    cout<<"\n\n\t\t Check weather umber is positive , negative or zero\t\t\t;"
    cout<<"\n\t\t\t ===================\t\t\t";
    cout<<"\n\t Enter number\t\t;"
    cin>>number;
    if(number>0)
    {
        cout<<"\n\t Number is positive\t\n";
    }
    else if(number<0)
    {
        cout<<"\t Number is negative\t\n";
    }
    else
    {
        cout<<"\t Number is zero\t\n"
    }
    return 0;
}