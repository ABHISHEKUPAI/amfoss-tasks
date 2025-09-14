#include <stdio.h>

int main() 
{
    FILE *file;
    int n;
    file = fopen("input.txt", "r");
    fscanf(file, "%d", &n); 
    fclose(file);

    // Pyramid logic
    for (int i = 1; i <= n; i++)
    {
        for (int s = 0; s < n - i; s++) 
        {
            printf(" ");
        }

        if (i == 1) 
        {
            printf("*");
        } 
        else if (i == n) 
        {
            for (int k = 0; k < 2 * n - 1; k++) 
            {
                printf("*");
            }
        }
        else 
        {
            printf("*");
            for (int sp = 0; sp < 2 * i - 3; sp++) 
            {
                printf(" ");
            }
            printf("*");
        }

        printf("\n");
    }
}
