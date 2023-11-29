#include<stdio.h>
#include<stdlib.h>
#define size 10

int top=-1;
int arr[size];
void push();
void pop();
void show();

int main(){
    int choice;
    while(1){
        printf("1.push 2.pop 3.display 4.exit");
        printf("enter yoyr choice:");
        scanf("%d",&choice);

        switch(choice){
            case 1:
            push();
            break;
            case 2:
            pop();
            break;
            case 3:
            show();
            case 4:
            exit(0);

            default:
            printf("\n Inavalid statement!!");
        }
        
    }
}