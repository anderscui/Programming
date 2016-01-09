import java.util.Map;
import java.util.HashMap;

public class Maps {

    public static void main(String[] args) {

    	Map<Character, Double> map = new HashMap<Character, Double>();
    	map.put('A', 1.0);
    	map.put('B', 2.0);
    	map.put('C', 3.0);

    	map.put('C', 3.1);
    	System.out.println(map.get('C'));
    	System.out.println(map.get('D')); // null

    	System.out.println(map.size());
    }
}
