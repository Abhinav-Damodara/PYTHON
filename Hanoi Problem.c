#include <stdio.h>
 
void towerofhanoi(int, char, char, char);
 
int main()
{
    int num;
 
    printf("Disks : ");
    scanf("%d", &num);
    printf("The Moves involved in the Tower of Hanoi are as follows :\n");
    towerofhanoi(num, 'A', 'C', 'B');
    return 0;
}
void towerofhanoi(int num, char frompeg, char topeg, char auxpeg)
{
    if (num == 1)
    {
        printf("\n Move disk 1 from peg %c to peg %c", frompeg, topeg);
        return;
    }
    towerofhanoi(num - 1, frompeg, auxpeg, topeg);
    printf("\n Move disk %d from peg %c to peg %c", num, frompeg, topeg);
    towerofhanoi(num - 1, auxpeg, topeg,frompeg);
}