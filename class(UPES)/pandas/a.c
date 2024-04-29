#include<stdio.h>
int main(){
    int i;
    char a='*';
    for(i=0;i<5;i++){
        printf("%c\n",a);
        a='a'+'i';
    }
    return 0;
}