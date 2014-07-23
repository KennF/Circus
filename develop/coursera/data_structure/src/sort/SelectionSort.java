package sort;
import java.util.Collections;

public class SelectionSort {
	public static void sort(Comparable[] a){
		int N = a.length;
		for(int i = 0; i < N; i++){
			int min = i;
			for(int j = i + 1; j < N; j++){
				if (less(a[j] , a[min])){
					min = j;
				}
			}
			exch(a, i, min);
		}
	}
	
	public static void exch(Comparable[] a, int i, int j){
		System.out.format("exchange a[%d]=%d and a[%d]=%d \n", i, a[i], j, a[j]);
		Comparable swap = a[i];
		a[i] = a[j];
		a[j] = swap;
	}
	
	public static boolean less(Comparable a, Comparable b){
		if(a.compareTo(b) <= 0){
			return true;
		}
		return false;
	}
}

class SelectionSortTest {
    public static void main(String[] args) {
    	Integer[] a = {1, 212, 6, 6, 65, 23, 152};
    	
    	for(int i=0; i < a.length; i++){
    		System.out.println(a[i]);
    	}
    	
    	SelectionSort.sort(a);
    	
    	for(int i=0; i < a.length; i++){
    		System.out.println(a[i]);
    	}
    }
 }