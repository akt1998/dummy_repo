public class Main{
    public static void main(String[] args){
        System.out.println("Hello World!");
        for(int i=0; i<args.length; i++){
            System.err.println(args[i]);
        }
    }
}