#include <iostream>

using namespace std;

// brute force method
int magicNumber(int A[],int index,int length)
{
    if(index>=length)
        return -1;
    if(A[index]==index)
        return index;
    else
        return magicNumber(A,index+1,length);

}

int main()
{


    int A[]  = {-2,0,2,4,10};
    int length = sizeof(A)/sizeof(A[0]);

    cout << "magic index : "<<magicNumber(A,0,length)<<endl;
    cout << "Hello world!" << endl;
    return 0;
}
