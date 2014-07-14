#include <stdio.h>

/*

printf

user's input = underlined text

Height: 4
   #  #
  ##  ##
 ###  ###
####  ####

i in range(0,23)

if user input not in range
then

use getint 

output = 
Height: -2
Height: -1
Height: foo
Retry: bar
Retry: 1
##

#1 hacker

*/

int main(void)

{
    
int i;
int n;
int spaces;
int hash;
int j;
 
   printf("Please input an integer value between 0 and 23: ");
   scanf("%d", &i);
   printf("Height: %d\n", i);

   if ( i>23 ) {
    printf("output = "
            "Height: -2"
            "Height: -1"
            "Height: foo"
            "Retry: bar"
            "Retry: 1");
            return 0;
    }

    for (n = 0; n < i; n++)
     {
      int spaces  = i - n;
        //print spaces
      for (j = 0; j<spaces;j++)
      {

        printf(" ");
      }
      for (j = 0;j<=n;j++)
        {
          //print hashes
        printf("#");

          //print new line
        }

        printf(" ");
      
      for (j = 0;j<=n;j++)
      {
          //print hashes
        printf("#");

          //print new line
      }

      printf("\n");
     }
    return 0;
}
