# include <stdio.h>

int main (void)
{
    int n = 5;
    for (int i = 1; i<n+1;i++)
    {
        for (int s = 0; s < n - i; s++) 
        {
            printf(" ");
        }
        if (i == 1)
        {
            printf("*");
        }
        else if (i==n)
        {
            for (int a=0; a<2*n-1;a++)
            {
                printf("*");
            }
        }
        else
        {
            printf("*");
            for (int p =0;p<2*i-3;p++)
            {
                printf(" ");
            }
             printf("*");
        }

        printf("\n");
    } 
    printf("\n");
}