#include <iostream>
#include <vector>
#include <string>
#include <sstream>
using namespace std;

int main()
{


char A[]="abcd";

vector<string> output;

output.push_back("");
string singleChar;
string newCombination;
int arrayLength= sizeof(A)-1;

for(int i=0;i<arrayLength;i++)
{
stringstream ss;

ss << A[i];
ss >> singleChar;

int len = output.size();
for(int j=0;j<len;j++)
{
newCombination = output[j] + singleChar;
output.push_back(newCombination);
cout <<newCombination<<endl;;

}


}


    return 0;
}
