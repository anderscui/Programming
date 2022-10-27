package tour.java.texts;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class basics {
    public static void main(String[] args) {
        Pattern re = Pattern.compile("(?<func>GetDate_(Day|Mon))\\(\\s*(?<param>-?\\d{1,3})?\\s*\\)", Pattern.CASE_INSENSITIVE | Pattern.UNICODE_CASE);
        String s = "select * from abc a where a.date1 = GetDate_Day() and a.date2=GetDate_Day(-1) and a.mon1=GetDate_Mon() and a.mon2=GetDate_Mon(-1)";
        Matcher matcher = re.matcher(s);
        while (matcher.find()) {
            System.out.println(matcher.group("func"));
            System.out.println(matcher.group("param"));
        }
    }
}
