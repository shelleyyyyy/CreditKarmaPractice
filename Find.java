public class Find{


    public static int findDouble(int [] arr){
        for(int i = 0; i < arr.length; i++){
            for(int j = i + 1; j < arr.length; j++){
                if(arr[j] == arr[i]){
                    return arr[i];
                }
            }
        }

        return -1;
    } 

    public static int contains(int [] arr, int k){
        int count = 0;
        for(int i = 0; i < arr.length; i++){
            if(arr[i] == k){
                count++;
            }
        }

        return count;
    }


    public static int findUnique(int [] arr){
        for(int i = 0; i < arr.length; i++){
            if(contains(arr, arr[i]) == 1){
                return arr[i];
            }
        }

        return -1;
    }


    public static void main(String[] args) {
        int [] arr = {1, 2, 3, 4, 5, 6, 7, 8, 9, 21, 1, 3, 4, 5, 6, 7, 8, 9, 2};

        int a = findUnique(arr);

        System.out.println(a);
    }
}