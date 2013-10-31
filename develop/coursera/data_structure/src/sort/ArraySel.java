package sort;

/**
 * Created with IntelliJ IDEA.
 * User: kennethfu
 * Date: 10/8/13
 * Time: 11:33 PM
 * To change this template use File | Settings | File Templates.
 */
public class ArraySel {
    private long a[];
    private int nElems;

    public ArraySel(int max) {
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

    private void swap(int one, int two) {
        long temp = a[one];
        a[one] = a[two];
        a[two] = temp;
    }

    public void selectionSort() {
        for (int i = 0; i < nElems - 1; i++) {
            int min_pos = i;
            for (int j = i; j < nElems; j++) {
                if (a[j] < a[min_pos]) {
                    min_pos = j;
                }
            }
            swap(i, min_pos);
        }
    }

}

class SelectionSortApp {
    public static void main(String[] args) {
        int maxSiza = 100;
        ArraySel arr;
        arr = new ArraySel(maxSiza);

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
        arr.selectionSort();
        arr.display();
    }
}
