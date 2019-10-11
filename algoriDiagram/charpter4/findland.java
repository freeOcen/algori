
public class findland {
    public static void main(String[] args) {
        System.out.println("hello world这种");

        int[] arg = {1,2,12,3};
        System.out.println(sum(arg));
        System.out.println(count(arg));
        System.out.println(max(arg));
        
        
    }


    public static int count(int[] arg){
        //基线条件
        if(arg.length == 0 ){
            return 0;
        }else if(arg.length==1){
            return 1;
        }else {//递归条件
             return 1 + count(shift(arg));
        }
    }

    /**
     * 递归查找数组中最大值
     */
    public static int max(int[] arg){
        if(arg.length==2){
            return arg[0]>=arg[1]?arg[0]:arg[1];
        }
        
        // int[]array = shift(arg);
        int sub_max = max(shift(arg));
        return arg[0]>=sub_max?arg[0]:sub_max;
        

    }

    /**
     * 递归求和
     * @param arg
     * @return
     */
    public static int sum(int[] arg){
        int s = 0 ;
        if(arg.length==0){
            s= 0;
        }else if(arg.length==1){
            s = arg[0];
        }else{
            s = arg[0] + sum(shift(arg));
        }
        return s;
    }


    /**
     * 
     * @param array
     * @return
     */
    public static int[] shift(int[] array) {
        if (array == null) {
            throw new IllegalArgumentException();
        }

        if (array.length <= 1) {
            return new int[0];
        }

        int[] de = new int[array.length - 1];
        System.arraycopy(array, 1, de, 0, de.length);
        return de;

    }
}