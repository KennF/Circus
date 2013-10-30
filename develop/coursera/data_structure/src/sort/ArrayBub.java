package sort;

/**
 * Created with IntelliJ IDEA.
 * User: kennethfu
 * Date: 10/7/13
 * Time: 10:24 PM
 * To change this template use File | Settings | File Templates.
 */
class ArrayBub {
    private long[] a;
    private int nElems;

    public ArrayBub(int max) {
        a = new long[max];
        nElems = 0;
    }

    public void insert(long value) {
        a[nElems] = value;
        nElems = nElems + 1;
    }

    public void display() {
        for (int i = 0; i < nElems; i++) {
            System.out.print(a[i] + " ");
        }
        System.out.println("");
    }

    private void swap(int one, int two) {
        long temp = a[one];
        a[one] = a[two];
        a[two] = temp;
    }

    public void bubbleSort() {
        for (int out = nElems -1; out > 1; out--) {
//            System.out.println("round " + out);
            for (int in = 0; in < out; in++) {
                if (a[in] > a[in + 1]) {
                    swap(in, in + 1);
                }
//                this.display();
            }
        }
    }
}

class BubbleSortApp {
    public static void main(String[] args) {
        int maxSiza = 100;
        ArrayBub arr;
        arr = new ArrayBub(maxSiza);

        arr.insert(10);
        arr.insert(3);
        arr.insert(95);
        arr.insert(36);
        arr.insert(145);
        arr.insert(15);
        arr.insert(209);

        arr.display();
        arr.bubbleSort();
        arr.display();

    }

}
