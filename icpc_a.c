#include<stdio.h>
#include<string.h>

int main()
{
    int n, i, j;
    scanf(" %d", &n);
    char str[100];

    for (i = 0; i < n; i++)
    {
        scanf(" %s", str);
        char new[100];
        strcpy(new, str);

        for (j = 0; j < strlen(new) ; j++)
        {
            if (new[j] == 'c')
            {
                if(new[j + 1] == 'a' || new[j+1] == 'o' || new[j+1] == 'u')
                {
                    new[j] = 'k';
                }
                else if (new[j + 1] != 'a' && new[j+1] != 'e' && new[j+1] != 'i' && new[j+1] != 'o' && new[j+1] != 'u' && new[j+1] != 'y' && new[j+1] != 'h')
                {
                    new[j] = 'k';
                }
                else if(new[j+1] == 'e' || new[j+1] == 'i' || new[j+1] == 'y')
                {
                    new[j] = 's';
                }
                else if (new[j+1] == 'h')
                {
                    new[j] = 'c';
                    new[j+1] = '1';
                    
                }
            }
            
        }
        for(j = 0; j < strlen(new); j++)
        {
            if(new[j] != '1')
            {
                printf("%c", new[j]);
            }
        }
        printf("\n");
    }
}
