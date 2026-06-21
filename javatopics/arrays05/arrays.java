// -----------------------------------------------------------------------
//             Array ke sabhi elements print karo.
// -----------------------------------------------------------------------

// import java.util.*;
// public class arrays {

//     public static void main(String[] args) {
//         int i,n;
//         Scanner ob = new Scanner(System.in);
            
//         // create a arrays
//         int[] arr = new int[5];
//         // array ko input le liya hai hamne
//         System.out.print("Enter the Array element : ");
//         for(i=0;i<arr.length;i++){
//             arr[i]=ob.nextInt();
//         }

//         System.out.println("Printed Array ............");
//         for(i=0;i<arr.length;i++){
//             System.out.print(arr[i] +" ");
//         }
//     }    
// }


// -----------------------------------------------------------------------
//             Array ke sabhi elements ko revers karo.
// -----------------------------------------------------------------------

// import java.util.*;
// public class arrays {

//     public static void main(String[] args) {
//         int i,n;
//         Scanner ob = new Scanner(System.in);
            
//         // create a arrays
//         int[] arr = new int[5];
//         // array ko input le liya hai hamne
//         System.out.print("Enter the Array element : ");
//         for(i=0;i<arr.length;i++){
//             arr[i]=ob.nextInt();
//         }

//         System.out.println("Printed Reverse Array ............");
//         for(i=arr.length-1;i>=0;i--){
//             System.out.print(arr[i] +" ");
//         }
//     }    
// }

// -----------------------------------------------------------------------
//             Array ke sabhi elements ka sum nikal.
// -----------------------------------------------------------------------

// import java.util.*;
// public class arrays {

//     public static void main(String[] args) {
//         int i,sum=0;
//         Scanner ob = new Scanner(System.in);
            
//         // create a arrays
//         int[] arr = new int[5];
//         // array ko input le liya hai hamne
//         System.out.print("Enter the Array element : ");
//         for(i=0;i<arr.length;i++){
//             arr[i]=ob.nextInt();
//         }

//         System.out.println("Sum of given array ............");
//         for(i=0;i<arr.length;i++){
//             sum = sum + arr[i];
//         }
//         System.out.print(sum);
//     }    
// }


// -----------------------------------------------------------------------
//             Array ke sabhi elements ka average nikalo.
// -----------------------------------------------------------------------

// import java.util.*;
// public class arrays {

//     public static void main(String[] args) {
//         int i,sum=0;
//         double ave=0;
       
//         Scanner ob = new Scanner(System.in);
            
//         // create a arrays
//         int[] arr = new int[5];
//         // array ko input le liya hai hamne
//         System.out.print("Enter the Array element : ");
//         for(i=0;i<arr.length;i++){
//             arr[i]=ob.nextInt();
//         }

//         System.out.println("Printed Array ............");
//         for(i=0;i<arr.length;i++){
//             sum +=arr[i];
//             ave = sum/arr.length;
//         }
//         int roundedInt = (int) Math.round(ave);
//         System.out.print(roundedInt);

//     }    
// }



// -----------------------------------------------------------------------
//             Array me maximum element find karo.
// -----------------------------------------------------------------------

// import java.util.*;
// public class arrays {

//     public static void main(String[] args) {
//         int i,size;

//         Scanner ob = new Scanner(System.in);
//         System.out.print("Enter the size of array : ");
//         size = ob.nextInt();
//         // create a arrays
//         int[] arr = new int[size];
//         // array ko input le liya hai hamne
//         System.out.print("Enter the Array element : ");
//         for(i=0;i<size;i++){
//             arr[i]=ob.nextInt();
//         }

//         int Max = arr[0];
//         System.out.println("Printed Maxmim number ............");
//         for(i=0;i<size;i++){
//            if (arr[i]>Max) {
//                 Max = arr[i];
//            }
//         }
//         System.out.print(Max +" ");
//     }    
// }


// -----------------------------------------------------------------------
//             Array me minimum element find karo.
// -----------------------------------------------------------------------

// import java.util.*;
// public class arrays {

//     public static void main(String[] args) {
//         int i,size;

//         Scanner ob = new Scanner(System.in);
//         System.out.print("Enter the size of array : ");
//         size = ob.nextInt();
//         // create a arrays
//         int[] arr = new int[size];
//         // array ko input le liya hai hamne
//         System.out.print("Enter the Array element : ");
//         for(i=0;i<size;i++){
//             arr[i]=ob.nextInt();
//         }

//         int Min = arr[0];
//         System.out.println("Printed Minmim number ............");
//         for(i=0;i<size;i++){
//            if (arr[i]<Min) {
//                 Min = arr[i];
//            }
//         }
//         System.out.print(Min +" ");
//     }    
// }


// -----------------------------------------------------------------------
//              Array me even numbers count karo. 
// -----------------------------------------------------------------------

// import java.util.*;
// public class arrays {

//     public static void main(String[] args) {
//         int i,size,count=0;

//         Scanner ob = new Scanner(System.in);
//         System.out.print("Enter the size of array : ");
//         size = ob.nextInt();
//         // create a arrays
//         int[] arr = new int[size];
//         // array ko input le liya hai hamne
//         System.out.print("Enter the Array element : ");
//         for(i=0;i<size;i++){
//             arr[i]=ob.nextInt();
//         }

//          System.out.println("Printed Even number : " );
//         for(i=0;i<size;i++){
//            if(arr[i]%2 ==0){
//             System.out.print( +arr[i] +" ");
//                count +=1;
//            }
//         }
//         System.out.println("\n Count Even number : " +count);
        
//     }    
// }


// -----------------------------------------------------------------------
//              Array me odd numbers count karo. 
// -----------------------------------------------------------------------

// import java.util.*;
// public class arrays {

//     public static void main(String[] args) {
//         int i,size,count=0;

//         Scanner ob = new Scanner(System.in);
//         System.out.print("Enter the size of array : ");
//         size = ob.nextInt();
//         // create a arrays
//         int[] arr = new int[size];
//         // array ko input le liya hai hamne
//         System.out.print("Enter the Array element : ");
//         for(i=0;i<size;i++){
//             arr[i]=ob.nextInt();
//         }

//          System.out.println("Printed odd number : " );
//         for(i=0;i<size;i++){
//            if(arr[i]%2!=0){
//             System.out.print( +arr[i] +" ");
//                count +=1;
//            }
//         }
//         System.out.println("\n Count odd number : " +count);
        
//     }    
// }


// -----------------------------------------------------------------------
//              count positive number in array 
// -----------------------------------------------------------------------

// import java.util.*;
// public class arrays {

//     public static void main(String[] args) {
//         int i,size,count=0;

//         Scanner ob = new Scanner(System.in);
//         System.out.print("Enter the size of array : ");
//         size = ob.nextInt();
//         // create a arrays
//         int[] arr = new int[size];
//         // array ko input le liya hai hamne
//         System.out.print("Enter the Array element : ");
//         for(i=0;i<size;i++){
//             arr[i]=ob.nextInt();
//         }

//         System.out.println("Printed Positive number : ");
//         for(i=0;i<size;i++){
//             if(arr[i]>0){
//                 System.out.print(arr[i] +" ");
//                count +=1;
//             }
//         }
//         System.out.print("\n Count Positive number  : " +count);
        
//     }    
// }


// -----------------------------------------------------------------------
//              count negitive number in array 
// -----------------------------------------------------------------------

// import java.util.*;
// public class arrays {

//     public static void main(String[] args) {
//         int i,size,count=0;

//         Scanner ob = new Scanner(System.in);
//         System.out.print("Enter the size of array : ");
//         size = ob.nextInt();
//         // create a arrays
//         int[] arr = new int[size];
//         // array ko input le liya hai hamne
//         System.out.print("Enter the Array element : ");
//         for(i=0;i<size;i++){
//             arr[i]=ob.nextInt();
//         }

//         System.out.println("Printed Positive number : ");
//         for(i=0;i<size;i++){
//             if(arr[i]<0){
//                 System.out.print(arr[i] +" ");
//                count +=1;
//             }
//         }
//         System.out.print("\n Count Positive number  : " +count);
        
//     }    
// }


// -----------------------------------------------------------------------
//              Array ke first aur last element swap karo.
// -----------------------------------------------------------------------

import java.util.*;
public class arrays {

    public static void main(String[] args) {
        int i,size;
        Scanner ob = new Scanner(System.in);
        System.out.print("Enter the size of array : ");
        size = ob.nextInt();
        // create a arrays
        int[] arr = new int[size];
        // array ko input le liya hai hamne
        System.out.print("Enter the Array element : ");
        for(i=0;i<size;i++){
            arr[i]=ob.nextInt();
        }

        // int temp = arr[0];
        // arr[0] = arr[size-1];
        // arr[size-1] = temp;

        System.out.println(" Array swap : ");
        for(i=0;i<size;i++){
            if(arr[0]!=arr[size-1]){
                int temp = arr[0];
                arr[0] = arr[size-1];
                arr[size-1] = temp;
                 System.out.print(+arr[i] +" ");
            }
        }
    }    
}