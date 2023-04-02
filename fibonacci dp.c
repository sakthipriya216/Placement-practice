// This code is fibonacci using dp
#include<stdio.h>
long long int f[10000]={0};
long long int fib(int n)
{
    if(n==0)
        return f[n];
    if(n==1 || n==2)
        return f[n]=1;
    if(f[n]!=0)
        return f[n];
    return f[n]=fib(n-1)+fib(n-2);
    
}
int main()
{
    int n;
    printf("Enter the number: ");
    scanf("%d",&n);
    printf("%lld",fib(n));
}
