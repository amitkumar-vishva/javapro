// -----------------------------------------------------------------------------------------
//         simple array print karna matrix form me
// -----------------------------------------------------------------------------------------

// public class twodarray {
//     public static void main(String[] args) {
//         int i,j;
//         int[][] arr = new int[3][4];

//         // es line ki help se ham pata laga sakte hai ki kitni row or kitne col hai
//         System.out.println(arr.length +" " +arr[0].length);
//         for(i=0;i<3;i++){
//             for(j=0;j<4;j++){
//                 System.out.print(arr[i][j] +" ");
//             }
//             System.out.println();
//         }
        
//     }    
// }


// -----------------------------------------------------------------------------------------
//         input section 
// -----------------------------------------------------------------------------------------

// import java.util.Scanner;

// public class twodarray {
//     public static void main(String[] args) {
//         int i,j;
//         Scanner ob = new Scanner(System.in);
//         int[][] arr = new int[3][3];

//         // Array input le liya hai mene 
//         System.out.print("Enter the element of array matrix : ");
//         for(i=0;i<arr.length;i++){
//             for(j=0;j<arr[0].length;j++){
//                 arr[i][j]=ob.nextInt();
//             }
//         }

//         // Array print kar diya hai mene
//         System.out.println("Matrix printed...............");
//         for(i=0;i<arr.length;i++){
//             for(j=0;j<arr[0].length;j++){
//                 System.out.print(arr[i][j] +" ");
//             }
//             System.out.println();
//         }
//     }    
// }


// -----------------------------------------------------------------------------------------
//         Sum of give matrix element
// -----------------------------------------------------------------------------------------

// import java.util.Scanner;

// public class twodarray {
//     public static void main(String[] args) {
//         int i,j,sum=0;
//         Scanner ob = new Scanner(System.in);
//         int[][] arr = new int[3][3];

//         // Array input le liya hai mene 
//         System.out.print("Enter the element of array matrix : ");
//         for(i=0;i<arr.length;i++){
//             for(j=0;j<arr[0].length;j++){
//                 arr[i][j]=ob.nextInt();
//             }
//         }

//         // Array print kar diya hai mene
//         System.out.println("Sum of given Matrix ...............");
//         for(i=0;i<arr.length;i++){
//             for(j=0;j<arr[0].length;j++){
//                 sum+=arr[i][j];
//             }
//         }
//         System.out.println(sum);
//     }    
// }


// -----------------------------------------------------------------------------------------
//         largest number find karo matrix ka
// -----------------------------------------------------------------------------------------

// import java.util.Scanner;

// public class twodarray {
//     public static void main(String[] args) {
//         int i,j;
//         Scanner ob = new Scanner(System.in);
//         int[][] arr = new int[3][3];

//         // Array input le liya hai mene 
//         System.out.print("Enter the element of array matrix : ");
//         for(i=0;i<arr.length;i++){
//             for(j=0;j<arr[0].length;j++){
//                 arr[i][j]=ob.nextInt();
//             }
//         }

//         // Array print kar diya hai mene
//         int Max = arr[0][0];
//         System.out.println("Largest no of given Matrix ...............");
//         for(i=0;i<arr.length;i++){
//             for(j=0;j<arr[0].length;j++){
//                if(arr[i][j]>Max){
//                 Max=arr[i][j];
//                }
//             }
//         }
//         System.out.println(Max);
//     }    
// }


// -----------------------------------------------------------------------------------------
//         smallest number find karo matrix ka
// -----------------------------------------------------------------------------------------

// import java.util.Scanner;

// public class twodarray {
//     public static void main(String[] args) {
//         int i,j;
//         Scanner ob = new Scanner(System.in);
//         int[][] arr = new int[3][3];

//         // Array input le liya hai mene 
//         System.out.print("Enter the element of array matrix : ");
//         for(i=0;i<arr.length;i++){
//             for(j=0;j<arr[0].length;j++){
//                 arr[i][j]=ob.nextInt();
//             }
//         }

//         // Array print kar diya hai mene
//         int smallest = arr[0][0];
//         System.out.println("smallest no of given Matrix ...............");
//         for(i=0;i<arr.length;i++){
//             for(j=0;j<arr[0].length;j++){
//                if(arr[i][j]<smallest){
//                 smallest=arr[i][j];
//                }
//             }
//         }
//         System.out.println(smallest);
//     }    
// }


// -----------------------------------------------------------------------------------------
//sabhi row ka sum karo fir largest row number nikalo
// -----------------------------------------------------------------------------------------

import java.util.Scanner;

public class twodarray {
    public static void main(String[] args) {
        int i,j;
        Scanner ob = new Scanner(System.in);
        int[][] arr = new int[3][3];

        // Array input le liya hai mene 
        System.out.print("Enter the element of array matrix : ");
        for(i=0;i<arr.length;i++){
            for(j=0;j<arr[0].length;j++){
                arr[i][j]=ob.nextInt();
            }
        }

        // Array print kar diya hai mene
        int smallest = arr[0][0];
        System.out.println("smallest no of given Matrix ...............");
        for(i=0;i<arr.length;i++){
            for(j=0;j<arr[0].length;j++){
               if(arr[i][j]<smallest){
                smallest=arr[i][j];
               }
            }
        }
        System.out.println(smallest);
    }    
}

