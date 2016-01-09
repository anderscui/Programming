import java.nio.charset.Charset;
import java.util.HashMap;
import java.util.List;
import java.util.Locale;
import java.util.Map;
import java.util.Vector;
import java.util.regex.Matcher;
import java.util.Collections;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;

public class Io {

    public static void main(String[] args) {

        long s = System.currentTimeMillis();

        Io io = new Io();
    	InputStream is = io.getClass().getResourceAsStream("prob.txt");

        Map<Character, Map<Character, Double>> emit = new HashMap<Character, Map<Character, Double>>();
            Map<Character, Double> values = null;

        try {
            BufferedReader br = new BufferedReader(new InputStreamReader(is, Charset.forName("UTF-8")));

            while(br.ready()) {
                String line = br.readLine();
                String[] tokens = line.split("\t");
                if (tokens.length == 1) {
                    values = new HashMap<Character, Double>();
                    emit.put(tokens[0].charAt(0), values);
                }
                else {
                    values.put(tokens[0].charAt(0), Double.valueOf(tokens[1]));
                }
            }
        }
        catch (IOException e) {
            System.err.println(String.format(Locale.getDefault(), "%s: load model failure", "prob.txt"));
        }
        finally {
            try {
                if (is != null)
                    is.close();
            }
            catch (IOException e) {
                    System.err.println(String.format(Locale.getDefault(), "%s: load model failure", "prob.txt"));
                }
        }
    	
        /* System.out.println(String.format(Locale.getDefault(), "model load finished, time elapsed %d ms.",
            System.currentTimeMillis() - s)); */

        System.out.println(emit.size());
        System.out.println(values.size());
    }
}
