#include <stdio.h>

#include <string.h>

#include <math.h>

#include <stdlib.h>

 

int main() {  

    int T;

    scanf("%d",&T);

    for (int i = 0;i<T;i++)

    {

        int x;

        scanf("%d",&x);

        if (x <=10)

        {

            printf("YES\n");

        }

    else

        {

        printf("NO\n");

        }

    }

  

    return 0;

}

 

Question 2

#include <stdio.h>

#include <string.h>

#include <math.h>

#include <stdlib.h>

 

int main()

{

    int x,y,z;

    scanf("%d",&x);

    for (int i=0;1<x;i++)

    {

      scanf("%d %d",&y,&z);

       

        if (y>x)

        {

            printf("%d\n",z);

        }

        else

        {

            printf("%d\n",y);

        }

    }

    return 0;

}

 

 

 

Question3

#include <stdio.h>

#include <string.h>

#include <math.h>

#include <stdlib.h>

 

int main() {

 

    int T,x,y,n;

    scanf("%d",&T);

    for(int i =0;i<T;i++)

    {

        scanf("%d %d %d",&n,&x,&y);

        int cap=(n+1)*y;

        if (cap >= x)

        {

            printf("YES\n");

        }

        else

        {

            printf("NO\n");

        }

    }

    return 0;

}

 

 

 

Question 4

#include <stdio.h>

#include <string.h>

#include <math.h>

#include <stdlib.h>

 

int main() {

    int T,X,Y;

    scanf("%d",&T);

    while(T--) 

          {

              scanf ("%d %d",&X,&Y);

              int floora=(X-1)/10+1;

              int floorb=(Y-1)/10+1;

              printf("%d\n",abs(floora-floorb));

          }

    return 0;

}

Question 5

#include <stdio.h>

 

int main() {

    int t;

    scanf("%d", &t);  
    while (t--) {    
        int n, x;

        scanf("%d %d", &n, &x);
 

        int first = -1, last, d;  

 

        for (int i = 0; i < n; i++) {   
            scanf("%d", &d);          

 

            if (d == 1) {               
                if (first == -1)     

                    first = i;          
                last = i;              
            }

        }

 

      

        if (last - first + 1 <= x)      

            printf("YES\n");

        else

            printf("NO\n");

    }

    return 0;

}

 

Question 6

#include <stdio.h>

 

int main() {

    int T;

    scanf("%d", &T);

 

    while (T--) {

        int N;

        scanf("%d", &N);

 

        int freq[11] = {0};  

        int num;

 

        for (int i = 0; i < N; i++) {

            scanf("%d", &num);

            freq[num]++;     

        }

 

        int max_count = 0;

        for (int i = 1; i <= 10; i++) {

            if (freq[i] > max_count) {

                max_count = freq[i];

            }

        }

 

        int moves = N - max_count;

        printf("%d\n", moves);

    }

 

    return 0;

}


