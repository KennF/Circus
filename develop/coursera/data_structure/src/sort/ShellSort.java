package sort;
import java.util.Collections;

public class ShellSort {
	public static void sort(Comparable[] a){
		int N = a.length;
		System.out.println(N);
		int h = 1;
		while( h < N/3){
			h = h * 3 + 1;
		}
//		h = 3 * h + 1;
		System.out.format("===the distance is %d \n", h);
		while(h >= 1)
		{	
			for(int i = 0; i < N; i = i + h){		
				for(int j = i; j > 0; j = j - h){
					if (less(a[j] , a[j-h])){
						exch(a, j, j-h);
					}
				}
			}
			h = h/3;
			System.out.format("===the distance is %d \n", h);
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

class ShellSortTest {
    public static void main(String[] args) {
    	Integer[] a = {3, 212, 6, 6, 65, 23, 152, 1, 53, 68, 67457, 4524, 423, 64, 5906, 4589,
    			45831, 4524, 453248, 56849, 434549, 314341, 48945, 242, 678, 34, 41, 23, };
    	
    	for(int i=0; i < a.length; i++){
    		System.out.println(a[i]);
    	}
    	
    	ShellSort.sort(a);
    	
    	for(int i=0; i < a.length; i++){
    		System.out.println(a[i]);
    	}
    }
 }