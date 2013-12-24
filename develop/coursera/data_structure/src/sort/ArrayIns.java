package sort;

/**
 * Created with IntelliJ IDEA.
 * User: kennethfu
 * Date: 10/8/13
 * Time: 11:54 PM
 * To change this template use File | Settings | File Templates.
 */
public class ArrayIns {
    private long a[];
    private int nElems;

    public ArrayIns(int max) {
        a = new long[max];
        nElems = 0;

    }

    public void insert(long value) {
        a[nElems] = value;
        nElems++;
    }

    public void display() {
        for (int i = 0; i < nElems; i++) {
            System.out.print(a[i] + " ");
        }
        System.out.println("");
    }

    public void insertionSort() {
        for(int out = 1; out < nElems; out++){
            long temp = a[out];
            int in = out;
            while(in>0 && a[in-1]>=temp){
                a[in] = a[in-1];
                in--;
            }
            a[in] = temp;

        }
    }

}

class InsertionSortApp {
    public static void main(String[] args) {
        int maxSiza = 100;
        ArrayIns arr;
        arr = new ArrayIns(maxSiza);

        arr.insert(77);
        arr.insert(99);
        arr.insert(55);
        arr.insert(22);
        arr.insert(88);
        arr.insert(11);
        arr.insert(00);
        arr.insert(66);
        arr.insert(33);

        arr.display();
        arr.insertionSort();
        arr.display();
    }
}

