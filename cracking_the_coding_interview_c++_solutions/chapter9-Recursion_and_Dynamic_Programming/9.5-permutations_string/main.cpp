#include <iostream>
#include <string.h>
using namespace std;

void printPermutations(char *s,int start,int length)
{

if(start==length)
{
cout << s << endl;
return;
}

else{

for(int j = start;j<=length;j++)
    {
    swap(s[start],s[j]);
    printPermutations(s,start+1,length);
    swap(s[start],s[j]);

    }

}
}



int main()
{

char  s[]= "abc";
//cout << strlen(s) <<endl;
printPermutations(s,0, strlen(s)-1);
   // cout << "Hello world!" << endl;
    return 0;
}
