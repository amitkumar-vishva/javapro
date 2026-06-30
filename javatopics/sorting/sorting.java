// --------------------------------------------------------------------------------
//     check karo ki array sort hai ya nahi
// --------------------------------------------------------------------------------
// import java.util.Arrays;

// public class sorting {

//     public static void main(String[] args) {
//         int[] arr = {9,8,7,6,5,4};
//         Arrays.sort(arr);
//         boolean isSorted = true;
//         for(int i=0;i<arr.length-1;i++){
//             if(arr[i]>arr[i+1]){
//                 isSorted=false;
//                 break;
//             }
//         }
//         if(isSorted){
//             System.out.println("sorted");
//         }
//         else{
//             System.out.println("not sorted");
//         }
//     }
// }


public class sorting {

    public static void main(String[] args) {
        int[] arr = {3,5,1,8,6};

        for(int i=0;i<arr.length-1;i++){
            for(int j=0;j<arr.length-1-i;j++){
                if(arr[j]>arr[j+1]){
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1]=temp;
                }
            }
        }

        for(int i=0;i<arr.length;i++){
            System.out.print(arr[i] +" ");
        }
    }
}