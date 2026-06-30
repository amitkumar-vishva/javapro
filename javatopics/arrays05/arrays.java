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

//         // int temp = arr[0];
//         // arr[0] = arr[size-1];
//         // arr[size-1] = temp;

//         System.out.println(" Array swap : ");
//         for(i=0;i<size;i++){
//             if(arr[0]!=arr[size-1]){
//                 int temp = arr[0];
//                 arr[0] = arr[size-1];
//                 arr[size-1] = temp;
//                  System.out.print(+arr[i] +" ");
//             }
//         }
//     }    
// }

// second method

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

//         int temp = arr[0];
//         arr[0] = arr[size-1];
//         arr[size-1] = temp;

//         System.out.println(" Array swap : ");
//         for(i=0;i<size;i++){
//            System.out.print(arr[i] +" ");
//         }
//     }    
// }

// -----------------------------------------------------------------------
//             Array me largest aur smallest element ka difference nikalo.
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
//         int smallest = arr[0];      
//         // System.out.println("Printed Array small number ............");
//         for(i=0;i<size;i++){
//            if (arr[i]>Max) {
//                 Max = arr[i]; 
//            }
//            else if(arr[i]<smallest){
//             smallest = arr[i];
//            }
//         }
//         int sub1 = Max - smallest;
//         System.out.print("\n Largest no : " +Max +" ");
//         System.out.print("\n Smallest no : " +smallest +" ");
//         System.out.print("\n Difference of both no : " +sub1);   
//     }    
// }

// -----------------------------------------------------------------------
//              Array me zero kitni baar aaya hai count karo.
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

//         // System.out.println("Printed Positive number : ");
//         for(i=0;i<size;i++){
//             if(arr[i]==0){
//                 // System.out.print(arr[i] +" ");
//                count +=1;
//             }
//         }
//         System.out.print("\n Count zero number  : " +count);
        
//     }    
// }

// -----------------------------------------------------------------------
//              Array ke sabhi elements ka product nikalo.
// -----------------------------------------------------------------------

// import java.util.*;
// public class arrays {

//     public static void main(String[] args) {
//         int i,size,product=1;

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

//         // System.out.println("Printed Positive number : ");
//         for(i=0;i<size;i++){
//             product = product*arr[i];
//         }
//         System.out.print("Product of given array  : " +product);
        
//     }    
// }


// -----------------------------------------------------------------------
//             Array me second largest element find karo.
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

//         int firstNo = arr[0];
//         int secondNo = arr[0];
//         System.out.println("Printed largest number ............");
//         for(i=0;i<size;i++){
//            if (arr[i]>firstNo) {
//                 firstNo = arr[i];
//            }
//            else if(arr[i]>secondNo){
//                 secondNo = arr[i];
//            }
//         }
//         System.out.print("\n First largest number : " +firstNo +" ");
//         System.out.print("\n second largest number : " +secondNo +" ");
//     }    
// }


// -----------------------------------------------------------------------
//             Array me second smallest element find karo.
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

//         int firstNo = arr[0];
//         int secondNo = arr[0];
//         System.out.println("Printed smallest number ............");
//         for(i=0;i<size;i++){
//            if (arr[i]<firstNo) {
//                 firstNo = arr[i];
//            }
//            else if(arr[i]<secondNo){
//                 secondNo = arr[i];
//            }
//         }
//         System.out.print("\n First smallest number : " +firstNo +" ");
//         System.out.print("\n second smallest number : " +secondNo +" ");
//     }    
// }

// -----------------------------------------------------------------------
//             Array me second largest element find karo.
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

//         int firstNo = arr[0];
//         int secondNo = arr[0];
//         System.out.println("Printed largest number ............");
//         for(i=0;i<size;i++){
//            if (arr[i]>firstNo) {
//                 firstNo = arr[i];
//            }
//            else if(arr[i]>secondNo){
//                 secondNo = arr[i];
//            }
//         }
//         System.out.print("\n First largest number : " +firstNo +" ");
//         System.out.print("\n second largest number : " +secondNo +" ");
//     }    
// }

// -----------------------------------------------------------------------
//            two sum.
// -----------------------------------------------------------------------

// import java.util.*;
// public class arrays {

//     public static void main(String[] args) {
//         int[] arr = {2,3,4,5,6};
//         int target = 9;
//         int i,j;
//         for(i=0;i<arr.length;i++){
//             for(j=i+1;j<arr.length;j++){
//                 if (arr[i]+arr[j] == target) {
//                     System.out.println(arr[i] + " " + arr[j]);
//                 }
//             }
//         }
//     }    
// }

// -----------------------------------------------------------------------
//             Remove elemets
// -----------------------------------------------------------------------

// import java.util.*;
// public class arrays {
//     public static void main(String[] args) {
//         int[] arr = {9,8,7,6,5};
//         for(int i=0;i<arr.length;i++){
//            if(arr[i]!= 8){
//                System.out.print(arr[i] +" ");
//            }
          
//         }
//     }
// }

// -------------------------------------------------------------------------
//     Remove duplicate value
// -------------------------------------------------------------------------

// public class demo {
//     public static void main(String[] args) {
//         int[] marks = {92, 90, 78, 92,79};
//         for(int i=0;i<marks.length;i++){
//             for(int j=i+1;j<marks.length;j++){
//                 if(marks[i]==marks[j]){
//                     System.out.println(marks[i]);
//                 }
//             }
//         }
//     }
// }

// -----------------------------------------------------------------------
//             Sort array elements & merge karo
// -----------------------------------------------------------------------
// import java.util.*;
// public class arrays {

//     public static void main(String[] args) {
//         int i,j,size1,size2;
//         Scanner ob = new Scanner(System.in);
//         System.out.print("Enter the size of first array elements : ");
//         size1 = ob.nextInt();

//         System.out.print("Enter the size of second array elements : ");
//         size2 = ob.nextInt();

//         int[] arr1 = new int[size1];
//         int[] arr2 = new int[size2];
        
//         System.out.print("Enter the first element of array : ");
//         for(i=0;i<size1;i++){
//             arr1[i] = ob.nextInt();
//         }

//         System.out.print("Enter the second element of array : ");
//         for(i=0;i<size2;i++){
//             arr2[i] = ob.nextInt();
//         }
        

//         Arrays.sort(arr1);
//         Arrays.sort(arr2);
//         System.out.println(Arrays.toString(arr1));
//         System.out.println(Arrays.toString(arr2));


//         //  ak merged name ka array bana kar us me dono array ko add kar diya hai
//         int[] merged = new int[size1 + size2];

//         i = 0; // arr1 pointer
//         j = 0; // arr2 pointer
//         int k = 0; // merged pointer

//         while (i < size1 && j < size2) {
//             if (arr1[i] <= arr2[j]) {
//                 merged[k++] = arr1[i++];
//             } else {
//                 merged[k++] = arr2[j++];
//             }
//         }

//         while (i < size1) {
//             merged[k++] = arr1[i++];
//         }

//         while (j < size2) {
//             merged[k++] = arr2[j++];
//         }

//         System.out.println("Merged array: " + Arrays.toString(merged));

        

//     }
// }


// import java.util.*;
// public class arrays {

//     public static void main(String[] args) {
//         int i,j,size1,size2;
//         Scanner ob = new Scanner(System.in);
//         System.out.print("Enter the first element of array size : ");
//         size1=ob.nextInt();

//         System.out.print("Enter the second element of array size : ");
//         size2=ob.nextInt();

//         int[] arr1 = new int[size1];
//         int[] arr2 = new int[size2];
//         // ye result array me ham merge array fill karege
//         int[] result = new int[size1+size2];

//         // first array input le liyea
//         System.out.print("Enter the first elements : ");
//         for(i=0;i<size1;i++){
//             arr1[i]=ob.nextInt();
//         }

//         System.out.print("Enter the second elements : ");
//         for(i=0;i<size2;i++){
//             arr2[i]=ob.nextInt();
//         }

//         Arrays.sort(arr1);
//         Arrays.sort(arr2);

//         System.out.println(Arrays.toString(arr1));
//         System.out.println(Arrays.toString(arr2));

//         // merge formula  
//         for (i = 0; i < size1; i++) {
//             result[i] = arr1[i];
//         }

//         for (i = 0; i < size2; i++) {
//             result[size1 + i] = arr2[i];
//         }

//         Arrays.sort(result);
//         System.out.println(Arrays.toString(result));

//     }
// }


// Searching element

// public class arrays {

//     public static void main(String[] args) {
//         int[] arr = {10,20,30,40,50,60,70};
//         int target = 60;
//         boolean found1 = false;
//         for(int i=0;i<arr.length;i++){
//             if(arr[i]==target){
//                 found1=true;
//                 break;
//             }
            
//         }
//         if(found1){
//             System.out.println("present");
//         }
//         else{
//             System.out.println("not present");
//         }
//     }
// }

// public class arrays {

//     public static void main(String[] args) {
//         for(int i=1;i<=5;i++){
//             System.out.println("hello ji kese ho sare");
//         }
//     }
// }

import java.util.*;
public class arrays {

    public static void main(String[] args) {
        for(int i=1;i<=5;i++){
            for(int j=1;j<=i;j++){
                System.out.print("*");
            }
        }
        System.out.println();
       
    }
}

















































































































// Basic Level (1–15)

// Array ke sabhi elements print karo. ok
// Array ka sum nikalo. ok
// Array ka average nikalo. ok
// Array me maximum element find karo. ok
// Array me minimum element find karo. ok
// Array me even numbers count karo. ok
// Array me odd numbers count karo. ok
// Array me positive numbers count karo.    ok
// Array me negative numbers count karo.    ok
// Kisi given number ko search karo (Linear Search).
// Array ko reverse print karo. ok
// Array ke first aur last element swap karo.   ok
// Array me largest aur smallest element ka difference nikalo.  ok
// Array ke sabhi elements ka product nikalo.   ok
// Array me zero kitni baar aaya hai count karo.    ok

// Easy-Medium Level (16–30)

// Second largest element find karo. ok
// Second smallest element find karo.   ok
// Array ascending order me sort karo (without built-in sort).
// Array descending order me sort karo.
// Array me duplicate elements count karo.
// Duplicate elements print karo.
// Array me unique elements print karo.
// Array ke sabhi even elements alag array me store karo.
// Array ke sabhi odd elements alag array me store karo.
// Array ko left rotate by 1.
// Array ko right rotate by 1.
// Array ko k positions left rotate karo.
// Array ko k positions right rotate karo.
// Array me frequency of each element find karo.
// Check karo array sorted hai ya nahi.

// Medium Level (31–40)

// Third largest element find karo.
// Third smallest element find karo.
// Array me missing number find karo (1 to n series).
// Array me pair find karo jinka sum target ke equal ho.
// Array ke elements ko reverse karke new array banao.
// Array merge karo aur sort karo.
// Do arrays equal hain ya nahi check karo.
// Common elements between two arrays print karo.
// Do arrays ka union nikalo.
// Do arrays ka intersection nikalo.

// Interview-Oriented Level (41–50)

// Array me largest contiguous sum find karo (Kadane's Algorithm).
// Array me leaders find karo.
// Array me majority element find karo.
// Array me first repeating element find karo.
// Array me first non-repeating element find karo.
// Array me equilibrium index find karo.
// Array me subarray ka maximum product find karo.
// Array ko aise rearrange karo ki positive aur negative alternate aaye.
// Array me smallest missing positive number find karo.
// Array me longest consecutive sequence find karo.
// Challenge Order
// Practice is order me karo:
// 1–15 → Warm-up
// 16–30 → Logic Building
// 31–40 → DSA Foundation
// 41–50 → Interview Preparation