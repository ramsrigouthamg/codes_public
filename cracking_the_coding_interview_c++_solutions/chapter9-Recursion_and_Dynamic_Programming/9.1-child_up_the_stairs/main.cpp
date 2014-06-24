#include <iostream>

using namespace std;


//method 1 - bottom up tracking
int noOfWays1(int n)
{
if(n<0)
    return 0;
else if(n==0)
    return 1;
else
    return noOfWays1(n-1)+noOfWays1(n-2)+noOfWays1(n-3);

}

// method2 - top down recursion
int noOfWays2(int n,int maxValue)
{
if(n>maxValue)
    return 0;
else if(n==maxValue)
    return 1;
else
    return noOfWays2(n+1,maxValue)+noOfWays2(n+2,maxValue)+noOfWays2(n+3,maxValue);

}




int main()
{
// Assuming 15 steps
cout << noOfWays1(15)<<endl;
cout << noOfWays2(0,15)<<endl;
    cout << "Hello world!" << endl;
    return 0;
}
