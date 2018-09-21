#include<iostream>
using namespace std;

int main(){
  int x,y,z;
  cin>>x>>y>>z;
  int arr[3] = {1,2,3};
  for(int i = 0;i <4; i++){
    x = arr[i];
  }
  cout<<"{"
        "\"key1\": "<< x << ","
        "\"key2\": "<< y << ","
        "\"key3\": "<< z << ""
        "}";
  return 0;
}
