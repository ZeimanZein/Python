#include <iostream>
using namespace std;
int main(){
    int s = 0;
    string t;
    cin>>t;
    for(int i=0;i<t.size();i++){
        if(t[i]=='I' && t[i+1]=='V'){
        s+=4;
        i++;    
        } else if(t[i]=='I' && t[i+1]=='X'){
            s+=9;
            i++;
        } else if(t[i]=='X' && t[i+1]=='L'){
            s+=40;
            i++;
        } else if(t[i]=='X' && t[i+1]=='C'){
            s+=90;
            i++;
        } else if(t[i]=='C' && t[i+1]=='D'){
            s+=400;
            i++;} else if(t[i]=='C' && t[i+1]=='M'){
            s+=900;
            i++; 
        } 
          else if(t[i]=='I') {s+=1; i++;}
          else if(t[i]=='V') {s+=5; i++;}
          else if(t[i]=='X') {s+=10; i++;}
          else if(t[i]=='L') {s+=50; i++;}
          else if(t[i]=='C') {s+=100; i++;}
          else if(t[i]=='D') {s+=500; i++;}
          else if(t[i]=='M') {s+=1000; i++;}
    } 
    cout<<s;
}